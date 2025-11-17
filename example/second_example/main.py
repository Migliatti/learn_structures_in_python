from counter import count_words

phrase = input("Write a phrase: ").strip()
if not phrase:
    print("The phrase is empty")
else:
    result = count_words(phrase)
    if result:
        print("Word count:")
        for word, count in result.items():
            print(f"{word}: {count}")
    else:
        print("No words found in the phrase")