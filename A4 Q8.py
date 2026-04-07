def main():

#write a program to remove duplicates from an array
    
    arr = [1,2,2,3,4,4,5,6,7,7,8,9,10,52,78,95,52,78]
    main_arr = [] 
    
    for i in range(len(arr)):
        
        if arr[i] not in main_arr:
            main_arr.append(arr[i])

    print("Array after removing duplicates:", main_arr)


if __name__=="__main__":
    main()