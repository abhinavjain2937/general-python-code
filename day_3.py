# num = int(input("Enter a number : "))

# if num %2 == 0 :
#     print(f"{num} is an even number")
#     age = int(input("Enter your age : "))
#     if age >= 18 :
#         print("You have to psy $ 40 ")
#     else:
#         print("you have to pay $13")

#     want_photo = input("Do you want a photo? (yes/no): ").strip().lower()
#     if want_photo=='yes':
#         print("Photo taken! charge $5")
    

    
# else:
#     print(f"{num} is an odd number")


# # we have to create an advanced bmi calculator

# # BMI Calculator 2.0
# print("Welcome to BMI converter")

# weight = float(input('Enter the wight in kg :'))
# hight = float(input("Enter the hight in cm :"))
# BMI = weight /(hight/100)**2


# if BMI < 18.5:
#     print(f"Your BMI is : {BMI:.2f} You are underweight")
# elif 18.5 <= BMI <=25 :
#     print (f"Your BMI is : {BMI:.2f} you have a normal weight")
# elif 25 < BMI <35:
#     print(f"Your BMI is : {BMI:.2f} you are obese")
# else:
#     print(f"Your BMI is : {BMI:.2f} You are clinically obouse")


# print("________Welcome to python pi€a delivery service_________")
# print("small pizza : $15")
# print("Medium pizza : $20")
# print("Large pizza : $25")
# print("\n\nPepperoni for small pizza : $2")
# print("Pepperoni for Medium and Large pizza : $2")
# print("\nExtra chease for any size pizza : $1")

# print("____________________________________________")

# size = input("What is the size of pizza you want ? (s/m/l) : ")
# add_pepperoni = input("do you want pepperoni ? (yes/no) : ").strip().lower()
# extra_cheese = input("do you want extra cheese ? (yes/no) : ").strip().lower()

# bill = 0 

# if size == 's':
#     bill += 15
#     if add_pepperoni == 'yes':
#         bill+=2
#     if extra_cheese =='yes':
#         bill +=1
#     else:
#         bill+=0
#     print(f"Your total bill is : ${bill}")

# elif size == 'm':
#     bill += 20
#     if add_pepperoni == 'yes':
#         bill += 3
#     if extra_cheese == 'yes':
#         bill += 1
#     else :
#         bill +=0
#     print(f"Your total bill is : ${bill}")
# elif size == 'l':
#     bill += 25
#     if add_pepperoni == 'yes':
#         bill+=3
#     if extra_cheese =='yes':
#         bill +=1
#     else:
#         bill+=0
#     print(f"Your total bill is : ${bill}")
# else:
#     print(" Invalid size selected . \nPlease select from the given inputs")

print("Welcome to the LOVE Calculator ")
name_1 = input("Enter your name :\n ").lower()
name_2 = input("Enter your partners name :\n").lower()

combined_string = name_1 + name_2
lowercase_string = combined_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")
true = t + r + u + e


l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")
love = l + o + v + e

love_score  = str(true) + str(love)
love_score = int(love_score)
if (love_score<10) or (love_score>90) :
   print(f"Your love score is {love_score} .you go together like cock and mentos")
elif (love_score >=40) or (love_score<=50):
   print(f"Your love score is {love_score} .you are allright together ")
else:
   print(f" Your love score is {love_score}")

print(love_score)