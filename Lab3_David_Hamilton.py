"""
David Hamilton
09/13/2024
This program's purpose is to find the users Federal Income Tax Bracket
based on earned income and marital status
"""

#get earned_income from user
earned_income = int(input("Enter the amount of income you "
							"earned in 2023: "))
#get marital_status from user
marital_status = str(input("Are you married or single? \n"
					"Type m for married and s for single: "))
						




#take if marital status = married
if marital_status == "m":
	if earned_income <= 22000:
		first_tax = earned_income * .1
		print("This year you owe", f'{first_tax:.2f}', "in taxes")
	elif earned_income <= 89450:
		second_tax = 22000 * .1 + (earned_income - 22000) * .12
		print("This year you owe", f'{second_tax:.2f}', "in taxes")
	elif earned_income <= 190750:
		third_tax = (22000 * .1) + ((89450 - 22000) * .12) + (earned_income - 89450) * .22
		print("This year you owe", f'{third_tax:.2f}', "in taxes")
	else:
		print("You made too much for this calculator. Hurray!")
	
#take if marital status = single
elif marital_status == "s":
	if earned_income <= 11000:
		first_tax = earned_income * .1
		print("This year you owe", f'{first_tax:.2f}', "in taxes")
	elif earned_income <= 44725:
		second_tax = 11000 * .1 + (earned_income - 11000) * .12
		print("This year you owe", f'{second_tax:.2f}', "in taxes")
	elif earned_income <= 95375:
		third_tax = (11000 * .1) + ((44725 - 11000) * .12) + (earned_income - 44725) * .22
		print("This year you owe", f'{third_tax:.2f}', "in taxes")
	else:
		print("You made too much for this calculator. Hurray!")

#user didn't enter married or single
else:
	print("Marital Status Error")
