# comparators
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = True

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = True

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = True

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = False

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = False

# (20 - 10) > 15
#bool_one = False

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
#bool_two = False

# 1**2 <= -1
#bool_three = False

# 40 * 4 >= -4
#bool_four = True

# 100 != 10**2
#bool_five = False

# Boolean expressions
# Make me true!
#bool_one = 3 < 5

# Make me false!
#bool_two = 99 == "lettuce"

# Make me true!
#bool_three = 44 / 2 <= 43

# Make me false!
#bool_four = "potato" != "potato"

# Make me true!
#bool_five = "tomato" == "tomato"

# And
#bool_one =  False and False

#bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

#bool_three = 19 % 4 != 300 / 10 / 10 and False

#bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

#bool_five = True and True

# Or
#bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

#bool_two = True or False

#bool_three = 100 ** 0.5 >= 50 or False

#bool_four = True or True

#bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1

# Not
#bool_one = not True

#bool_two = not 3 ** 4 < 4 ** 3

#bool_three = not 10 % 3 <= 10 % 2

#bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

#bool_five = not not False

# This and That
#bool_one = False or not True and True

#bool_two = False and not True or True

#bool_three = True and not (False or False)

#bool_four = not not True or False and not True

#bool_five = False or not (True and True)

# Mix 'n' Match
# Make me false!
#bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
#bool_two = not 4 ** 6 < 6 ** 4

# Make me false!
#bool_three = False and True or False

# Make me true!
#bool_four = True and not (False and False)

# Make me true!
#bool_five = 20 * 2 >= 4

# Conditional Statement Syntax
if 8 < 9:
    print("Eight is less than nine!")

response = "Y"
answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# If Statements
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print(using_control_once())
print(using_control_again())

# Else
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:
        return False    # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:
        return False     # Make sure this returns False

# Elif
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# Complete the if and elif statements
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 65:
        return "D"
    else:
        return "F"


# This should print an "A"
print(grade_converter(92))

# This should print a "C"
print(grade_converter(70))

# This should print an "F"
print(grade_converter(61))

