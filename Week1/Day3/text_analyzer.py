# Text Analyzer

def text_analyzer():

    text = input("Enter a paragraph:\n")

    # Total Characters
    total_characters = len(text)

    # Total Words
    words = text.split()
    total_words = len(words)

    # Total Sentences
    sentences = 0
    for ch in text:
        if ch == '.' or ch == '!' or ch == '?':
            sentences = sentences + 1

    # Total Vowels
    vowels = 0
    for ch in text.lower():
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowels = vowels + 1

    # Total Consonants
    consonants = 0
    for ch in text.lower():
        if ch >= 'a' and ch <= 'z':
            if ch != 'a' and ch != 'e' and ch != 'i' and ch != 'o' and ch != 'u':
                consonants = consonants + 1

    # Total Digits
    digits = 0
    for ch in text:
        if ch >= '0' and ch <= '9':
            digits = digits + 1

    # Total Special Characters
    special = 0
    for ch in text:
        if not((ch >= 'a' and ch <= 'z') or
               (ch >= 'A' and ch <= 'Z') or
               (ch >= '0' and ch <= '9') or
               ch == ' '):
            special = special + 1

    # Longest Word
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word

    # Shortest Word
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word

    # Most Frequently Used Word
    frequency = {}

    for word in words:
        word = word.lower()

        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1

    most_word = ""
    max_count = 0

    for word, count in frequency.items():
        if count > max_count:
            max_count = count
            most_word = word

    # Display Results
    print("\n===== TEXT ANALYSIS =====")
    print("Total Characters :", total_characters)
    print("Total Words :", total_words)
    print("Total Sentences :", sentences)
    print("Total Vowels :", vowels)
    print("Total Consonants :", consonants)
    print("Total Digits :", digits)
    print("Total Special Characters :", special)
    print("Longest Word :", longest)
    print("Shortest Word :", shortest)
    print("Most Frequently Used Word :", most_word)


text_analyzer()