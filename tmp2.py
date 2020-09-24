#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Cat:
    #属性

    def eat(self):
        print('Cat is eatting.')

    def drink(self):
        print('Cat is drinking!')

Tom = Cat()

Tom.name = '汤姆'
Tom.age = 18

Tom.eat()
Tom.drink()
print(Tom.name,Tom.age)


