def age_calc(year_of_birth):
    age = 2019 - year_of_birth
    if age < 18:
        print("you are a minor")
    elif age < 36:
        print("you are a youth")
    elif age >= 36:
        print("you are an elder")

value = int(input("please enter your year of birth "))
age_calc(value)        
