import random

n=random.randint(1,100)
a=-1
guesses=0
print("Guess the numebr from 1 to 100 computer already choose the number now its your turn lets see how many attemps its takes you to guess teh number ")
try:
 while(a!= n): 
   guesses+=1
   a=int(input("Guess the number = "))

   if(a>n):
    print("guess the lower number ")
   else:
    print("guess the higher number ")
except Exception as e:
 print("something wents wrong ")

print(f"you guess the number in {guesses} attemp and the correct number is {n}")        