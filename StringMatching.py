def string_matching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
                break
    return result
# 1. Take input as a single line separated by spaces
user_input = input("Enter words separated by spaces: ")

# 2. Convert the input string into a list
words_list = user_input.split()

# 3. Call the function and print result
print(string_matching(words_list))