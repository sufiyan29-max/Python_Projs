#Rock paper Scissor -_-

import random
print('''

Rock=1
Paper=2
scissor=3

''')

#computer chance

choices = [1,2,3]
computer=random.choice(choices)

#user chance

user =int(inpuxt("Enter your choice 1,2 or 3: "))

#user"s choice

if (user==1):
    print("You chose : Rock")
elif (user==2):
    print("You chose : Paper")
elif (user==3):
    print("you chose : Scissor")  
else:
    print("Wrong Input")          

#comps choice

if (computer==1):
    print("computer chose : Rock")
elif (computer==2):
    print("computer chose : Paper")
elif (computer==3):
    print("computer chose : Scissor")

# Fight

# if(computer == user):
#     print("It's a Draw")

# elif(computer==1 and user==2):#-1
#     print("You Win")

# elif(computer==2 and user==3):  #-1  
#     print("You Win")

# elif(computer==3 and user==1):#2
#     print("You win")

# elif(computer==1 and user==3):#-2
#     print("You Lose")

# elif(computer==2 and user==1):#1
#     print("You Lose")
        

# elif(computer==3 and user==2):  #1  
#     print("You Lose") 

    #or you can use this instead of big else loop

if(computer == user):
    print("It's a Draw")  

elif((computer-user==2) or (computer-user==-1)):
    print("You win")

else :
    print("you lose")    