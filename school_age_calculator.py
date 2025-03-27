def school_age_calculator(age,name):
    age = int(age)
    if age < 6:
        print(f"Enjoy your childhood, {name} is only {age} years old")

    elif age == 6:
        print("Welcome to school, {name}, is oly {age} years old")
    else:
        print("You are a big kid, {name},is only {age} years old")


school_age_calculator(7, "John")