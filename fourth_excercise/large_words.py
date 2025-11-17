# Sofia is a text reviewer and needs to identify very long words in a paragraph. Easier-to-read texts tend to have short words, so she wants a program that finds words longer than 10 letters and highlights them.

# Create a program that receives a text and displays all words that have more than 10 letters. If no long word is found, the program should inform the user.

# take worlds from user

# function to find large words

def find_large_words(text):
    words = text.split()
    large_words = [word for word in words if len(word) > 10]
    
    if large_words:
        print(f"Large words quantity: {len(large_words)}")
    else:
        print("No large words found.")

text = input("Enter a text: ")
find_large_words(text)