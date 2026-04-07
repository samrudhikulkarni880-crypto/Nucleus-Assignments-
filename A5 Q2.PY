def main():
    #write a recursive function to generate fibonacci numbers
    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)
    num = 8
    print("Fibonacci sequence up to", num, ":")
    for i in range(num):
        print(fibonacci(i), end=' ')
if __name__=="__main__":    
    main()