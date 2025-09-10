# Problem:
#Ask the user for withdrawal amount.
#If balance is enough → allow withdrawal.
#Else → show "Insufficient funds".
# Helps practice: if-else, user input.
balance=1000
withdrawlamount=int(input("enter the amount: "))
newbalance=balance-withdrawlamount 
if withdrawlamount<=balance:

   print(f"withdrawal successful",{newbalance})

else:
   print("Insufficient balance")

#Ask user for Principal, Rate, and Time.
#Formula = (P × R × T) / 100.
#Calculate and show Interest.
# Helps practice: input, formula, output.
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of interest: "))
time = float(input("Enter the Time (in years): "))

# Calculate Simple Interest
interest = (principal * rate * time) / 100

# Show the Interest
print(f"The Simple Interest is: {interest}")

#Traffic signal 

def traffic(signal):
    signal=input("enter")
    print(signal)
    if signal=="red":
        sign="stop"
        print(sign)
    elif signal=="green":
        sign="get ready"
        print(sign)
    elif signal=="yellow":
        sign="go"
        print(sign)

traffic("red")

# Temperature Advisor
#Input temperature value.
#● 40°C → "Very Hot"

#● 30–40°C → "Normal Hot"
#● 20–30°C → "Pleasant"
#● < 20°C → "Cold"

#Helps practice: multiple elifs and ranges.

def temp_advisor(degrees):
    degrees=float(input("enter tht temerature"))
    if degrees >= 40:
        print("very hot")
    elif 30<=degrees <40:
        print("normal")
    elif 20<=degrees <=30:
        print("pleasant")
    elif degrees<=20:
        print("cold")

temp_advisor(40)
    
#6. Movie Ticket Booking System
#Goal: Show ticket price based on age.
# Flow Idea:
#● If age < 12 → ₹150
#● Else if age < 60 → ₹250
#● Else → ₹200

# Practice elif + variables

def ticket_booking_system(age):
    
    if age <=12:
       print(f"Child ticket price: ₹150")
       return 150
    elif age <= 60:
        ticket_price=250
        return(ticket_price)
    else:
        print("ticket price is 200")
ticket_booking_system(8)

#4. Friend Group Message Sender
#Goal: Send same message to 5 friends.
# Flow Idea:
#● For each friend in list
#● Send "Hey, what’s up?"

## Practice for loop over list
friends = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
for i in friends:
    print(f"message Sending to {i}: Hey, what's up?")# whenever creating a sudden list or dict format f should be used in case of preassign not hapen     
    
#3. Fast Food Order Chooser
#Goal: Suggest food based on money in pocket.
# Flow Idea:
#● If money > ₹200 → Pizza
#● Else if money > ₹100 → Burger
#3● Else → Maggi

# Practice elif chain

def fast_food_order(money):
    money=float(input("enter ")) ## whenever string assigning a int float should be used
    if money >= 200 :
        print("u can buy pizza")
    elif money >= 100:
        print("u can buy burger")
    else:
        print("only maggie u can buy")
fast_food_order(232)

#2. Exam Hall Entry Check
#Goal: Allow student inside if Hall Ticket shown.
# Flow Idea:
#● Ask: "Do you have hall ticket?"
#● If YES → Allow
#● Else → Stop

def exam_hall_entry():
    response = input(" Do you have hall ticket? (yes/no): ").lower().strip()
    
    if response in ['yes', 'y', 'true', '1']:
        print("ALLOWED - You can enter the exam hall!")
        return True
    else:
        print(" STOP - You cannot enter without hall ticket!")
        return False

exam_hall_entry()

 #   Ask for total bill and number of friends.
#Calculate amount each friend should pay.
# Helps practice: division, clean printing.

frnds_num=int(5)
totall_bill=3800
sharing=totall_bill//frnds_num
print(sharing)
### train seats
available_seats=list(range(1,100))
seat_num=int(input(" u r num"))
if seat_num < 1 or seat_num >100:
   print("not available")
elif seat_num in available_seats:
    available_seats.remove(seat_num)
    print(f"Seat {seat_num} booked successfully.")
else:
    print(f"Seat {seat_num} is already booked.")
## check username
usernames=["siva","ram","raghu"]
ask=input("enter user name")
if ask in usernames:
   print("name taken , try another")
else:
   print("name available")
   

## prime num
num = int(input("enter num"))
if num //num ==0  and num//1 == 0:
   print(num)
else:
   print("not prime num ",num)
   
### 
secret_number = 7

while True:
    guess = int(input("Guess the secret number: "))
    
    if guess == secret_number:
        print("Congrats! You guessed it right 🎉")
        break
    else:
        print("Wrong guess, try again!")

















        
