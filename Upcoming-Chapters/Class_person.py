# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:20:53 2020
Exmaple of a Class 
@author: rshirale
"""
import datetime

class Person(object):
    
    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank =  name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
    
    def getName(self):
        """
        Returns self's full name

        """
        return self.name
    
    def getLastName(self):
        """
        Returns self's last name
        """
        return self.lastName
    
    def setBirthday(self, birthdate):
        """
        Assumes birthdate us of type datetime.date
        Sets self's birthday to birthdate
        """
        self.birthday = birthdate
        
    def getAge(self):
        """
        Returns
        -------
        Self's current age in days'

        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """
        Returns True if self precedes other in alplhabetical order,
        and False otherwise. Comparison is based on last names, but if these
        are the same full names are compared.
        -------
        """
        
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        """Returns self's name"""
        return self.name

me = Person('Rahul Shirale')
him = Person('Neel Daniel Shirale')
her = Person('Blanca')
print(him.getLastName())
him.setBirthday(datetime.date(2013, 2, 10))
her.setBirthday(datetime.date(1977, 7, 22))
print(him.getName(), 'is', him.getAge(), 'days old')
