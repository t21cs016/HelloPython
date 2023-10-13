'''
Created on 2023/10/13

@author: t21cs016
'''
def fibo(n):
    if n==0 or n==1:
          return 1;
    return fibo(n-1) + fibo(n-2)