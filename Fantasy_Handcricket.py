import random
import time

print("*******Hand Cricket - THE LEGACY*******")
time.sleep(2)
name = input("What should we call you? ")
time.sleep(1)
print("Since time immemorial, humans have had ruled over Edora IV...")
time.sleep(3)
print("The turmoil began a century ago, whe the Machines came...")
time.sleep(3)
print("The Machines began ruling over the land of Edora IV, and enslaved all humans ")
time.sleep(3)
print(f"You are {name}, the greatest warrior of all time!")
time.sleep(3)
print("You must win against the Machines to free us.")
time.sleep(3)
print(f"It is You vs the Machines. Don't dissappoint us, {name}!")
time.sleep(5)


def toss(comp, you):
    
    if you == comp:
        time.sleep(1)
        print("The toss turned out to be a tie")
        time.sleep(1)
        return 1
    elif you != comp:
        time.sleep(1)
        print ("Tossed!")
        return 0

def bat():

    sum = 0
    flag = 1

    while(flag):

        print("The Machine has balled!")
        comp_ball = random.randint(1,6)
        you_bat = int(input("Bat: "))
        if you_bat != comp_ball:
            sum = sum + you_bat
            flag = 1
        else:
            print("OUT!")
            flag = 0
        
    return(sum)

def comp_bat():
     flag = 1
     sum = 0
     
     while(flag):
         
         comp_bat = random.randint(1, 6)
         you_ball = int(input("Ball: "))
         if you_ball == comp_bat:
             print("The Machine is finally OUT!")
             flag = 0
         else:
             sum += comp_bat
             flag = 1
    
     return sum

flag = 1

while flag:

    print("The Machine has tossed")
    comp = random.randint(1, 2)
    time.sleep(1)
    you = int(input("Your turn: "))
    flag = toss(comp, you)
    
boss_toss = random.randint(1, 2)

if(you == boss_toss):
    time.sleep(1)
    print("You Won the Toss!")
    time.sleep(1)
    you_choice = int(input("Choose to Bat(1) or Ball(2), beware, your choices have grave consequences: "))
    if(you_choice==1):
        time.sleep(1)
        print("You chose Bat!")
        time.sleep(1)
        your_score = bat()
        time.sleep(1)
        print(f"You scored: ", your_score)
        time.sleep(1)
        print("Your turn to Ball! ")
        comp_score = comp_bat()
        time.sleep(1)
        print("Machine Scored: ", comp_score)
    else:
        time.sleep(1)
        print("You chose Ball! ")
        comp_score = comp_bat()
        time.sleep(1)
        print("The Machine Scored: ", comp_score)
        time.sleep(1)
        print("Your turn to Bat! ")
        your_score = bat()
        time.sleep(1)
        print(f"Your Runs: ", your_score)

    time.sleep(1)
    print(f"Machine v You: ", comp_score , your_score)
    time.sleep(1)

else:
    time.sleep(1)
    print("The Machine Won the Toss")
    comp_choice = random.randint(1, 2)
    if comp_choice == 1:
        time.sleep(1)
        print("The Machine chooses Bat!")
        comp_score = comp_bat()
        time.sleep(1)
        print(f"The Machine Scored: ", comp_score)
        time.sleep(1)
        print("Your turn to Bat ")
        your_score = bat()
        time.sleep(1)
        print("You Scored: ", your_score)
    else:
        time.sleep(1)
        print("The Machine chose Ball!")
        time.sleep(1)
        your_score = bat()
        time.sleep(1)
        print("Your Score: ", your_score)
        time.sleep(1)
        print("The Machine's turn to Bat! ")
        comp_score = comp_bat()
        time.sleep(1)
        print(f"The Machine's Runs: ", comp_score)
    
    time.sleep(1)
    print(f"Machine v You: ", comp_score , your_score)

if your_score == comp_score:
    time.sleep(1)
    print("Nice Try. Edora is not disappointed.")
elif your_score > comp_score:
    time.sleep(1)
    print("You won, and saved Edora!")
else:
    time.sleep(1)
    print("You lost, and you are a big dissapointment.")