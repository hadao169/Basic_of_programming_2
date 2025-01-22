import random

finnish_queries = {
    "Hello": "What does 'Hei' mean in English?",
    "Thank you": "What is the English translation of 'Kiitos'?",
    "Love": "What does 'Rakkaus' translate to in English?",
    "Friend": "What is the meaning of 'Ystävä' in English?",
    "House": "What is the English word for 'Talo'?",
    "Home": "How do you say 'Koti' in English?",
    "School": "What does 'Koulu' mean in English?",
    "Water": "What is the English translation of 'Vesi'?",
    "Sun": "How do you translate 'Aurinko' to English?",
    "Book": "What does 'Kirja' mean in English?"
}

def word_quiz(quiz: dict):
    point = 0
    keys_list = list(quiz.keys()) 
    for i in range(10):
        rdIndex = random.randint(0, len(keys_list) - 1)  
        rdWord = keys_list[rdIndex]
        answer = input(f"Give your answer: {quiz[rdWord]} ")

        if answer.casefold() == rdWord.casefold():
            print("Correctly! You got 1 point.")
            point += 1
            keys_list.remove(rdWord)  
        else:
            print("It's wrong! Let's try again.")

    print(f"Your total point: {point}")
    
    new_round = input("Do you want to play a new round: (Y/N)")
    if(new_round.casefold() == "y"):
      print("Let's play next round!")
      word_quiz(quiz)
    elif(new_round.casefold() == "n"):
      return

word_quiz(finnish_queries)
