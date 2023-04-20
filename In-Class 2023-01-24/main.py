#main.py

#Generate a random integer
#Decide if it's even or odd
#Print even or odd
''' #comments out the code so I can continue working at the bottom
import random
alpha = random.randint(100, 200) #A random integer between 100 and 200, inclusive
print("alpha =", alpha)
if alpha % 2 == 0: #Integer remainder of alpha/2 (% is mod)
    print("even")
else:
    print("odd")
    
#Read an integer from the keyboard
#Print a friendly message telling if it's even or odd
data = input("Enter your favorite integer ")
num = int(data)
if (num % 2 == 0):
    print("Your number is even")
else:
    print("Your number is odd")
    
#while loop
# Divide by 2 until we get to zero
tmp = 100
while(True): #Infinite loop. Run forever because the condition never goes false.
    tmp = int(tmp / 2)
    print(tmp)
    if (tmp == 0):
        break #Takes us out of the loop immediately 
    
    #Rule: Use integers unless you have a good reason not to.
    # 2 Reasons: Faster, floating point numbers have a precision problem.

#for loop
# Default start is zero
for i in range(10,25,2):    # I want ints from 10 to 25 but just the even numbers
    print(i)
    
#Start an infinite loop
#    Read int from the kbd
#    it it's negative exit the loop
#    else add it to the running total
#After the loop print the running total 
total = 0
while True:
    alpha = int(input())
    if alpha < 0:
        break
    else:
        total += alpha #total = total + alpha
print(total)
'''

#print even integers from 100 to 1 in descending order
for i in range(100,1,-2):
    print(i)