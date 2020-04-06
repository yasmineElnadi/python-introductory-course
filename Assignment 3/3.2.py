#3.2 Palindrome integer


###### functions ######
def reverse(n):
    s=str(n)
    revstr=s[::-1]
    revnumber=int(revstr)
    return(revnumber)

def isPalindrome(s):
    rev=reverse(s)
    if (s==rev):
        return True
    return False



##### main #####

val=eval(input("enter a number:"))
print(reverse(val))

if isPalindrome(val):
    print("is palindrome")
else:
    print("not palindrome")

    


