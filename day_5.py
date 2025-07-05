# # pasword generator for a new user
# import random
# symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
# number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# print("Welcome to the password generator!")
# num_lettre = int(input("How many letters would you like in your password?\n"))
# num_symbols = int(input("How many symbols would you like in your password?\n"))
# num_numbers =  int(input("How many Numbers would you like in your password?\n"))
# # eASY LEAVEL 
# easy_password = ""

# for char in range(1, num_lettre + 1):
#     easy_password += random.choice(letters)
# for char in range (1,num_symbols + 1):
#     easy_password = easy_password+ random.choice(symbols)
# for char in range(1,num_numbers +1):
#     easy_password+= random.choice(number)

# print(easy_password)


# # hard level password generator
# password_list = []

# for char in range(1, num_lettre + 1):
#     password_list.append(random.choice(letters))
# for char in range (1,num_symbols + 1):
#     password_list.append(random.choice(symbols))
# for char in range(1,num_numbers +1):
#     password_list.append(random.choice(number))
# print(password_list)
# random.shuffle(password_list)
# print(password_list)

# password = ""

# for char in password_list:
#     password += char

# print(f"Your password is ; {password}")

# for i in range(1,11):
#     # print(f" {i} I am sorry . i dont do it again")
#     #writing a table with for loop
#     for j in range(1,11):
#         print(f"{i} * {j} = {i*j}")
#         print("\n\n")

# # CALCULATION OF AVARAGE HIGHT WITHJOUT USING FUNCTION (len(),sum())
# hight_list = input("Enter your hight in cm: ").split()
# print(hight_list) 

# hight_sum = 0
# no_of_candidates = 0

# for x in hight_list:
#     hight_sum = hight_sum+ int(x)
# print(f"The total hight is : {hight_sum} cm")


# for y in hight_list:
#     no_of_candidates+=1
# print(f"Number of candidates to masure hight : {no_of_candidates}")

# avg_hight = hight_sum/no_of_candidates

# print(f"Avarage hight of given candidates is : {avg_hight:.2f} cm .")


# # finding hihest score from list without [max()]
# scores = input("Enter the markes of all the students one by one \n").split()
# print(scores)

# higest_score = 0
# for x in scores:
#     if int(x)>higest_score:
#         higest_score = int(x)
#     else:
#         higest_score = higest_score

# print(f" the higest score in the class is : {higest_score}")

# #find the sum of all the even number including 1 and 100 in the range of 1 to 100

# number = 0

# for num in range (1,101):
#     if num % 2 == 0 :
#         print (num)
#         number+= num
#     if num == 1:
#         print(num)
#         number+=num
# print(f"The sun of the numbers between 1 to 100 incliudin 1 and 100 is : {number}")


# # a fizbuzz # for num in range(1, 101):
# for num in range (1,101):
#     if num % 3 == 0 and num % 5 ==0:
#         print("fizzbuzz")
#     elif num %5 == 0 :
#         print("buzz")
#     elif num % 3 == 0:
#         print("fizz")
#     else:
#         print(num)

# print(num)
def welcome():
    print("Welcome to the treasure island.")
    print("Welcome to the treasure island.")
    print("Welcome to the treasure island.")
    print("Welcome to the treasure island.")

welcome()