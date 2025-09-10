#Dream City Selector
#Goal: Recommend City based on climate choice.
# Flow Idea:
#● If choice = "cold" → Manali
#● If choice = "hot" → Goa
#● If choice = "rainy" → Kerala
#● Else → Delhi
# Practice input + if-else

def dreamcity(dream):
    city=dream
    dream=input("enter city: ")
    if city=="cold":
        print("recomended city manali",city)
    elif city=="hot":
        print("recomended city goa",city)
    elif city=="rainy":
        print("recomended city kerala",city)
    else:
        print("recomended city delhi")
dreamcity("hot")
dreamcity("cold")

choice = input("Enter climate (cold/hot/rainy): ").strip().lower()

if choice == "cold":
    print("Recommended city: Manali")
elif choice == "hot":
    print("Recommended city: Goa")
elif choice == "rainy":
    print("Recommended city: Kerala")
else:
    print("Recommended city: Delhi")
# Marksheet Creator
#Goal: Calculate grade based on marks.
# Flow Idea:
#● Marks > 90 → A
#● Marks > 75 → B
#● Marks > 60 → C
#● Else → Fail

# Practice multiple elif
def grade_calculator(marks):
    if marks>=90:
        grade="A"
        print("grade",grade)
    elif marks >= 75:
         grade="B"
    elif marks >= 60 :
         grade="B"
    else:
        print("fail")
#print(marks.grade_calculator()) oops method.object calling
grade_calculator(92)

## Odd/Even Number Checker
##Goal: Ask number → tell Odd or Even.
## Flow Idea:
##● Take number input    
##● If number%2==0 → Even
##● Else → Odd

## Practice modulus operator %

def num_check(value):
    value=int(input("enter"))
    num=value
    if num%2==0:
        print("even",num)
    else:
        print("odd",num)
num_check(9)
        
def num_check(num):
    if num%2==0:
        print("even",num)
    else:
        print("odd",num)
num_check(9)

## Crush Reply Waiter
#Goal: Keep checking phone until crush replies.
# Flow Idea:
#● While reply not received
#● Check phone every 5 mins
#● When reply comes → Celebrate!
# Practice while loop

import time

reply_received = False  # Initially no reply

while not reply_received:
    print(" Checking phone for crush's reply...")
    time.sleep(5)  # Simulates waiting 5 seconds (instead of 5 minutes)
    
    reply = input("Did the crush reply? (yes/no): ").strip().lower()
    if reply == "yes":
        reply_received = True

print(" Yay! Crush replied! Time to celebrate!")

  
reply = ""

while reply != "yes":
    reply = input("Did the crush reply? (yes/no): ").strip().lower()

print(" Yay! Crush replied! Time to celebrate!")

# Password Strong Checker
#Goal: Check if password has >8 letters and number.
# Flow Idea:
#● If password length >8 and has digit → strong
#● Else → weak


password = input("Enter your password: ")

if len(password) > 8 and any(ch.isdigit() for ch in password):
    print(" Strong password")
else:
    print(" Weak password")



import time

current_hour = 9  # starting at 9 AM

while current_hour < 21:  # until 9 PM
    print(" Drink water!")
    time.sleep(30 * 60)  # wait 30 minutes
    current_hour += 0.5  # add half an hour

print(" Water reminder stopped.")





















