#!/bin/python3

import sys


# Complete the function below.
class stack_element:
    def __init__(self,v,o):
        self.value = v
        self.offset = o
    def __str__(self):
        return f'{self.value + self.offset}'

class stack:
    def __init__(self):
        self.stack=[]

    def push(self,v):
        new_element = stack_element(v,0)
        self.stack.append(new_element)
        print(v)
    def pop(self):
        if self.stack:
            top_element = self.stack.pop()
            if self.stack:
                self.stack[-1].offset += top_element.offset
                print(self.stack[-1])
            else:
                print("EMPTY")
        else:
            print("EMPTY")
    def inc(self,i,v):
        if self.stack:
            i = min(i, len(self.stack))
            self.stack[i-1].offset += v
        print(self.stack[-1] if len(self.stack) else "EMPTY")
        
        
def superStack(operations):
    stack_instance = stack()
    stack_instance.push
    for operation in operations:
        params = operation.split()
        # calls the function with the params passed by parsing the string
        getattr(stack_instance,params[0])(*[int(param) for param in params[1:]])