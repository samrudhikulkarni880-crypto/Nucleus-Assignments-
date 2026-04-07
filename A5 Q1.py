def main():
    #write a recursive function to calculate factorial
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    num = 7
    print("Factorial of", num, "is", factorial(num))
if __name__=="__main__":    
    main()