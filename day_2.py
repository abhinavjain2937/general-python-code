
# # nwe project : a tip calculator and bill display
# print("****************************************")
# print("Welcomw to our indica fight restaurent")
# print("****************************************")

# bill = float(input("what was the total bill ? ₹"))
# tip = int(input("how much tip % would you like to give ? (eg. 10 ,20 ,30)"))
# people = int(input("no of people to split the bill : "))

# bill_with_tip = ((tip/100)*bill)+bill
# print(f"the total amount of bill is : {bill_with_tip}")
# bill_per_person = bill_with_tip/people
# print(f"The bill per person will be : {bill_per_person}")

# print("12344"+"5678")
# print(123+456)

# num = input("Enter a number: ")

# # Ensure the input is a valid two-digit number
# if num.isdigit() and 9 < int(num) < 100:
#     num_1 = int(num[0])
#     num_2 = int(num[1])
#     result = num_1 + num_2
#     print(f"The sum of the digits is: {result}")
# else:
#     print("The number is not a two-digit number.")

# # write a program fond body mass index
# # BMI Calculator
# print("Welcome to BMI converter")

# weight = float(input('Enter the wight in kg :'))
# hight = float(input("Enter the hight in cm :"))

# BMI = weight /(hight/100)**2
# print(f"Your BMI is : {BMI:.2f}")
# print(round(8/3,3))
# print(8//3)


# Write a program to calculate the number of days, weeks, and months in a given number of days.
print("Welcome to the days, weeks, and months calculator")

age = int(input("Enyer your current age in years:"))
days_used = age * 365
days_remaining = 365*90 - days_used
weeks_remaining = days_remaining // 7
month_remain = days_remaining // 30
year_remain = 90 - age

print(f"You have {days_remaining} days,{weeks_remaining} weeks,{month_remain} months and {year_remain} years of life renaiming")
print("it's time to think what we have to do now")
print("Thank you for using the calculator!")