calc_to_unit = 24               # global vars
name_of_unit = "hours"



def days_to_units(days, custom_msg):        # local vars
    print(f"{days} days are {days*calc_to_unit} {name_of_unit}")
    print(custom_msg)


def scope_check(days):
    my_var = "var inside function"
    print(name_of_unit)
    print(days)
    print(my_var)

days_to_units(35, "gg ez")
scope_check(20)