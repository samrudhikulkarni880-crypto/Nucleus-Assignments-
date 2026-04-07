def main():
    #write a memorized recursive fibonacci function to improve performance
    pass

def memoized_fibonacci(n, memo={}):
        if n in memo:
            return memo[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            memo[n] = memoized_fibonacci(n-1, memo) + memoized_fibonacci(n-2, memo)
            return memo[n]

        
if __name__ == "__main__":
    main()