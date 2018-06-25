def main():
    n =input()
    n=n.split(' ')
    if int(n[0])==1:
        n1 = input()
        n1 = n1.split(' ')
        s={}.fromkeys([x for x in range(int(n[1]))],[])
        for i in range(int(n[1])):
            temp=[]
            temp.append(n1[i])
            s[i]=temp
        for j in range(int(n[1])):
            print(' '.join(s[j]))
    if int(n[0])==3:
        n1 = input()
        n1 = n1.split(' ')
        n2 = input()
        n2 = n2.split(' ')
        n3 = input()
        n3 = n3.split(' ')
        s={}.fromkeys([x for x in range(int(n[1]))],[])
        for i in range(int(n[1])):
            temp=[]
            temp.append(n1[i])
            temp.append(n2[i])
            temp.append(n3[i])
            s[i]=temp
        for j in range(int(n[1])):
            print(' '.join(s[j]))
    if int(n[0])==2:
        n1 = input()
        n1 = n1.split(' ')
        n2 = input()
        n2 = n2.split(' ')
        s={}.fromkeys([x for x in range(int(n[1]))],[])
        for i in range(int(n[1])):
            temp=[]
            temp.append(n1[i])
            temp.append(n2[i])
            s[i]=temp
        for j in range(int(n[1])):
            print(' '.join(s[j]))
    if int(n[0])==4:
        n1 = input()
        n1 = n1.split(' ')
        n2 = input()
        n2 = n2.split(' ')
        n3 = input()
        n3 = n3.split(' ')
        n4=input()
        n4=n4.split(' ')
        s={}.fromkeys([x for x in range(int(n[1]))],[])
        for i in range(int(n[1])):
            temp=[]
            temp.append(n1[i])
            temp.append(n2[i])
            temp.append(n3[i])
            temp.append(n4[i])
            s[i]=temp
        for j in range(int(n[1])):
            print(' '.join(s[j]))
