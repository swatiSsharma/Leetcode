# Length of Last Word

'''
Given a string "S" consisting of upper or lower case alphabets and empty space characters " ". return 
the length of last word in the string.
If the last word does not exists return 0

NOTE: A word is defined as a character sequence consists of non-space characters only.
'''

def lenOfLastWord(string: str) -> int:
    count = 0
    for i in range(len(string)):
        if string[i] != ' ':
            count += 1
        else:
            # current character is a space
            while  (i + 1 < len(string)) and (string[i+1] == ' ') :
                i += 1
            if i ==  len(string)-1:   # end of the string, so this is the last word
                return count    
            else:
                count = 0

print(lenOfLastWord("hello  world "))
print(lenOfLastWord("hello world of Programming     "))
print(lenOfLastWord(" world "))

print("Hello World   ".split())

# space complexity -> constant ie O(1)
# time complexity -> linear ie O(n)