import math
print("\n            ++-------------------------++")
print("              ++---------------------++")
print("*---*Calculator Volume of an equilateral Cube & Tetrahedron*---*")
print("               ++-------------------++")
print("              ++-----------------------++\n")

#Ask user what he wants to calculate
option = int(input('What you want to calculate,'
                        'please choose an option below.\n1.Volume of an equilateral Cube\n2'
                        '.Volume of an equilateral Tetrahedron\n:'))

unit = (input("Which unit you want to use in this calculation? "))

def cal_vol_cube(a):
  return a**3


def cal_vol_tetrahedron(a):
  return round((a ** 3 / (6 * math.sqrt(2))), 2)

def vol_cal_optins(option):
  if option == 1:
    a = int(input("Enter the side length of Cube: "))
    print(f"Volume of the Cube is {cal_vol_cube(a)}{unit}")
  else:
    a = int(input("What is the side length of the regular tetrahedron: "))  
    print(f"Volume of Tetrahedron is {cal_vol_tetrahedron(a)}{unit}") 

vol_cal_optins(option)
   