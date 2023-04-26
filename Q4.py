def anagrams(word, word_list):

    sorted_word = ''.join(sorted(word.lower().replace(" ", "")))


    anagrams_dict = {}


    for w in word_list:

        sorted_w = ''.join(sorted(w.lower().replace(" ", "")))

        if sorted_w in anagrams_dict:
            anagrams_dict[sorted_w].append(w)
        else:
            anagrams_dict[sorted_w] = [w]


    if sorted_word in anagrams_dict:
        return anagrams_dict[sorted_word]
    else:
        return []
word = "listen"
word_list = ["enlists", "google", "inlets", "banana"]
print(anagrams(word, word_list))
