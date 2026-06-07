import random

print("Guess the number Game")

print("Choose difficulty:")
print("1.Easy(10 attempts)")
print("2. Medium(7 attempts)")
print("3. Hard(5 attempts)")

choice= input("Enter your choice( 1,2, or 3):")
 
if choice == "1":
    attempts=10
elif choice== "2":
    attempts=7
elif choice== "3":
    attempts=5

else:
    print("Invalid choice. Defaulting to Easy.")

number = random.randint(1,100)

while attempts> 0:
    guess= int(input("Guess a number between 1 and 100:"))

    if guess == number: 
        print("Congratulations! You guessed right")
        break
    elif guess> number: 
        print("Too high")
    else: 
        print("Too low")
    attempts-=1
    if attempts>0:
        print("Attempts left:",attempts)        

if attempts==0:
    print("Game over!")        
    print("The number was:",number)

   
       
