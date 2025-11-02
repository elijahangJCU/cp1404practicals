"""
Word Occurrences
Estimate: 30 minutes
Actual: 30 minutes
"""

user_string = input("Text: ").lower()

words = user_string.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

longest_word = max(len(word) for word in word_counts)

for word, count in sorted(word_counts.items()):
    print(f"{word:<{longest_word + 1}}: {count}")