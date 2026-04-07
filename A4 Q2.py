def main():

#write a program to find the smallest element in array
    
    arr = [1,2,3,4,5,6,7,8,9,10]
    smallest = arr[0] 
    
    for i in range(1,len(arr)):
        
        if arr[i] < smallest:
            smallest = arr[i]    

    
    print("Smallest element in array is:",smallest)



if __name__=="__main__":
    main()