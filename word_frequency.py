def count_word_frequency(text):
    word_frequency = {}
    words = text.lower().split()

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    return word_frequency

# Run the Word Frequency Counter
text = input("Enter the text: ")
frequency = count_word_frequency(text)
print("Word Frequency:")
for word, count in frequency.items():
    print(f"{word}: {count}")
