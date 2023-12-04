import random, time, sys, msvcrt, os
from pynput import keyboard

letters = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

numbers = [
    "-----",
    ".----",
    "..---",
    "...--",
    "....-",
    ".....",
    "-....",
    "--...",
    "---..",
    "----.",
]

print("welcome to morse code practice-r")
print("type stop to stop at any time")

usr = input("number (n) or letter (l) or timed (t): ")

run = True

charlist = []

def delete_line():
    #cursor up one line
    #sys.stdout.write('\x1b[1A')

    #delete line
    sys.stdout.write('\x1b[2K')
    #move cursor to beginning of line
    sys.stdout.write('\x1b[0E')


def on_press(key):
    try:
        print(key.char, end="")
        charlist.append(key.char)
    except AttributeError:
        #print('special key {0} pressed'.format(key))
        pass

def on_release_letter(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        while msvcrt.kbhit():
            msvcrt.getch()
        # Stop listener
        return False
    elif len(charlist) > 5:
        charlist.clear()
        print("\n" + letters[letter], end = "")
        while msvcrt.kbhit():
            msvcrt.getch()
        return False
    elif charlist == list(letters[letter]):
        charlist.clear()
        while msvcrt.kbhit():
            msvcrt.getch()
        return False
    elif charlist == list("stop"):
        while msvcrt.kbhit():
            msvcrt.getch()
        os._exit(0)
        #charlist.clear()
        #global run
        #run = False
        #while msvcrt.kbhit():
        #    msvcrt.getch()
        #return False
    elif key == keyboard.Key.backspace:
        if len(charlist) > 0:
            charlist.pop()
            delete_line()
            for x in charlist:
                print(x, end = "")

def on_release_number(key):
    if key == keyboard.Key.esc:
        while msvcrt.kbhit():
            msvcrt.getch()
        # Stop listener
        return False
    elif len(charlist) > 5:
        charlist.clear()
        print("\n" + number, end = "")
        while msvcrt.kbhit():
            msvcrt.getch()
        return False
    elif charlist == list(number):
        charlist.clear()
        while msvcrt.kbhit():
            msvcrt.getch()
        return False
    elif charlist == list("stop"):
        while msvcrt.kbhit():
            msvcrt.getch()
        os._exit(0)
        #charlist.clear()
        #global run
        #run = False
        #while msvcrt.kbhit():
        #    msvcrt.getch()
        #return False
    elif key == keyboard.Key.backspace:
        if len(charlist) > 0:
            charlist.pop()
            delete_line()
            for x in charlist:
                print(x, end = "")

if usr == "n":
    while run:
        global number 
        number = random.choice(numbers)
        print("\n" + str(numbers.index(number)))
        with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
            listener.join()

elif usr == "l":
    while run:
        global letter
        letter = random.choice(list(letters.keys()))
        print("\n" + letter)
        # Collect events until released
        with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
            listener.join()

elif usr == "t":
    start = time.perf_counter()

    for letter in letters:
        print("\n" + letter)
        with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
            listener.join()
    for i in numbers:
        number = i
        print("\n" + str(numbers.index(number)))
        with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
            listener.join()
    
    stop = time.perf_counter()
    print("\ntime: " + str(stop - start) + " seconds")
