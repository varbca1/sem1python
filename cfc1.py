def char_frequency(s):
    freq = {} 
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq 

str1 = input("freq: ")
print(char_frequency(str1)) 