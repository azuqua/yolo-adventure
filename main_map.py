__author__ = 'Wilson'

from setup import *

def main():
    # Get argument for wordlist.txt
    try:
        arg_1 = sys.argv[1]
    except:
        print "usage: python main.py mapfile.txt (where mapfile.txt is a text file with floats relating to a word.)"
        sys.exit(1)

    # Open input .txt file
    try:
        txt_file = open("import/wordlist.txt")
        map_file = open(arg_1)
    except:
        print "Unable to open import/wordlist.txt or " + arg_1
        sys.exit(1)

    # Place words from .txt file into a dictionary
    d = dict()
    del_chars = string.punctuation.translate(string.maketrans("",""),"'")
    trans = string.maketrans(del_chars," "*len(del_chars))
    for line in txt_file:
        # In order to get ride of pesky escape and hex characters in the text files.
        ln = unicode(line,errors='ignore').encode('utf8').strip(string.whitespace + "-").translate(trans).split()
        for elem in ln:
            d[elem] = 0

    # Treating side cases that fail the above logic for string parsing (for example, B & W).
    for elem in string.ascii_letters.translate(string.maketrans("",""),"aAiI") + "'":
        if d.has_key(elem): del d[elem]

    # Place words and floats from map file into a dictionary
    d2 = dict()
    for line in map_file:
        arr = line.strip('\n').split(' ')
        d2[arr[0]] = float(arr[1])

    # Use this dictionary to construct a trie tree of the words
    p = pytrie.SortedStringTrie(d)
    s = raw_input("Please input prefix: ")

    # While user doesn't input quitting string, take input and print all
    # strings in trie tree that have a matching prefix lexographically.
    while s != 'I quit (seriously now guys)':
        for item in sorted(p.keys(s), key=lambda i: d2[i]):
            print item
        s = raw_input("Please input prefix: ")

    # Clean up
    txt_file.close()
    print "Take care now!"

if __name__ == "__main__":
    main()