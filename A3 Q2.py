def main():
    #write  a program to reverse a number
    
    reverse = 0
    list = [1,2,3,4,5,6,7,8,9]
    list.reverse()
    for i in list:
        reverse = reverse*10 + i
    print(f"The reverse of the number is {reverse}")
    
if __name__=="__main__":
    main()