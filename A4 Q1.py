def main():

#write a program to find the largest element in array
    
    arr = [1,2,3,4,5,6,7,8,9,10]
    largest = arr[0] 
    
    for i in range(1,len(arr)):
        
        if arr[i] > largest:
            largest = arr[i]    
    
    print("Largest element in array is:",largest)


if __name__=="__main__":    
    main()