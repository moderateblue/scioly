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

print("random numbers only infinite (rn)\n"
      "random letters only infinite (rl)\n"
      "numbers in order infinite (n)\n"
      "letters in order infinite (l)\n"
      "timed all (t)\n"
      "timed numbers (tn)\n"
      "timed letters (tl)")

usr = input("what mode would you like to use: ")

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
        if 'acc' in globals():
            global acc
            acc -= 1
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
        if 'acc' in globals():
            global acc
            acc -= 1
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

if usr == "rn":
    while run:
        global number 
        number = random.choice(numbers)
        print("\n" + str(numbers.index(number)))
        with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
            listener.join()

elif usr == "rl":
    while run:
        global letter
        letter = random.choice(list(letters.keys()))
        print("\n" + letter)
        # Collect events until released
        with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
            listener.join()

elif usr == "t":
    global acc
    acc = 36
    start = time.perf_counter()

    for letter in letters:
        print("\n" + letter)
        with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
            listener.join()
    for number in numbers:
        print("\n" + str(numbers.index(number)))
        with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
            listener.join()
    
    stop = time.perf_counter()
    print("\ntime: " + str(stop - start) + " seconds")
    print("accuracy: " + str(acc/36 * 100) + "% (" + str(acc) + "/36)")

elif usr == "n":
    while run:
        for number in numbers:
            print("\n" + str(numbers.index(number)))
            with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
                listener.join()

elif usr == "l":
    while run:
        for letter in letters:
            print("\n" + letter)
            # Collect events until released
            with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
                listener.join()

elif usr == "tn":
    acc = 10
    start = time.perf_counter()

    for number in numbers:
        print("\n" + str(numbers.index(number)))
        with keyboard.Listener(on_press = on_press, on_release = on_release_number) as listener:
            listener.join()
    
    stop = time.perf_counter()
    print("\ntime: " + str(stop - start) + " seconds")
    print("accuracy: " + str(acc/10 * 100) + "% (" + str(acc) + "/10)")

elif usr == "tl":
    acc = 26
    start = time.perf_counter()

    for letter in letters:
        print("\n" + letter)
        with keyboard.Listener(on_press = on_press, on_release = on_release_letter) as listener:
            listener.join()
    
    stop = time.perf_counter()
    print("\ntime: " + str(stop - start) + " seconds")
    print("accuracy: " + str(acc/26 * 100) + "% (" + str(acc) + "/26)")
