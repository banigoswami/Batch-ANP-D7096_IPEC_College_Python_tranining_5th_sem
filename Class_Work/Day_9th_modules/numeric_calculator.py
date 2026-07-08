'''Module for numerical operations'''
def add(a, b):
    '''Function to add two numbers'''
    return a + b

def subtract(a, b):
    '''Function to subtract two numbers'''
    return a - b

def multiply(a, b):
    '''Function to multiply two numbers'''
    return a * b

def divide(a, b):
    '''Function to divide two numbers'''
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a / b
def remainder(a, b):
    '''Function to find the remainder of two numbers'''
    if b == 0:
        raise ValueError("Denominator cannot be zero")
    return a % b