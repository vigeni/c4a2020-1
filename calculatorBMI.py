def prompt():
    height = input("Please enter your height in meters: \n")
    weight = input("Please enter your weight in kg: \n")
    print (height)
    bmi = float(weight) / float(height)**2
    printStatus(bmi)

def printStatus(bmi):
    if bmi < 18.5:
        return print("Your weight status is underweight.")
    if bmi < 25.0:
        return print("Your weight status is normal.")
    if bmi < 30:
        return print("Your weight is overweight.")
    return print("Your weight is obese")

prompt()
