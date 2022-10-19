#In Funcitons file there are two funcitons and we r going to inport them here and use them

from functions import power

print("Now am gonna see if it works or not")

num = int(input("Enter any Number: "))
its_power = int(input("Enter it's power: "))

calculation = power(num, its_power)
print(calculation)