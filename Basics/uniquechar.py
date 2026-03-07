

#  ---------------------

# def uniquechar(s):
#     set1= set(s)
#     print(set1)
#     print(len(set1))

    


# s='racecars'
# uniquechar(s)


#  ---------------------


# s= "racecars"
# uniquestr= ''

# for char in s:
#     if char not in uniquestr:
#         uniquestr +=char


# print(uniquestr[0])

# UNIQUE CHARS

from collections import Counter

def fun(s):
    c= Counter(s)

    # print(c)

    for char in s:
        if c[char]==1:
            return char
    return None



s= 'swiss'
print(fun(s))