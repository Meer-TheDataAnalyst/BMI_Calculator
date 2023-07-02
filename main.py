#Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m2, resulting from mass in kilograms and height in metres.

#ask the user to enter his/her height in meter
height = input("enter your height in m: ")

# ask the user to inter his/her weight in kg.ab
weight = input("enter your weight in kg: ")

#convert the weight and the height into int/float data type, if you calculate without converting into int/float type you may end up with errors or just a result concatenating the input but not calculation.

new_height = float(height)  #height(in meter) may be in decimals so float data type is used.

new_weight = int(weight)

# calculate bmi using thr formula BMI= weight/(height**2)
BMI = new_weight / (new_height**2)

#print the result
print(f"your BMI is: {round(BMI)}")

