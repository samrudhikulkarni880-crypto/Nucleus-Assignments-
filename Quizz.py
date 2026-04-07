# Quiz Application

score = 0

questions = [
    ("Who is Krishna?", ["God", "Friend", "Guide", "Everything"], 1),
    ("Capital of India?", ["Mumbai", "Delhi", "Chennai", "Kolkata"], 2),
    ("2 + 2 = ?", ["3", "4", "5", "6"], 2),
    ("Which language is used for web?", ["Python", "HTML", "C", "Java"], 2),
    ("Sun rises in?", ["North", "South", "East", "West"], 3),
    ("Largest planet?", ["Earth", "Mars", "Jupiter", "Venus"], 3),
    ("H2O is?", ["Oxygen", "Hydrogen", "Water", "Salt"], 3),
    ("Fastest animal?", ["Lion", "Tiger", "Cheetah", "Horse"], 3),
    ("Binary of 2?", ["10", "11", "01", "00"], 1),
    ("CPU stands for?", [
        "Central Process Unit",
        "Central Processing Unit",
        "Computer Personal Unit",
        "Central Power Unit"], 2)
]

# Loop through questions
for q, options, answer in questions:
    print("\n" + q)
    
    for i in range(4):
        print(f"{i+1}. {options[i]}")

    # Input validation
    while True:
        try:
            choice = int(input("Enter your choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Enter number between 1 to 4 only.")
        except:
            print("Invalid input! Enter a number.")

    if choice == answer:
        score += 1

# Result
print("\nQuiz Completed!")
print("Your Score:", score, "/10")
