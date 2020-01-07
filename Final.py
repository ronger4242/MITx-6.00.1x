# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:51:54 2020

@author: Nancy Zhao
"""

def sum_digits(s):
    sum = 0
    non_int = 0
    for char in s:
        try:
            sum += int(char)
        except:
            non_int += 1
    if len(s) != non_int:
         return sum
    else:
         raise ValueError

def largest_odd_times(L):
    d= {}
    d_odd = {} 
    for i in L:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for e in d:
        if d[e]%2 !=0:
            d_odd[e] = d[e]
    if len(d_odd) !=0:
        return max(d_odd.keys())
    else:
        return None
    
def dict_interdiff(d1, d2):
    inter = {}
    diff = {}
    for i in d1:
        if i in d2:
            inter[i] = f(d1[i],d2[i])
        else:
            diff[i] = d1[i]
    for j in d2:
        if j not in d1:
            diff[j] = d2[j]
    return(inter,diff)
    


class Person(object):
    def __init__(self, name):
        #create a person with name name
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank+1:]
        except:
            self.lastName = name
        self.age = None
    def getLastName(self):
        #return self's last name
        return self.lastName
    def setAge(self, age):
        #assumes age is an int greater than 0
        #sets self's age to age (in years)
        self.age = age
    def getAge(self):
        #assumes that self's age has been set
        #returns self's current age in years
        if self.age == None:
            raise ValueError
        return self.age
    def __lt__(self, other):
        #return True if self's name is lexicographically less
        #than other's name, and False otherwise
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    def __str__(self):
        #return self's name
        return self.name
    
class USResident(Person):
    """ 
    A Person who resides in the US.
    """
    def __init__(self, name, status):
        """ 
        Initializes a Person object. A USResident object inherits 
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        valid = ["citizen", "legal_resident", "illegal_resident"]
        if status in valid:
            self.status = status
        else:
            raise ValueError
        
    def getStatus(self):
        """
        Returns the status
        """
        return self.status


class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        if e in self.vals:
            return self.vals[e]
        else:
            return 0    
