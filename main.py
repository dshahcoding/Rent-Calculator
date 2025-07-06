print("\n\nWelcome to the rent calculator project.....")

#to calculate the rent we need inputs from the user
"""
total rent
total food ordered for snacking
electricity units spend
charge per unit
number of persons living in room/flat
"""

rent = int(input("\nEnter your room/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food+rent+total_bill)/persons    #equation which provides the output

print("\nEach person will pay = ",output)
print("\n")