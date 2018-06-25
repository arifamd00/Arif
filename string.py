print(__name__)
from string_sorted import*
def main1():
    i=0
    l=[]
    n= int(input())
    while i!=n:
        n1=input()
        l.append(n1)
        i+=1
    l.sort()
    for x in l:
        print(x)
