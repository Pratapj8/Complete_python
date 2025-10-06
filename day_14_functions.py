# Modulor coding
# python day_14_functions.py

## why functions?(Interview Question)
# 1. to make code more readable
# 2. to make code more efficient
# 3. to make code more maintainable
# 4. to make code more reusable
# 5. to make code more extensible


# function - to avoid repeatative tasks , do changes once and it will change all functions


def coding():
    print("Python is Very Easy")


coding()
coding()
coding()

"""print("Python is Easy")

print("Python is Easy")

print("Python is Easy")"""


# Return string


def jarvis():
    return "Greetings from Jarvis"


print(jarvis())

# Use variable
msg = jarvis()
print(msg)

# Use variable with comments
msg = jarvis()
print(msg + " Good morning")


# Add in multi line comments what this function does so that next person can understand


def welcome():
    """
    Description: This function will show a welcome message


    Return : This function will return the welcome message
    """

    return "Greeting Pratap"


msg = welcome()
print(msg + " Happy coding")


# it is returning string


def welcome() -> str:
    """
    Description: This function will show a welcome message


    Return : This function will return the welcome message
    """

    return "Greetings from Baba"


msg = welcome()
print(msg + " Practice coding")


# Parameterize
def welcome(msg) -> str:
    """
    Description: This function will show a welcome message

    Return : This function will return the welcome message
    """

    return msg  # parameterize (we gave right to user to define)


msg = welcome("Welcome all")
print(msg + " Easy coding")


## function to add even and odd number


def even_odd_sum(lst):
    """
    Description: This function will add even and odd number in a list
    Return : This function will return the sum of even and odd number in a list
    """

    even_sum = 0
    odd_sum = 0
    for i in lst:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    return even_sum, odd_sum


sum1, sum2 = even_odd_sum([1, 2, 3, 45, 6, 677, 7, 8, 8, 54, 4, 3, 5, 6])
print(sum1, sum2)


# function to sum all numbers in a list
def list_sum(lst):
    """
    Description: This function will return the sum of numbers in a list
    """
    return sum(lst)


total = list_sum([10, 20])
print(total)


# function to sum all numbers in a list manually
def list_sum_manual(lst):
    """
    Description: This function will return the sum of numbers in a list
    without using the built-in sum() function.
    """
    total = 0
    for num in lst:
        total += num
    return total


total = list_sum_manual([10, 10, 20])
print(total)
