import itertools
import nltk

# Download the CMU Pronouncing Dictionary if not already downloaded
nltk.download('cmudict')

# Load the dictionary
arpabet = nltk.corpus.cmudict.dict()

def get_syllables(word):
    # Get the ARPAbet phonetic transcription of the word
    try:
        phones = arpabet[word.lower()][0]
    except KeyError:
        # If the word is not in the dictionary, return an empty list
        return []
    
    # Identify the vowel sounds in the phonetic transcription
    vowels = ['AE', 'AH', 'AO', 'AW', 'AY', 'EH', 'ER', 'EY', 'IH', 'IY', 'OW', 'OY', 'UH', 'UW']
    syllables = []
    current_syllable = []
    
    for phone in phones:
        if phone in vowels:
            # If the phone is a vowel, start a new syllable
            current_syllable.append(phone)
            syllables.append(''.join(current_syllable))
            current_syllable = []
        else:
            # If the phone is not a vowel, add it to the current syllable
            current_syllable.append(phone)
    
    # If there are any remaining phones in the current syllable, add them as a final syllable
    if len(current_syllable) > 0:
        syllables.append(''.join(current_syllable))
    
    return syllables

def get_combinations():
    words = []
    while True:
        word = input("Type the word\n>>:")
        if word == '':
            break
        else:
            words.append(word)
    # Get the syllables for each word
    syllables_list = [get_syllables(word) for word in words]
    # Get all possible combinations of syllables
    combinations = list(itertools.product(*syllables_list))
    # Join the syllables together to form words
    words = [''.join(combination) for combination in combinations]
    # Remove any duplicate words
    words = list(set(words))
    return words

print(get_combinations())
