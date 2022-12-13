name = "Ibrahim Diriye"
age_in_years = 19
height_in_cm = 190

print("hello, could you please give me your name?")
inputted_name = input()

print("Alright! Up next, your age in years")
inputted_age = int(input())

print("And finally, your height in centimetres, no decimals!")
inputted_height_in_cm = int(input())

print("Ok, sit tight while we do some math....")

if name == inputted_name:
    print("Alright, your name checks out.")
else:
    print("fake name")
    exit()

if age_in_years == inputted_age:
    print("Age test passed too....")
else:
    print("Why u always lying?")
    exit()

if height_in_cm == inputted_height_in_cm:
    print("Your as tall as you look!")
else:
    print("Short kings rule as well.")
    exit()


