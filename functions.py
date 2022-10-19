#The functions for square

def square(x):
    return x*x
def power(p, q):
     return p**q
   
    

num = int(input("Enter your number and I will give you it's square: "))

print (f"You have entered {num}, and it's square is {square(num)}")

print("Now do you want me to perform further calculation? ")
answer = input(": ")

if answer.upper() == "YES":
    print("Write a number")
    answer2 = int(input(": "))
    print("Now write it's power (how many times you want me to multiply...)")
    answer3 =int(input("Power: "))
    print(f"Your Answer: {power(answer2, answer3)}, Enjoy!")
    
elif answer.upper() == "NO":
    print("Ending it now")
    
else:
    print("r u dumb?")
    