import math 

#truncated 

def truncate(number):
    factor = 10 ** 7
    return math.trunc(number * factor) / factor

#inputs 

V1 = float(input("V1: "))
V2 = float(input("V2: "))
angle = math.radians(float(input("Angle: ")))

#math 

A = V1 * math.cos(angle) + V2 * math.sin(angle)
B = (-V1) * math.sin(angle) + V2 * math.cos(angle)

print(truncate(A))
print(truncate(B))
input("press to enter clear")
