def H():
    return ["*   *", "*   *", "*****", "*   *", "*   *"]

def A():
    return ["  *  ", " * * ", "*   *", "*****", "*   *"]

def P():
    return ["**** ", "*   *", "**** ", "*    ", "*    "]

def Y():
    return ["*   *", " * * ", "  *  ", "  *  ", "  *  "]

def B():
    return ["**** ", "*   *", "**** ", "*   *", "**** "]

def I():
    return ["*****", "  *  ", "  *  ", "  *  ", "*****"]

def R():
    return ["**** ", "*   *", "**** ", "*  * ", "*   *"]

def T():
    return ["*****", "  *  ", "  *  ", "  *  ", "  *  "]

def D():
    return ["**** ", "*   *", "*   *", "*   *", "**** "]

# Store all letters in dictionary
letters = {
    'H': H(), 'A': A(), 'P': P(), 'Y': Y(),
    'B': B(), 'I': I(), 'R': R(), 'T': T(), 'D': D(),
    ' ': ["     "] * 5
}

def print_message(msg):
    msg = msg.upper()
    for i in range(5):
        for ch in msg:
            print(letters[ch][i], end="  ")
        print()

def main():
    message = "HAPPY BIRTHDAY"
    print_message(message)

if __name__ == "__main__":
    main()