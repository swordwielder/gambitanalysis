import math
from random import random


turns = 100
suc = 86
multiplier = 1.05
tokens = 10000
daily=1.065
hedge = 0.0167
actualSB = 9000
total=0
totalvalue = actualSB*100


total=(tokens*multiplier)*suc
print('winning 6 out of 7 matches has a percentage of '+ str(round(6/7*100,2)))
print('After 100 tries with '   + str(suc) + ' percent chance win ratio')
print(total)
print('Spent: ')
print(totalvalue)

totalWithoutBets = 0


totalWithoutBets=turns*(actualSB-actualSB*hedge)

print()

print('After 100 tries with hedging at -1.67 everyday is:' + str(totalWithoutBets) )
print('loss of '+ str(totalvalue - totalWithoutBets))
print('spent:')
print(totalvalue)