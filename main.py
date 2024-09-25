import math
def BMIcalculator(height:float, weight:float):
    bmi= weight/math.pow(height,2)
    print("Your bmi index is:%.2f"%(bmi))
    if bmi<18.5:
        print("You are underweight!")
    elif bmi<25:
        print("You are healthy :)")
    elif bmi<30:
        print("You are overweight!")
    else:
        print("You are obese")

if __name__ == '__main__':
    height = float(input("Enter height in cm:"))
    weight = float(input("Enter weight in kg:"))
    BMIcalculator(height/100,weight)