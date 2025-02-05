import random
import json
f1 = open("word_quiz/englishwords.json")
f2 = open("word_quiz/finnishwords.json")
english_words = json.load(f1)
finnish_words = json.load(f2)

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

if __name__=="__main__":
    language = input("Choose the language you want to play (e/f): ")
    if(language.casefold() == 'f'):
        word_quiz(finnish_words)
    elif(language.casefold() == 'e'):
        word_quiz(english_words)
    else:
        print("Invalid language")
