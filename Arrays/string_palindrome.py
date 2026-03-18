s = "madat"

left  = 0 
right = len(s) -1 
if_palindrome = True
while left < right :
        if s[left] != s[right]:
                if_palindrome = False
                break
        left +=1
        right -=1 

if if_palindrome:
    print("Palindrome")
else:
    print("Not a Palindrome")