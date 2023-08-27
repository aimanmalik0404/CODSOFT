print("     Welcome to Quiz Game     ")
questions=[["Which is the largest planet of solar system?",
            "Saturn","Jupiter","Mars","Neptune",
            1],
           ["Which is the largest country(area) in the world?",
            "US","China","Russia","Japan",
            2],
           ["Which is the smallest country in the world?",
            "Maldives","San Marino","Nauru","Vatican",
            3],
           ["Which is the highest valued currency in the world?",
            "Kuwaiti Dinar","british Pound Sterling","Omani Rial","Bahrain Dinar",
            0],
           ["Who is the highest paid actor in the world?",
            "Tom Cruise","Will Smith","Leonardo Dicaprio","Jackie Chan",
            0],
           ["Which is the largest ocean in the world",
            "Indian Ocean","Atlantic Ocean","Pacific Ocean","Arctic Ocean",
            2],
           ["Where is the international court of justice located?",
            "The Hague", "Geneva", "Washington", "New York",
            0],
           ["What is the currency of Indonesia?",
            "riyal", "rupiah", "dinar", "rangit",
            1],
           ["Organization of Islamic Cooperation (OIC) has how many official languages?",
            "1", "4", "3", "2",
            2],
           ["How many members are there in SAARC?",
            "8", "6", "5", "7",
            0]]
levels=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]
i=0
for i in range(0, len(questions)):
    question=questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"Your question is: {question[0]}")
    #print(f"Your question is: {question[6]}")
    #print(f"Your question is: {question[12]}")
    #print(f"Your question is: {question[18]}")
    print(f"0). {question[1]}       1). {question[2]}")
    print(f"2). {question[3]}       3). {question[4]}")
    reply=int(input("Enter your answer(0-3):"))
    if (reply==question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        #print(f"Your take home money is {levels[i]}")
    else:
        print("Wrong answer!")
        print(f"Correct answer is:{question[-1]}")
        print(f"Your take home money is {levels[i-1]}")
        break
again=str(input("Do you want to play again? Yes or No:"))
if (again=="Yes"):
    i=0
    for i in range(0, len(questions)):
        question=questions[i]
        print(f"\n\nQuestion for Rs. {levels[i]}")
        print(f"Your question is: {question[0]}")
    #print(f"Your question is: {question[6]}")
    #print(f"Your question is: {question[12]}")
    #print(f"Your question is: {question[18]}")
        print(f"0). {question[1]}       1). {question[2]}")
        print(f"2). {question[3]}       3). {question[4]}")
        reply=int(input("Enter your answer(0-3):"))
        if (reply==question[-1]):
            print(f"Correct answer, You have won Rs. {levels[i]}")
        #print(f"Your take home money is {levels[i]}")
        else:
            print("Wrong answer!")
            print(f"Correct naswer is:{question[-1]}")
            print(f"Your take home money is {levels[i-1]}")
            break
elif (again=="No"):
    print("Game Over")
    
    
       
