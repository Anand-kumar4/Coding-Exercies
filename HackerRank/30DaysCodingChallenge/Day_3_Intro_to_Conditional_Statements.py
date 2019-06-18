#!/bin/python3

import math
import os
import random
import re
import sys


def isWeird(N):
    if(N%2 != 0) or (N>=6 and N<=20):
        return "Weird"
    if(N>=2 and N<=5) or (N>20):
        return "Not Weird"

if __name__ == '__main__':
    N = int(input())
    print(isWeird(N))
#One Line Solution using Regex
#if __name__ == '__main__':
    #N = int(input().strip())
    #print("Not "*bool(re.match(r'^(..)(\1|\1{10,})?$','1'*N))+"Weird")

