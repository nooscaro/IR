import tokenize
import glob


class Dictionary:
    dict = set()
    num_words = 0
    words_in_collection = 0
    collection_size = 0

    def __init__(self, file_list):
        for f in file_list:
            list_of_words = tokenize.tokenize(open(f,"r").read())
            for word in list_of_words:
                self.collection_size += 1
                self.words_in_collection += 1
                if not word in self.dict:
                    self.dict.add(word)
                    self.num_words += 1
        dict_file = open("dict","w+")
        for word in dict:
            dict_file.write(word)
        dict_file.write("Collection size = "+self.collection_size+"\nTotal words in collection = "+self.words_in_collection+"\nWords in dictionary = "+self.num_words);
        print("Collection size = " + self.collection_size + "\nTotal words in collection = " + self.words_in_collection + "\nWords in dictionary = " + self.num_words);


if __name__ == '__main__':
    collection = []
    for filename in glob.glob('*.txt'):
        collection.append(filename)
    dictionary = Dictionary(collection)