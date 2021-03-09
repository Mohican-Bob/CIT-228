filenames = ['Chapter10/alice.txt', 'Chapter10/bukowski.txt', 'Chapter10/picoult.txt']
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

def find_words(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        contents.lower
        word.lower
        words=contents.count(word)
        print("the word", word, "appears", words, "times")
for filename in filenames:
    count_words(filename)
word = input("enter a common word you you would like to count in each file: ")
for filename in filenames:   
    find_words(filename, word)


