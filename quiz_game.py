def main():
    
    question_set_1 = {"Who is National Crush?":["Rashmika","Aneet","Samrudhi","Alia",2],
                    "Which is my fav dish?":["dal tadka","bharli vangi","paneer masala","shepu",3],
                    "which is my favorite hobby?":["dancing","eating","crying","singing",0],
                    "which is my favorite Team?":["CSK","RCB","MI","KKR",1],
                    "who is my favorite animal?":["cat","dog","peocock","sparrow",3]}
    
    question_set_2 ={"what is the capital of India?":["Mumbai","Delhi","Chennai","Kolkata",1],
                    "what is the currency of India?":["Dollar","Euro","Rupee","Yen",2],
                    "which is the largest continent?":["Asia","Africa","Europe","Australia",0],
                    "which is the longest river?":["Nile","Amazon","Yangtze","Mississippi",0],
                    "which is the highest mountain?":["Everest","K2","Kangchenjunga","Lhotse",0]}
    
    question_set_3 ={"which is the smallest unit of life?":["Cell","Atom","Molecule","Organ",0],
                    "which is the largest organ in human body?":["Heart","Liver","Skin","Brain",2],
                    "which is the fastest land animal?":["Cheetah","Lion","Tiger","Leopard",0],
                    "which is the largest mammal?":["Elephant","Blue Whale","Giraffe","Hippopotamus",1],
                    "which is the most abundant gas in Earth's atmosphere?":["Oxygen","Nitrogen","Carbon Dioxide","Argon",1]}
    
    question_set_4 ={"What does CPU stand for?":["Central Processing Unit","Computer Personal Unit","Central Power Unit","Central Process Unit",0],
                    "Which programming language is used for web development?":["Python","HTML","C","Java",1],
                    "What is the binary representation of 5?":["101","110","111","100",0],
                    "Which company developed the Windows operating system?":["Apple","Microsoft","Google","IBM",1],
                    "What does RAM stand for?":["Random Access Memory","Read Access Memory","Run Access Memory","Random Access Machine",0]}
    
    question_sets = [question_set_1,question_set_2,question_set_3,question_set_4]
    
    Terminator = True

    print("message:for more details type help")
    option = 1
    
    while(Terminator):
        
        cmd = input(">>>")
        
        if cmd == "exit":
            exit()
        
        elif cmd == "help":
            
            print("""
                  To start the game just say "start"
                  If you want to stop just say "exit"
                  If you want to choose different topics just say "options
                  To add your own quiz just say "add-quiz"
                  """)
        elif cmd == "options":
            
            print("""
                  type 1 for : MYTHOLOGICAL QUESTIONS
                  type 2 for : GK QUESTIONS
                  type 3 for : SCIENTIFIC QUESTIONS
                  type 4 for : COMPUTER QESTIONS
                  type 5 for : HISTORICAL QUESTIONS
                  """)
            
            option = int(input(">>>"))

        elif cmd == "start":
                
            point = 0
            
            for question in question_sets[option]:
                    print(question+"\n")
                    
                    for ops in range(0,len(question_sets[option][question])-1):
                        print("\t",ops+1,question_sets[option][question][ops])
                    
                    #ans = int(input())-1
                    ans = input()
                    
                    if ans.isdigit():
                        ans = int(ans)-1

                    elif ans == "exit":
                        print(f"You score{point}/5") 
                        exit()
                    
                    if question_sets[option][question][-1] == ans:
                        point +=1
                    
                    print(f"You score{point}/5")
        
        elif cmd == "add-quiz":
            quiz = {}
            options = []
            
            print("Enter quiz title ")
            title = input()
            
            for question in range(1,6):
                    print(f"Enter question no.{question}")
                    key = input()

                    for val in range(0,6):
                        
                        if val == 5:
                             value =input("Enter an answer of this question : ")
                        else :
                             value =input(f"Enter option {val}:")

                        options.append(value)
                    quiz[key] = options
                    
                    question_sets.append(quiz)
                    option = -1

if __name__ == "__main__":
    main()

    