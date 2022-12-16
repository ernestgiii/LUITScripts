#!/usr/bin/env python3.7

# Our EC2 Random Name Generator 

# Our resouces
#https://docs.python.org/3/library/random.html
#https://www.educative.io/answers/how-to-generate-a-random-string-in-python

import random 
import string 

# Random Name Generator Function 

def random_generatorID(size=14, string=string.ascii_letters + string.digits):
    return ''.join(random.choice(string) for _ in range(size))
    
department = input("Welcome! Are you a member of Accounting, FinOps, or Marketing? Please enter your department: ").upper()

for _ in department:
    if department == "Accounting" or department.lower() == "accounting":
        print("Standby while we check our system...")
        break 
    
    elif department == "FinOps" or department.lower() == "finops":
        print("Standby while we check our system...")
        break
    
    elif department == "Marketing" or department.lower() == "marketing":
        print ("Standby while we check our system...")
        break
    
    else: 
        print("🛑 🛑 Sorry: The deparment you entered is incorrect please try again!")
        exit()
number = int(input("Type in the number of EC2 Instances: "))

if number < 0:
    print("Enter in a number: ")
elif number > 0:
    print("Congrats!! You get your new instances")
    
    # Let's print our results
    print("\n...Standby...\n")
    print("Let's get your new EC2 Instance Names!")
    
    for _ in range(1, number +1):
        EC2_name = department
        EGen_ID_Name = EC2_name + "_" + random_generatorID()
        print("You are now being given your unique EC2 Instance Name: ", EGen_ID_Name)
        
        print("Thank you! Please use the EGen random name generator again 😎 ")

        
    
        