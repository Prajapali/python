##2.2 (Compute the volume of a cylinder) Write a program that reads in the radius and length of a cylinder and computes 
# ##the area and volume using the following formulas:


##area = radius * radius * π
##volume = area * length

pi = 3.14159

radius = float(input("Enter the radius: "))
length = float(input("Enter the length: "))

area = radius * radius * pi
volume = area * length

print("Area:", area)
print("Volume:", volume)

![Exercise](../Images/img-Ex_2_2)




