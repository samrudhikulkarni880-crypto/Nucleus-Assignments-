def main():

#write a program to search for an element in array
    arr = [1,2,3,4,5,6,7,8,9,10]
    element = int(input("Enter the element to search: "))
    found = 0
    for i in range(len(arr)):
        if arr[i] == element:
            found = 1
            break

    if found:
        print("Element found in the array.")
    else:
        print("Element not found in the array.")


if __name__=="__main__":
    main()