text = "play games"
words = text.split()

longest_world = ""
shortest_world = ""
longest_world_length = 0
shortest_world_length = 0



for word in words:
    print(word)
    current_word_length = len(word)
    print(current_word_length)

    if current_word_length > longest_world_length:
        longest_world_length = current_word_length
        longest_world = word

    if current_word_length == 0:
            shortest_world_length = current_word_length
            shortest_world = word
    if current_word_length < shortest_world_length:
        shortest_world_length = current_word_length
        shortest_world = word


print(f"{longest_world_length=} {longest_world}")
print(f"{shortest_world_length=} {shortest_world}")