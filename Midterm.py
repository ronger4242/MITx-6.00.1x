# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 22:18:25 2019

@author: Nancy Zhao
"""

#Midterm
"""
Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have
the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is
1*4 + 2*5 + 3*6, meaning your function should return: 32
"""
def dotProduct(listA, listB):
    sum = 0
    for i in range(0,len(listA)):
        prod= listA[i] * listB[i]
        sum += prod
    return sum
listA = [1, 2, 3]
listB = [4, 5, 6]
dotProduct(listA, listB)


"""
Write a recursive Python function, given a non-negative integer N,
to calculate the no. of occurrences of digit 7 in N.
Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6),
while doing integer division by 10 removes the rightmost digit (126 / 10 is 12).
This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.
"""
def count7(num):
    if num == 0:
        return 0
    elif num % 10 == 7:
        return 1 + count7(num//10)
    else:
        return count7(num//10)
num1 = 1237123
count7(num1)
num2 = 717
count7(num2)
num3 = 8989
count7(num3)

def sumDigits(N):
    if N<=9:
        return N
    else:
        return N%10 + sumDigits(N//10)
sumDigits(8)
sumDigits(123)
    

#none-recursive way:

def digit_seven(number):
    list = []
    count = 0
    digits = len(str(number))
    for i in range(0,digits):
        list += str((number//(10**i))%10)
    for elem in list:
        if int(elem) == 7:
            count += 1
    return count
num3 = 71771
digit_seven(num3)
"""
Write a Python function that returns the sublist of strings in aList
that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"],
your function should return: ["cat", "dog"]
This function takes in a list of strings and returns a list of strings.
Your function should not modify aList.
"""
result = []
def lessthan4(aList):
    for element in aList:
        if len(element) <=4:
            result.append(element)
    return result
aList = ["apple", "cat", "dog", "banana"]
lessthan4(aList)


"""
Implement a function called closest_power that meets the specifications below.

def closest_power(base, num):
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.     Returns the exponent.
"""
def closest_power(base, num):
    if base > num:
        return 0
    else:
        for expo in range(1, num):
            if abs(base**expo-num) <= abs(base**(expo+1)-num) and abs(base**expo-num) <= abs(base**(expo-1)-num):
                return expo
closest_power(4,4)

"""
Write a function to flatten a list. The list contains other lists, strings, 
or ints. For example, [[1,'a',['cat'],2],[[[3]],'dog'],4,5] is flattened 
into [1,'a','cat',2,3,'dog',4,5] (order matters).
"""
def flatten(aList):
    newlist = []
    for elem in aList:
        if type(elem) == list:
            newlist.extend(flatten(elem)) # 
        else:
            newlist.append(elem)
    return newlist
            #return str(elem) + str(flatten(aList))
aList = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatten(aList)

#differences between append and extend
x = [1,2,3]
x.append([4,5]) #[1, 2, 3, [4, 5]]
print(x)
y = [1,2,3]
y.extend([4,5])
print(y) #[1, 2, 3, 4, 5]

def dict_invert(d):
    inverse = {}
    for keys in d.keys():
        if d[keys] in inverse:
            inverse[d[keys]].append(keys)
        else:
            inverse[d[keys]] = [keys]
    for values in inverse.values():
        values.sort()
    return inverse
d = {2:10, 1:20, 3:30}
dict_invert(d)

def satisfiesF(L):
    i = 0
    while i < len(L):
        if f(L[i]) == False:
            L.pop(i)
        else:
            i += 1
    return len(L)
run_satisfiesF(L, satisfiesF)

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x

def f(x):
    return 3

for i in range(1000001, -1, -2):
    print(f)

