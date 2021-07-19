if __name__ == '__main__':
    x = int(input("hjhdjk: "))
    y = int(input("hhg: "))
    z = int(input("hjd: "))
    n = int(input("fd: "))
    
    list0 = [[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]
    print(list0)