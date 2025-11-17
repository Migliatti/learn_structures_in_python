# Mariana is a Portuguese language teacher and wants a program that counts how many vowels are in a text entered by her students. This will help her analyze the structure of the words used.

# Create a program that asks for a text and displays how many vowels (a, e, i, o, u) it contains.

def vogals_count(text):
    text = text.lower()
    vogals = "aeiou"
    count = 0
    for char in text:
        if char in vogals:
            count += 1
    return count


text = input("Enter a text: ")
print(f"The text contains {vogals_count(text)} vowels.")