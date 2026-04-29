def sort_words_by_order(words, order):
    # Create a rank dictionary for O(1) character priority lookup
    rank = {}
    for index, char in enumerate(order):
        rank[char] = index
    
    # Helper function to convert a word into a list of ranks
    # This replaces the need for a lambda key
    def get_word_priority(word):
        priority_list = []
        for char in word:
            priority_list.append(rank[char])
        return priority_list

    # Sort using the helper function as the key
    words.sort(key=get_word_priority)
    
    return words