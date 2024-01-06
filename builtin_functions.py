def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try: 
        user_input_num = int(days_and_unit_dictionary["days"])
        # converstion only for positive integers
        if user_input_num > 0:
            calculated_value = days_to_units(user_input_num, days_and_unit_dictionary["unit"])
            print(calculated_value)
        """elif user_input_num == 0:
            print("entered 0, enter positiv number")
        else:
            print("entered negativ number")"""
    except:
        print("incorrect input")



user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter number of days and conversion unit!\n")
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()