questions = [
    ["Which language is used to make FB?" , "python", "french",
     "JavaScript","none", 4],

    ["Which language is used to make FB?" , "python","french",
     "JavaScript","none", 4],

    ["Which language is used to make FB?" , "python","french",
     "JavaScript","none", 4],

    ["Which language is used to make FB?" , "python","french",
     "JavaScript","none", 4],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 400000, 80000, 160000, 320000]
money = 0
i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n\nQuestin for Rs. {levels[i]}")
    print(f"a. {question[1]}          b. {question[2]}")
    print(f"c. {question[3]}          d. {question[4]} ")

    reply = int(input("Enter your answer(1-4) or press 0 to quit : "))

    if(reply == 0):
        money = levels[i-1]
        break

    if reply == question[-1]:
        print(f"Correct Answer, you have won {levels[i]}")
        if(i == 4):
            money =10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000

    else:
        print("Wrong answer!")
        break

print(f"Your available money is {money}")