"""
Author:Viktoriia Denys
Program:camper_age_input_py
The program will have will prompt for the age of one infant (age 1-5 years) who is attending camp
and convert the age in months to years via a function call then print the result.

"""


import constants


def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your child`s age: ")
    age_in_months = convert_to_months(int(age_in_years))

    print("{} years is {} months".format(age_in_years,age_in_months))


"""
used convert method ,imported MONTHS from constant
"""
