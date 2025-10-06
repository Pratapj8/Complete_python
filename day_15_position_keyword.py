# python day_15_position_keyword.py

# postional argument


def hello(name, age):
    print("Hello " + name + " your age is " + str(age) + " years old.")


hello("Pratap", 28)


# keyword argument
def hello(name, age=25):
    print("Hii " + name + " your age is " + str(age) + " years old.")


hello("Pratap")


# keyword argument overwrite
def hello(name, age=25):
    print("Hii " + name + " your age is " + str(age) + " years old.")


hello("Pratap", 5)


# *args == Postional arguments
# **kwarg == Keyword arguments


def hello(*args, **kwargs):
    print(args)
    print(kwargs)


hello(
    "Pratap", "Jadhav", age=28, bob=1995
)  # args == "Pratap" & "Jadhav" , kwargs == age=28 ,bob=1995

# convert tuple into list
lst = list(("Pratap", "Jadhav"))
dict_val = {"age": 28, "bob": 1995}

hello(lst, dict_val)  # it will treat as postional arguments
hello(*lst, **dict_val)  # It will treat *args and **kwargs


# Summing numbers and printing additional info


def process_data(*args, **kwargs):
    # args are positional arguments
    total = sum(args)
    print("Positional arguments (numbers to sum):", args)
    print("Sum of numbers:", total)

    # kwargs are keyword arguments
    for key, value in kwargs.items():
        print(f"{key} : {value}")


# Using both *args and **kwargs
process_data(10, 20, 30, name="Alice", city="Wonderland", age=25)

# Using a list and dictionary
numbers = [5, 15, 25]
info = {"name": "Bob", "city": "Builderland", "age": 30}

# Correct way to pass them as *args and **kwargs
process_data(*numbers, **info)
