# ''' tester
#     in IR/Dictionary
#     Tester file for dicitonary classes
#     Vera Baklanova (@nooscaro)
#     Applied Mathematics @ FI, NAUKMA-2020
#     https://github.com/nooscaro
#     04/02/18
# '''
import glob
import Dictionary.position_inverted_index
import Dictionary.biword_index
import Dictionary.dictionary
import Dictionary.three_gram_index

def run_dictionary(collection):
    dictionary = Dictionary.dictionary.Dictionary(collection)
    req = input("Search request using '&&' (and) and '||' (or): ")
    dictionary.parse_request(req)

def run_biword_index(collection):
    biword = Dictionary.biword_index.BiwordIndex(collection)
    biword.request()

def run_postion_index(collection):
    pos = Dictionary.position_inverted_index.PositionInvertedIndex(collection)
    pos.process_request()

def run_three_gram_index(collection):
    thrgr = Dictionary.three_gram_index.ThreeGramIndex(collection)
    while True:
        req = input("Search with * for jokers now! Remember that our index is threegramed, so be aware that there must be at least three symbols between each *")
        if req == '0':
            return
        thrgr.process_request(req)


if __name__ == '__main__':
    collection = []
    for filename in glob.glob("Data/Books/*.txt"):
        print(filename)
        collection.append(filename)
    # run_biword_index(collection)
    # run_postion_index(collection)
    run_three_gram_index(collection)