message = input(">")
words = message.split(" ")  # splits all words of a sentence in different lists
emojis = {
    ":)": "😀",
    ":(": "😞"
}
output = " "
for word in words:
    output += emojis.get(word, word) + " "
print(output)
