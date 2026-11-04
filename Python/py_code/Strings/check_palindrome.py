s = "MadAM"
s2 = "Mad*am"

def palindrome(s):
    i=0
    j=len(s)-1
    while(i<j):
        if (s[i].upper() != s[j].upper()):
            return False
        i+=1
        j-=1
    return True

print(palindrome(s))



if(not s2.isalnum):
    print(False)
else:
    print(palindrome(s2))





