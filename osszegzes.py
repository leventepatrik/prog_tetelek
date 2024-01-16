def osszegzes():
    n:int=int("N=")
    i:int=int("i=")
    ossz = 0
    while not n<0:
        for i in range(0,n+1,1):
            ossz+=1
        print(f"Az első {n}db természetes szám összege:{ossz}")

