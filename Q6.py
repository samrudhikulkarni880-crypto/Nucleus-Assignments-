def is_alphabe(list):
    consonent = 0
    vovel= 0
    for i in list:
        if i in "aeiouAEIOU":
            vovel+=1
        else:
            consonent+=1
    return vovel,consonent
        
def main():

    list = ("a","b","c","d","e","f","g","h","i","j")
    vovel,consonent = is_alphabe(list)
    

    print(f"vovel number:{vovel}")
    print(f"consonent number:{consonent}")


if __name__=="__main__":
    main()






