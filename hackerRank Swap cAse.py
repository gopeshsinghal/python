def swap_case(s):

    """
    how swapcase works:::
    k = list(s)
    for i in range(len(s)):
        if k[i].isupper():
           k[i] = k[i].lower()
        elif k[i].islower():
           k[i] = k[i].upper()
            
    s = ""
    for i in k:
        s = s+i
    """
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
