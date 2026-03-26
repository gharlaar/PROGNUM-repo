#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""

    def __init__(self, N, M):
        self.N = N
        self.M = M
    def termN(self):  #returns the nth fibonacci number
        a = 0
        b = 1
        for i in range(self.N - 1):
            a, b = b, b+a
        return a
    def divbyM(self):  #gives the numbers that are divisible by M
        a = 0
        b = 1
        fibonacci = [0]
        for i in range(self.N - 1):
            a, b = b, b + a
            if a % self.M == 0:
                fibonacci.append(a)
        return fibonacci

fib = Fibonacci(100, 7)     

print(f"The 100th Fibonacci number is {fib.termN()}.")
print(f"The Fibonacci numbers divisible by 7 before the 100th term is {fib.divbyM()}.")

            

