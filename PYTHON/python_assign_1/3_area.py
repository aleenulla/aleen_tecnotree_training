import math

radius = float(input("Enter the radius of the circle: "))

# calculate area
area = math.pi * radius ** 2

# calculate circumference
circumference = 2 * math.pi * radius

print(f"The area of the circle is {area:.2f} square units.")
print(f"The circumference of the circle is {circumference:.2f} units.")
