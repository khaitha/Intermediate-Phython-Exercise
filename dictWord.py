def count_letters(string):
    letter_count = {}
    string = string.lower()
    for char in string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
    return letter_count

user_string = input("Enter a string: ")
letter_count = count_letters(user_string)
print(letter_count)