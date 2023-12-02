calc_to_unit = 24               
name_of_unit = "hours"



def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calc_to_unit} {name_of_unit}"




def validate_and_execute():
    try: 
        user_input_num = int(user_input)
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num)
            print(calculated_value)
        elif user_input_num == 0:
            print("entered 0, enter positiv number")
        else:
            print("entered negativ number")

    except:
        print("incorrect input")



user_input = ""
while user_input != "exit":
    user_input = input("input number of days:\n")
    validate_and_execute()