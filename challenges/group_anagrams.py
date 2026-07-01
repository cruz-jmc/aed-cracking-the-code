def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_groups = {} # Dictionary to hold groups of anagrams
    for word in words:
        sorted_word = ''.join(sorted(word)) # Sort the characters of the word to get a unique key
        # for anagrams
        if sorted_word not in anagram_groups:# If the sorted word is not already a key in the 
            # dictionary, initialize it with an empty list
            anagram_groups[sorted_word] = []
        anagram_groups[sorted_word].append(word) # Add the original word to the corresponding
        # anagram group
    return list(anagram_groups.values())