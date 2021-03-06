from typing import Dict, Iterator
from input_output import output
from Levenshtein import hamming
import numpy as np

def hamming_distance(words: Iterator[str], vocabulary: Dict[str, int]):
    """Corrects the words based on Hamming distances

    Args:
        words (Iterator[str]): Iterator over the misspelled words
        vocabulary (Dict[str,int]) : dictionary holding words and their frequency
    """

    for word in words:
        distances = []
        suggestions = []
        vocab_list = list(vocabulary)
        for (i,vocab) in enumerate(vocab_list):
            if len(vocab) == len(word):
                distances.append(hamming(word, vocab))
            else:
                distances.append(120)
            
        idx = np.array(distances).argsort()[:5]
        
        for i in range(5):
            for j in range(i+1,5):
                if distances[idx[i]] == distances[idx[j]]:
                    if vocabulary.get(vocab_list[idx[i]]) < vocabulary.get(vocab_list[idx[j]]):
                        temp = idx[i] 
                        idx[i] = idx[j]
                        idx[j] = temp   

        for i in idx:
            suggestions.append(vocab_list[i])

        output("{misspelled}\t{corrections}".format(
            misspelled=word,
            corrections="\t".join(suggestions)
        ))  # may cause IO bottleneck
