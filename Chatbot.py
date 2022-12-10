# We're creating a basic chatbot 

import time 


name = input ("Hello! I am EGen, Ernest's new chatbot. What is your name: ")

time.sleep(2)

print("Hello" ' '+  name)

time.sleep(2)

like = input("Would you like to play a game?")

time.sleep(2)
if "yes" in like:
    print("Ok! What is your favorite comic company Marvel or Breezy Comics 🦸🏾?")
else:
    print("Sorry! We'll play another time")
    exit()
time.sleep(2)
results = input("Please Enter your favorite comic company?: ")
if "Marvel" in results:
    print("I hear Namor is one of your favorite characters, do you like the X-Men too?")
if "Breezy Comics" in results:
    print("Black Thunder is the greatest! ⚡")
time.sleep(2)

print("I hope you enjoyed your experience with the EGen chatbot. I hope you have a good day!")

    
    
    
