while True:
    n,k=map(int,input().split())
    out=0
    for i in range(n):
        ti=int(input())
        if (ti%k==0):
            out+=1
    print(out)
