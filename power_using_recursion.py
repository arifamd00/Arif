def main():
    n= input()
    n=n.split(' ')
    n=list(map(intl,n))
    print(n[0]**n[1])
def intl(x):
    return(int(x))
