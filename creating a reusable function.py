def emoji_converter(messsage):                # emoji_converter is a reusable function
    words = message.split(" ")
    emojis = {
        ":)": "😀",
        ":(": "😞"
    }
    output = " "
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
