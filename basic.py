import os
import time
import datetime
import functions

functions.multiple_table()
this_year=2021
myname=input('pls input your name:')
myage=int(input('how old are you:'))

print('hello ' ,myname + '\n')
print('you are ',myage, 'years old')
print('so you were born in : ', this_year-myage)
