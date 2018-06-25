def main():
    s=input()
    uc=0
    lc=0
    s=s.replace(' ','')
    for i in s:
        if i.isupper():
            uc+=1
        else:
            lc+=1
    print(uc,lc,sep='\n')
