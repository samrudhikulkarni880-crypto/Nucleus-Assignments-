def main():

#write a program to reverse an array
    arr = [2,4,7,11,90,3,73,18,43,56]
    rev_arr = []
    for i in range(len(arr)-1,-1,-1):
        rev_arr.append(arr[i]) 
    print("Reversed array is:",rev_arr)


if __name__=="__main__":
    main()