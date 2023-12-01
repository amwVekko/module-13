calc_to_unit = 24               
name_of_unit = "hours"



def days_to_units(num_of_days):        
    return f"{num_of_days} days are {num_of_days * calc_to_unit} {name_of_unit}"

user_input = input("input number of days:\n")
print(days_to_units(int(user_input)))