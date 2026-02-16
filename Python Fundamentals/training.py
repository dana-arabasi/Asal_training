"""
Python Fundamentals - Training File
Author: Dana Arabasi
Description:
This file demonstrates Python basics in a clean, organized,
and PEP8-compliant way for learning purposes.
"""

# =========================
# Imports
# =========================
from abc import ABC, abstractmethod
import numpy as np
import array as arr


# =========================
# Input & Output
# =========================
def input_output_examples():
    name = input("What is your name? ")
    print(name)

    try:
        number = int(input("Enter a number: "))
        print(number, "is of type", type(number))
    except ValueError:
        print("Invalid input! Please enter a number.")

    first, second = input("Enter two values: ").split()
    print(first, second)

    elements = input("Enter elements separated by space: ").split()
    print("List:", elements)


# =========================
# Variables & Data Types
# =========================
def variable_examples():
    age = 22
    user_name = "Dana"
    is_student = True

    print(age)
    print(user_name)
    print(is_student)
    print(type(age))


# =========================
# Strings
# =========================
def string_examples():
    text = "hello world"
    print(text.upper())
    print(text.lower())
    print(text[::-1])
    print("hello" in text)


# =========================
# Lists
# =========================
def list_examples():
    numbers = [1, 2, 3, 4]
    numbers.append(5)
    numbers.remove(2)
    print(numbers)

    squares = [x ** 2 for x in range(1, 6)]
    print(squares)


# =========================
# Tuples
# =========================
def tuple_examples():
    person = ("Dana", 22)
    name, age = person
    print(name, age)


# =========================
# Dictionaries
# =========================
def dictionary_examples():
    student = {"name": "Dana", "age": 22}
    student["major"] = "CS"

    for key, value in student.items():
        print(key, value)


# =========================
# Sets
# =========================
def set_examples():
    unique_numbers = {1, 2, 3, 3, 4}
    unique_numbers.add(5)
    print(unique_numbers)


# =========================
# Operators
# =========================
def operator_examples():
    num1, num2 = 10, 20
    min_value = num1 if num1 < num2 else num2
    print("Min value:", min_value)


# =========================
# Control Flow
# =========================
def control_flow_examples():
    age = 25

    if age < 18:
        print("Minor")
    elif age < 35:
        print("Young Adult")
    else:
        print("Adult")


# =========================
# Loops
# =========================
def loop_examples():
    for char in "Dana":
        print(char)

    count = 0
    while count < 3:
        print("Hello")
        count += 1


# =========================
# Functions
# =========================
def add_numbers(x, y):
    return x + y


def function_examples():
    result = add_numbers(5, 3)
    print(result)

    cube = lambda x: x ** 3
    print(cube(4))


# =========================
# Object-Oriented Programming
# =========================
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


def oop_examples():
    dog = Dog("Buddy")
    print(dog.name)
    print(dog.sound())


# =========================
# Abstraction
# =========================
class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass


class English(Greet):
    def say_hello(self):
        return "Hello!"


# =========================
# Encapsulation
# =========================
class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self._age = age
        self.__salary = salary

    def show_salary(self):
        print("Salary:", self.__salary)


# =========================
# Decorators
# =========================
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper


@decorator
def greet():
    print("Hello World")


# =========================
# Main Runner
# =========================
def main():
    input_output_examples()
    variable_examples()
    string_examples()
    list_examples()
    tuple_examples()
    dictionary_examples()
    set_examples()
    operator_examples()
    control_flow_examples()
    loop_examples()
    function_examples()
    oop_examples()
    greet()


if __name__ == "__main__":
    main()
