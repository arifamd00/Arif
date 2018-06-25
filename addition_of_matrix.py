def main():
    n=input()
    n=n.split(' ')
    if int(n[0])==3:
        l1 = input()
        l1=l1.split(' ')
        l1=list(map(intl,l1))
        l2=input()
        l2=l2.split(' ')
        l2=list(map(intl,l2))
        l3=input()
        l3=l3.split(' ')
        l3=list(map(intl,l3))
    if int(n[0])==2:
        l1 = input()
        l1=l1.split(' ')
        l1=list(map(intl,l1))
        l2=input()
        l2=l2.split(' ')
        l2=list(map(intl,l2))
    m=input()
    m=m.split(' ')
    if int(m[0])==3:
        v1=input()
        v1=v1.split(' ')
        v1=list(map(intl,v1))
        v2=input()
        v2=v2.split(' ')
        v2=list(map(intl,v2))
        v3=input()
        v3=v3.split(' ')
        v3=list(map(intl,v3))
    if int(m[0])==2:
        v1=input()
        v1=v1.split(' ')
        v1=list(map(intl,v1))
        v2=input()
        v2=v2.split(' ')
        v2=list(map(intl,v2))
    r1=[]
    r2=[]
    r3=[]
    i=0
    j=0
    i1=0
    j1=0
    i2=0
    j2=0
    if int(n[0])==3:
        while i<len(l1):
            while j<len(v1):
                r1.append(l1[i]+v1[j])
                i+=1
                j+=1
                break
        while i1<len(l2):
            while j1<len(v2):
                r2.append(l2[i1]+v2[j1])
                i1+=1
                j1+=1
                break
        while i2<len(l3):
            while j2<len(v3):
                r3.append(l3[i2]+v3[j2])
                i2+=1
                j2+=1
                break
        r1=list(map(strl,r1))
        r2=list(map(strl,r2))
        r3=list(map(strl,r3))
        print(' '.join(r1))
        print(' '.join(r2))
        print(' '.join(r3))
    if int(n[0])==2:
        while i<len(l1):
            while j<len(v1):
                r1.append(l1[i]+v1[j])
                i+=1
                j+=1
                break
        while i1<len(l2):
            while j1<len(v2):
                r2.append(l2[i1]+v2[j1])
                i1+=1
                j1+=1
                break
        r1=list(map(strl,r1))
        r2=list(map(strl,r2))
        r3=list(map(strl,r3))
        print(' '.join(r1))
        print(' '.join(r2))
def intl(x):
    return(int(x))
def strl(x):
    return(str(x))
