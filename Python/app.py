def countValidWords(s):
    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    words = s.split()
    count = 0

    for word in words:
        if len(word) >= 3 and all(c.isalnum() for c in word):
            has_vowel = False
            has_consonant = False
            for c in word:
                if c in vowels:
                    has_vowel = True
                elif c in consonants:
                    has_consonant = True
            if has_vowel and has_consonant:
                count += 1

    return count

s = "This is Form16 submis$ion date"
result = countValidWords(s)
print(f"Number of valid words: {result}")