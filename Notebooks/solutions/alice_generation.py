with open("/data/alice_in_wonderland.txt") as f:
    text = f.read().lower()
    

def get_trigrams(text):
    return [text[i:i+3] for i in range(len(text) - 2)]

trigrams = get_trigrams(text)

trigram_count = {}
for trigram in trigrams:
    if trigram not in trigram_count:
        trigram_count[trigram] = 0
    
    trigram_count[trigram] += 1


def get_trigrams_starting(trigrams, starting_letters):
    return [trigram for trigram in trigrams if trigram.startswith(starting_letters)]


new_text = "at"

import random
for i in range(1000):
    starting_letters = new_text[-2:]
    possible_trigrams = get_trigrams_starting(trigrams, starting_letters)
    chosen_trigram = random.choice(possible_trigrams)
    new_text += chosen_trigram[-1]
    
print(new_text)