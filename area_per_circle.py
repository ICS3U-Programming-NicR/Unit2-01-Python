#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 02-28-2022

# Calculates the area and perimeter of a square


import math

PI = math.pi


def main():
    r = float(input("Enter the radius of a circle:"))
    perimeter = PI * r * 2
    area = PI * r * r
    print("Area of a circle = %.2f" % area)
    print("Perimeter of a circle = %.2f" % perimeter, end = "\r")


if __name__ == "__main__":
    main()
