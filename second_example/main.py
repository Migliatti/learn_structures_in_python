from counter import count_words

phrase = input("Write a phrase: ")
quantity = count_words(phrase)
print(f"The phrase has {quantity} words")