def main():
    #write a program to check whether a number is palindrome

    num = int(input("Enter a number: "))
    original_num = num
    reverse = 0
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num //= 10
    if original_num == reverse:
        print(f"{original_num} is a palindrome number.")
    else:
        print(f"{original_num} is not a palindrome number.")
        
if __name__=="__main__":
    main()

'''Example for my understanding: 123 % 10 = 3
reverse = 0 → (0×10 + 3) = 3
reverse = 3 → (3×10 + 2) = 32
reverse = 32 → (32×10 + 1) = 321'''