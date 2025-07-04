# # uSE OF RANDOME module
import random


# random_integer = random.randint(1, 18)
# print(random_integer)
# #0.00000000000 to 0.999999999999999
# random_float = random.random()
# print(random_float*5)




 
# random.seed(1)
 
# # Get the state of the generator
# state = random.getstate()
 
# print('Generating a random sequence of 3 integers...')
# for i in range(3):
#     print(random.randint(1, 1000))
 
# # Restore the state to a point before the sequence was generated
# random.setstate(state)
# print('Generating the same identical sequence of 3 integers...')
# for i in range(3):
#     print(random.randint(1, 1000))


 
# print('Random number from 0 to 1 :', random.random())
# print('Uniform Distribution between [1,5] :', random.uniform(1, 5))
# print('Gaussian Distribution with mean = 0 and standard deviation = 1 :', random.gauss(0, 1))
# print('Exponential Distribution with lambda = 0.1 :', random.expovariate(0.1))
# print('Normal Distribution with mean = 1 and standard deviation = 2:', random.normalvariate(1, 5))

# # making a working dice simulator
# print("Welcome to the dice simulator!")
# print("Rolling the dice...")
# print("aao chalo khalein ludo with lodu(friends)")
# rand_num = random.randint(1,6)

# if rand_num==1:
#     print("You rolled a 1! \n  _______ \n |       |\n |   0   |\n |       |\n |_______|")
# elif rand_num==2:
#     print("You rolled a 2! \n  _______ \n |0      |\n |   0   |\n |       |\n |_______|")
# elif rand_num==3:
#     print("You rolled a 3! \n  _______ \n |0      |\n |   0   |\n |      0|\n |_______|")
# elif rand_num==4:
#     print("You rolled a 4! \n  _______ \n |0     0|\n |       |\n |0     0|\n |_______|")
# elif rand_num==5:
#     print("You rolled a 5! \n  _______ \n |0     0|\n |   0   |\n |0     0|\n |_______|")
# else:
#     print("You rolled a 6! \n  _______ \n |0     0|\n |0     0|\n |0     0|\n |_______|")
# print("Thank you for using the dice simulator!")


# # list concepts
# # who will pay selection system

# name_strings = input("Give me everybody's name seprated by a coma :") 
# names = name_strings.split(", ")

# print(names)
# num_itens = len(names)

# randome_choose = random.randint(0,num_itens-1)
# person_who_will_pay = names[randome_choose]

# print(f"{person_who_will_pay} is  going to buy food for all of us")

# rock paper scissors game
# print("Welcome to rock paper scissors game !")

# user_choice = input("Enter tour choice (rock ,paper ,scissor): ").lower()
# choice = ["rock","paper","scissor"]
# computer_choice = random.choice(choice)
# print(f"Computer chose: {computer_choice}")

# if user_choice == computer_choice :
#     print("It's a tie!")
# elif user_choice == "rock" and computer_choice == "scissor":
#     print("You win! Rock beats Scissor.")
# elif user_choice == "paper" and computer_choice == "rock":
#     print("You win! Paper beats Rock.")
# elif user_choice == "scissor" and computer_choice == "paper":
#     print("You win! Scissor beats Paper.")  
# else:
#     print("You lose! Better luck next time.")

# fruits = ["apple", "banana","kiwi", "mango", "grape", "orange", "kiwi", "pineapple", "papaya", "pomegranate", "strawberry"]

# print(fruits.append("watermelon"))
# print(fruits,"\n\n")

# fruits.insert(3,"peach")
# print(fruits,"\n\n")

# fruits.remove("grape")
# print(fruits,"\n\n")

# print(fruits.pop(1))
# print(fruits,"\n\n")

# print(fruits.index("kiwi",0,4))
# print(fruits,"\n\n")

# print(fruits.count("kiwi"))
# print(fruits,"\n\n")

# fruits.sort(key=len,reverse=False)
# print(fruits,"\n\n")

# fruits.reverse()
# print(fruits,"\n\n")

# fruits.copy()
# print(fruits,"\n\n")


# let us crate a stact from a list
stack = input("Enter the number of elements in the stack: ").split(",")
stack = [item.strip()for item in stack]  # Remove any leading/trailing spaces
# meaning of stack is last in frist out
print("The stack is created with the following elements:")
print(stack) 


stack.append(input("Enter the element to be pushed onto the stack: ").strip())
print(f"The stack after pushing the element:\n{stack}")

n = len(stack)
pop_element = input("enter the element to be poped out :").strip()
found = False
# print(f"The element that was poped out is : {stack.pop(n-1)}")
for i in range (n-1, -1, -1):
    
    if pop_element == stack[i]:
        print(f"The element that was poped out is : {stack.pop(i)}")
        found = True
        break
if not found:
    print("Element not found in the stack. No element was popped out.")
print(stack)

