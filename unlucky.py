import random

print("Generating")
number = random.randint(1,20)

if number == 4 or number==13:

    print(f"{number} Unlucky")
elif number%2!=0:
     print(f"{number} ODD")
else:
    print(f"{number} Even")