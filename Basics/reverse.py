def reverse(s):

    r=''
    for char in s:
        r=char+r
        print(r)

    return r

print(reverse('abcde'))