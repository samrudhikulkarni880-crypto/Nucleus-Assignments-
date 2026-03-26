def is_even(list):
    even = 0
    odd = 0
    for i in list:
        if i%2 ==0:
            even+=1
        else:
            odd+=1
    return even,odd
        
def main():

    list = (1,2,3,4,5,6,7,8,9,10)
    even,odd = is_even(list)
    

    print(f"even number:{even}")
    print(f"odd number:{odd}")


if __name__=="__main__":
    main()




