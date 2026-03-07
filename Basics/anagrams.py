#  ANAGRAMS

def anagrams(s1,s2):

    if len(s1) !=len(s2):
        return False
    
    s1= sorted(s1)
    s2=sorted(s2)

    return s1 == s2

if __name__=="__main__":

    s1='makers'
    s2='make'

    print(anagrams(s1,s2))


