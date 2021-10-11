text_file = open("words_alpha.txt", "r")
word_list = text_file.read().split('\n')
palindrome_list = []
for word in word_list:
    if word == word[::-1] and len(word) > 1:
        palindrome_list.append(word)

print(len(palindrome_list))
print(len(word_list))
