def nonrepeat(s):
    n=len(s)

    for i in range(n):
        f=False

        for j in range(n):

            if i!=j and s[i] ==s[j]:
                f=True
                break
            
        if not f:
            return s[i]
    return '$'

print(nonrepeat('abcdacb'))

