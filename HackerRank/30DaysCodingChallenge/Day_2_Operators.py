#!/bin/python3

import math
import os
import random
import re
import sys
print(round (float(input())*(1+int(input())*.01+int(input())*.01)))
# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    
    if __name__ == '__main__':
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())

        tip = meal_cost * (tip_percent/100)
        tax = meal_cost * (tax_percent/100)
        totalCost = meal_cost + tip + tax
        rounded_totalCost = round(totalCost)


    solve(meal_cost, tip_percent, tax_percent)

