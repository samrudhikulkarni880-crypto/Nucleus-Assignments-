def main():

#write a program to count even or odd number in array
    
    arr = [1,12,23,5,8,50,7,9,10]
    even = 0
    odd = 0
    
    for i in range(len(arr)):
        
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even numbers in array:", even)
    print("Odd numbers in array:", odd)


if __name__=="__main__":
    main()