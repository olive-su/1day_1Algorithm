def is_palindrome(word):
    for i in range(len(word)):
        if (word[i] != word[len(word) - 1 - i]):
            return False
    return True

# test
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))
