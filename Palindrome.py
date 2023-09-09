def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return (s == s[::-1]) 

if (is_palindrome == True):
    print("It is a palindrome")
elif(is_palindrome == False):
    print("It is not an Palindrome")

s = input("palindrome: ")
print(is_palindrome(s)) 