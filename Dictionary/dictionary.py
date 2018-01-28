import glob
import re


class Dictionary:
    def __init__(self, file_list):
        self.dict = []
        self.num_words = 0
        self.words_in_collection = 0
        self.collection_size = len(file_list)
        self.matrix = {}
        count = 0
        for f in file_list:
            list_of_words = open(f, "r").read()
            tokenized_list_of_words = re.split("[,\s\n\-\u2014!?:.;()\"]+", list_of_words)
            for word in tokenized_list_of_words:
                self.words_in_collection += 1
                if word.upper() not in self.dict:
                    self.dict.append(word.upper())
                    self.num_words += 1
                    self.init_list(word)
                self.matrix.get(word.upper())[count] = 1
            count += 1
        dict_file = open("dict.txt", "w+")
        dict_file.write("Files processed: "+str(self.collection_size)+'\n')
        dict_file.write("Total words: "+str(self.words_in_collection)+'\n')
        dict_file.write("Total unique words: "+str(self.num_words)+'\n'+"--------------------------------"+'\n')
        for word in self.dict:
            dict_file.write(word+'\n')
        dict_file.close()
        matrix_file = open("matrix.txt","w+")
        for token in self.matrix.iterkeys():
            matrix_file.write(token+'\t')
            for i in self.matrix.get(token):
                matrix_file.write(str(i)+'\t')
            matrix_file.write('\n')
        matrix_file.close()
        print("Files processed: " + str(self.collection_size) + '\n')
        print("Total words: " + str(self.words_in_collection) + '\n')
        print("Total unique words: " + str(self.num_words))

    def init_list(self, word):
        list_temp = []
        for i in range(0,self.collection_size,1):
            list_temp.append(0)
        self.matrix[word.upper()] = list_temp


if __name__ == '__main__':
    collection = []
    for filename in glob.glob('*.txt'):
        collection.append(filename)
    dictionary = Dictionary(collection)
