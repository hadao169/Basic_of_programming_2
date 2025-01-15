import random
fruits = [["🍎", "🍌", "🍇", "🍒", "🍓", "🌽"], 
          ["🍓", "🍇", "🍌", "🌽", "🍎", "🍒"], 
          ["🍌", "🍒", "🌽", "🍇", "🍓", "🍎"]]

def slot_game(fruits: list):
  money = 10  
  print("Welcome to the Slot Game!")
  print("Your starting balance is $10.")
  
  while(money > 0):
    myList = []
    result = True
    # Generate the slot results
    for i in range(3):
      fruit = random.choice(fruits[i])
      myList.append(fruit)
    print("Slot result: ",myList)
  
    # Check if all fruits are the same
    for j in myList:
      if(j != myList[0]):
        result = False
        break
    
    if(result == True):
      print("Congratulation, you've just won 5$")
      money += 5
    else:
      print("Sadly, you lost 1$!")
      money -= 1
    
    print("Your current balance: ",money)
    
    if(money > 0):
      query = input("Do you want to continue (y/n)").lower()
      if(query == "y"):
        continue
      elif(query == "n"):
        print("Thank for playing our game! See you next time.")
        return    
  print("Game Over!")    
  
slot_game(fruits)

  