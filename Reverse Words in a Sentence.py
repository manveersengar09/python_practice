# 15. Reverse Words in a Sentence
# •	Write a function to reverse the order of words in a sentence, keeping the words themselves intact (sentence should not be changed or altered in any way; they should remain exactly as they are,).
# Example
# Input: "Python is fun"
# Expected Output: "fun is Python"

def reverse_words(sentence):
    # Split sentence into words
    words = sentence.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join them back into a sentence
    return " ".join(reversed_words)

# Ex:- 1
sentence = "Python is fun"
print("Original:", sentence)
print("Reversed:", reverse_words(sentence))

# Output → "fun is Python"

# Ex :- 2 
sentence = "I love programming in Python"
print("Original:", sentence)
print("Reversed:", reverse_words(sentence))

# Output → "Python in programming love I"
