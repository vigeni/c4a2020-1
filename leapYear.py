def prompt():
    year=input("Enter year: \n")
    if int(year) < 1549:
        print("Year out of range.")
        prompt()
    if int(year) % 400 == 0 or (int(year) % 4 == 0 and int(year) % 100 != 0):
        return print(year + " is a leap year!")
    else:
        return print(year + " is not a leap year.")

prompt()