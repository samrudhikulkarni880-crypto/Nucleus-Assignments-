def main():
#find the factorial of a number using a loop
    num = int(input("Enter a number: "))
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
    



if __name__=="__main__":
    main()