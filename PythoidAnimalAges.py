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
#used for all three animals
user_age = float(input("Enter Your Age: "))


# dog section

# 1 human year = 7 dog years
dog_translate_years = 7

#translate user_age into dog_days
dog_days = user_age * dog_translate_years * 360

#gives whole years for dog age
dog_years = dog_days // 360
dog_years_remainder = dog_days % 360

#gives whole months for dog age
dog_months = dog_years_remainder // 30
dog_months_remainder = dog_years_remainder % 30

#gives whole days for dog age
dog_days = dog_months_remainder // 1

#print out age in dog years
print("Your age in dog years is ", dog_years, "years", dog_months, "months", dog_days, "days")


# cat section

# 1 human year = 1/9 cat years 
cat_translate_years = 1/9

#translate user_age into cat_days
cat_days = user_age * cat_translate_years * 360

#gives whole years for cat age
cat_years = cat_days // 360
cat_years_remainder = cat_days % 360

#gives whole months for cat age
cat_months = cat_years_remainder // 30
cat_months_remainder = cat_years_remainder % 30

#gives whole days for cat age
cat_days = cat_months_remainder // 1

#print out age in cat years
print("Your age in cat years is ", cat_years, "years", cat_months, "months", cat_days, "days")


# horse section

# 1 human year = 3 * ((user_age) ** 2 - 47) / 7 + 12

#translate user_age into horse_days
horse_days = 3 * (((user_age ** 2 - 47) / 7) + 12) * 360

#gives whole years for horse age
horse_years = horse_days // 360
horse_years_remainder = horse_days % 360

#gives whole months for horse age
horse_months = horse_years_remainder // 30
horse_months_remainder = horse_years_remainder % 30

#gives whole days for horse age
horse_days = horse_months_remainder // 1

#print out age in dog years
print("Your age in horse years is ", horse_years, "years", horse_months, "months", horse_days, "days")


