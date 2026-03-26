def main():

#write a program to print the fibonacci sequence uo to N terms
   
    n = int(input("Enter the number of terms: "))
    a, b = 0, 1
    print("Fibonacci sequence:")
    for _ in range(n):
        print(a)
        a, b = b, a + b
        
if __name__=="__main__":
    main()