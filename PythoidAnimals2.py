"""
David Hamilton
9/6/24
The purpose of the code is to calculate human age
translated to dog, cat, and horse ages on Planet Pythoid
"""


"""
Background on Pythoid
1 year = 360 days
1 month = 30 days
"""

#get input of human age
#used for all animals on Pythoid
user_age = float(input("Enter Your Age: "))

#animals
animals = ["dog", "cat", "horse"]

#animal formulas
dog_formula = 7 * user_age
cat_formula = 1/9 * user_age
horse_formula = 3 * (((user_age ** 2 - 47) / 7) + 12)

#make list for formulas
animal_formulas = [dog_formula, cat_formula, horse_formula]

x = 0

#for loop to run through all animals
for animal in animal_formulas:
	days = animal_formulas[x] * 360
	#print(days)
	
	#gives years
	years = days // 360
	#print(years)
	years_remainder = days % 360
	#print(years_remainder)
	
	#give months
	months = years_remainder // 30
	#print(months)
	months_remainder = years_remainder % 30
	#print(months_remainder)
	
	#gives whole days left
	days = months_remainder // 1
	#print(days)
	
	print("Your age in", animals[x], "years is",  years, "years",
	months, "months",  days, "days")
	
	#sends next value in animal_formulas through for loop
	x = x + 1

quit() 

