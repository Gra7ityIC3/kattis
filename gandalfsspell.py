def solve(chars, words):
    if len(chars) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for char, word in zip(chars, words):
        mapped_word = char_to_word.get(char)
        mapped_char = word_to_char.get(word)
        if mapped_word:
            if mapped_word != word:
                return False
        else:
            char_to_word[char] = word
        if mapped_char:
            if mapped_char != char:
                return False
        else:
            word_to_char[word] = char
    return True

print(solve(input(), input().split()))