def main():
    #write a function to check whether number is prime
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = 47
    if is_prime(num):
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

if __name__=="__main__":
    main()