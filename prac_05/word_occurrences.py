"""
Word Occurrences CP1404 - Practical 05
Estimate: 20 Minutes
Actual: 25 Minutes
"""

text = input("Text: ").lower()

words = text.split()

words_to_count = {}
for word in words:
    if word in words_to_count:
        words_to_count[word] += 1
    else:
        words_to_count[word] = 1

maximum_word_length = max(len(word) for word in words_to_count)

for word in sorted(words_to_count):
    print(f"{word:{maximum_word_length}} : {words_to_count[word]}")
