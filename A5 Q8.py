def main():
    #write a function to calculate power (x^y) using recursion
    def power(a, b):
        if b == 0:
            return 1
        else:
            return a * power(a, b-1)
    base = 7
    exponent = 17
    print(base, "raised to the power of", exponent, "is", power(base, exponent))    
if __name__=="__main__":    
    main()