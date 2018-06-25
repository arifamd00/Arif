def main():
    n=int(input())
    l=input()
    l=l.split(' ')
    if n==len(l):
        intl=list(map(int_l,l))
        intl.remove(max(intl))
        print(max(intl))
def int_l(x):
    return(int(x))
