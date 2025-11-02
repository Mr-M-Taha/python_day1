# from random import choice


def temp_converter():
    print("""Temprature converter\n Convert from:
        1. Celsius → Fahrenheit
        2. Fahrenheit → Celsius
        3. Celsius → Kelvin
        4. Kelvin → Celsius
        5. Fahrenheit → Kelvin
        6. Kelvin → Fahrenheit""")
    choice = input("choose an option: ")
    try:
        input_temp = int(input("enter the temp value: "))
    except:
        pass

    match choice:
        case "1":
            print(f"result: {cel_to_fah(input_temp)}")
        case "2":
            print(f"result: {fah_to_cel(input_temp)}")
        case "3":
            print(f"result: {cel_to_kel(input_temp)}")
        case "4":
            print(f"result: {kel_to_cel(input_temp)}")
        case "5":
            print(f"result: {fah_to_kel(input_temp)}")
        case "6":
            print(f"result: {kel_to_fah(input_temp)}")


###functions
def cel_to_fah(temp):
    return (temp * 9 / 5) + 32


def fah_to_cel(temp):
    return (temp - 32) * 5 / 9


def cel_to_kel(temp):
    return temp + 273


def kel_to_cel(temp):
    return temp - 273


def fah_to_kel(temp):
    return ((temp - 32) * 5 / 9) + 273


def kel_to_fah(temp):
    return ((temp - 273) * 9 / 5) + 32


temp_converter()
