def main():
#write a program to count the number of digits in a number
    num = int(input("Enter a number: "))
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print(f"The number of digits in the number is {count}")
    



if __name__=="__main__":
    main()