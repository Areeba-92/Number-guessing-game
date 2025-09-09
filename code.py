#Write a game of number guessing
import random
def game():
# Get the computer choices 
   comp = random.randint(1,100)

   num =-1
   #  for attempts counting
   guess_no = 1

   # determine the outcomes/results
   while (num!=comp):
      num= int(input ("Guess the number from 1 to 100 : "))
      if (comp > num):
         print("higher number please")
         guess_no +=1
      elif (comp < num):
         print("lower number please")
         guess_no +=1
   print("..............................")
   print(f"computer choose : {comp}")
   print(f"you choose  : {num}")

   print(f"You have  Guess the correct no {comp } in {guess_no} attemps .")


if __name__ == "__main__":
   game()
