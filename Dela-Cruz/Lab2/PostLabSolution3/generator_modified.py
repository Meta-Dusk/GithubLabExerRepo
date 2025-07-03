"""
Program: generator.py
Author: Ken
Generates and displays sentences using a simple grammar
and vocabulary. Words are chosen at random from text files in a user-specified directory.
"""
import random
import os

def getWords(filepath):
    """Reads words from a file and returns them as a tuple."""
    try:
        with open(filepath, 'r') as file:
            words = [line.strip() for line in file if line.strip()]  # Read and strip whitespace
            if not words:
                print(f"Error: File '{filepath}' is empty.")
                return ()
            return tuple(words)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return ()
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        return ()

# Global vocabulary variables
articles = ()
nouns = ()
verbs = ()
prepositions = ()

def main():
    """Allows the user to input a directory and the number of sentences to generate."""
    global articles, nouns, verbs, prepositions  # Declare global variables
    
    # Prompt for directory
    directory = input("Enter the directory containing vocabulary files: ").strip()
    
    # Validate directory existence
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    # Initialize vocabulary from text files in the specified directory
    articles = getWords(os.path.join(directory, "articles.txt"))
    nouns = getWords(os.path.join(directory, "nouns.txt"))
    verbs = getWords(os.path.join(directory, "verbs.txt"))
    prepositions = getWords(os.path.join(directory, "prepositions.txt"))
    
    # Check if all vocabulary lists are non-empty
    if not (articles and nouns and verbs and prepositions):
        print("Cannot generate sentences due to missing or empty vocabulary files.")
        return
    
    try:
        number = int(input("Enter the number of sentences: "))
        if number < 0:
            print("Please enter a non-negative number.")
            return
        for count in range(number):
            print(sentence())
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

# The entry point for program execution
if __name__ == "__main__":
    main()