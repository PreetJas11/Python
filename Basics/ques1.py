#  REVERSE A STRING


# def palindrome(z):
#     s1 = str(z)
#     s2= s1[::-1]

#     if s1==s2:
#         return True
#     else:
#         return False

# x=12345

# r= palindrome(x)
# print(r)


def reverse_string(s):
    s=list(s)

    left=0
    right= len(s)-1

    while left< right:
        s[left], s[right]= s[right],s[left]
        left+=1
        right -=1

    return "".join(s)

print(reverse_string('python'))
