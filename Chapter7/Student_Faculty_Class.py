# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:18:10 2020
Using classes to keep track of students and faculty
@author: rshirale
"""
import datetime

class Person(object):
    
    def __init__(self, name):
        """Create a person"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank+1:]
        except:
            self.lastName = name
        self.birthday = None
        
    def getName(self):
        """Returns self's full name"""
        return self.name
    
    def getLastName(self):
        """Returns self's last name"""
        return self.lastName
    
    def setBirthday(self,birthdate):
        """Assummes birthdate is of type datetime.date
        Sets self's birthday to birthdate"""
        self.birthday = birthdate
        
    def getAge(self):
        """Returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """Return True if self precedes other in alphabethical 
        order, and False otherwise. Comparison is based on last
        names, but if these are the same full names are compared."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
    def __str__(self):
        """Return self's name"""
        return self.name
        
        
class MITPerson(Person):
    
    nextIdNum = 0 #identification number
    
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    def __lt__(self, other):
        return self.idNum < other.idNum
        
class Student(MITPerson):
    pass

class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year

class Grad(Student):
    pass

        
        
        
        
        