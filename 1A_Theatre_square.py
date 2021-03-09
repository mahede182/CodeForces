# import math
# n = input(int())
# m = input(int())
# a = input(int())
#
#
# result = math.ceil(m/a)*math.ceil(n/a)
# print(result)

from math import ceil
n,m,a=map(int,input().split())
# print(ceil(n/a),ceil(m/a))
c=ceil(n/a)*ceil(m/a)
print(c)