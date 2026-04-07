def main():
    #write a lambda/ananymous function to calculate the square of a number
    square = lambda x: x ** 2
    num = 7
    print("The square of", num, "is", square(num))
if __name__=="__main__":
    main()