import glob


class Dictionary:


    def __init__(self, file_list):
        self.dict = set()
        self.num_words = 0
        self.words_in_collection = 0
        self.collection_size = 0
        for f in file_list:
            list_of_words = open(f, "r").read()
            tokenized_list_of_words = list_of_words.split()
            for word in tokenized_list_of_words:
                self.collection_size += 1
                self.words_in_collection += 1
                if word not in self.dict:
                    self.dict.add(word)
                    self.num_words += 1
        dict_file = open("dict.txt", "w+")
        for word in self.dict:
            dict_file.write(word+'\n')
        # dict_file.write("Collection size = "+self.collection_size+"\nTotal words in collection = "+self.words_in_collection+"\nWords in dictionary = "+self.num_words);
        # print("Collection size = " + self.collection_size + "\nTotal words in collection = " + self.words_in_collection + "\nWords in dictionary = " + self.num_words);


if __name__ == '__main__':
    collection = []
    for filename in glob.glob('*.txt'):
        collection.append(filename)
    dictionary = Dictionary(collection)