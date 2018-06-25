def main2():
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
