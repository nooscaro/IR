''' tester
    in IR/Dictionary
    Tester file for dicitonary classes
    Vera Baklanova (@nooscaro)
    Applied Mathematics @ FI, NAUKMA-2020
    https://github.com/nooscaro
    04/02/18
'''
import glob
import Dictionary.dictionary
import Dictionary.biword_index

def run_dictionary(collection):
    dictionary = Dictionary.dictionary.Dictionary(collection)
    req = input("Search request using '&&' (and) and '||' (or): ")
    dictionary.parse_request(req)

def run_biword_index(collection):
    biword = Dictionary.biword_index.BiwordIndex(collection)

if __name__ == '__main__':
    collection = []
    for filename in glob.glob("Data/Books/*.txt"):
        print(filename)
        collection.append(filename)
    run_biword_index(collection)
