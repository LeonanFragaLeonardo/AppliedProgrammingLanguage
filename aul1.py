# -*- coding: utf-8 -*-
"""
Created on Sat May 30 09:35:20 2020

@author: leowc
"""

for i in [1, 2, 3, 4, 5]:
  print(i)                   # first line in "for i" block
  for j in [1, 2, 3, 4, 5]:
    print(j)                 # first line in "for j" block
    print(i + j)             # last line in "for j" block
  print (i)                   # last line in "for i" block
print("done looping")


long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
                           13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)

# and for making code easier to read:

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easier_to_read_list_of_lists = [ [1, 2, 3],
                                 [4, 5, 6],
                                 [7, 8, 9] ]

two_plus_three = 2 + \
                 3
                 
import re
my_regex = re.compile("[0-9]+", re.I)

import matplotlib.pyplot as plt

from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()


import some_module
result = some_module.f(5)
pi = some_module.PI
 

def double(x):
    """
    Here must contains a doc string
    """
    return x*2

def apply_to_one(f):
    return f(1)

my_double = double
x = apply_to_one(my_double)

"""
lambda x: x + 4
argumento   -> x
retorno     ->    x+4
"""
t = apply_to_one(lambda x: x + 4)
another_double = lambda x: x * 2
def another_double(x): return 2 * x


def my_print(message="My Default Parameter"):
    print(message)

my_print()
my_print("x")



integer_list = [1,2,3]
heterogeneous_list = ["123", 1, False]
  
i = range(0,10)

