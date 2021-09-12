import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


print("what do you choose?.0 for rock 1 paper and 2 for scissors")
choose = int(input())
if choose == 0:
  choose = rock
elif choose == 1:
  choose = paper
elif choose == 2:
  choose = scissors    
else:
  print("wrong num choose again from 0 to 2 ")

print(choose)

print("computer choose")
com_choose = [rock,paper,scissors]
com_choose = (random.choice(com_choose))
print(com_choose)

if com_choose == rock and choose == rock:
  print("draw")
elif com_choose == rock and  choose == paper:
  print("you won")
elif com_choose == rock and choose == scissors: 
  print("you lose") 
else:
  pass

if com_choose == paper and choose == paper:
  print("draw")
elif com_choose == paper and  choose == rock:
  print("you lose")
elif com_choose == paper and choose == scissors: 
  print("you won") 
else:
  pass
  
if com_choose == scissors and choose == scissors:
  print("draw")
elif com_choose == scissors and  choose == paper:
  print("you lose")
elif com_choose == scissors and choose == rock: 
  print("you won") 
else:
  pass  