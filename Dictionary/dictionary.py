import glob
import re


class Dictionary:
    def __init__(self, file_list):
        self.dict = []
        self.num_words = 0
        self.words_in_collection = 0
        self.collection_size = len(file_list)
        self.matrix = {}
        self.inverted_index = {}
        self.files = []
        count = 0
        for f in file_list:
            self.files.append(f)
            list_of_words = open(f, "r").read()
            tokenized_list_of_words = re.split("[,\s\n\-\u2014!?:.;()\"]+", list_of_words)
            for word in tokenized_list_of_words:
                self.words_in_collection += 1
                if word.upper() not in self.dict:
                    self.dict.append(word.upper())
                    self.num_words += 1
                    self.init_list(word)
                    self.inverted_index[word.upper()] = []
                self.matrix.get(word.upper())[count] = 1
                if count not in self.inverted_index[word.upper()]:
                    self.inverted_index.get(word.upper()).append(count)
            count += 1
        self.print_dictionary()
        self.print_matrix()
        self.print_index()

    def print_dictionary(self):
        dict_file = open("Output/dict.txt", "w+")
        dict_file.write("Files processed: " + str(self.collection_size) + '\n')
        dict_file.write("Total words: " + str(self.words_in_collection) + '\n')
        dict_file.write("Total unique words: " + str(self.num_words) + '\n' + "--------------------------------" + '\n')
        for word in self.dict:
            dict_file.write(word + '\n')
        dict_file.close()

    def print_matrix(self):
        matrix_file = open("Output/matrix.txt", "w+")
        for token in self.matrix.iterkeys():
            matrix_file.write(token + '\t')
            for i in self.matrix.get(token):
                matrix_file.write(str(i) + '\t')
            matrix_file.write('\n')
        matrix_file.close()

    def print_index(self):
        inverted_index_file = open("Output/index.txt", "w+")
        for token in self.inverted_index.iterkeys():
            inverted_index_file.write(token + '\t')
            for i in self.inverted_index.get(token):
                inverted_index_file.write(str(i) + '\t')
            inverted_index_file.write('\n')
        inverted_index_file.close()
        print("Files processed: " + str(self.collection_size) + '\n')
        print("Total words: " + str(self.words_in_collection) + '\n')
        print("Total unique words: " + str(self.num_words))

    def init_list(self, word):
        list_temp = []
        for i in range(0, self.collection_size, 1):
            list_temp.append(0)
        self.matrix[word.upper()] = list_temp

    def boolean_or(self, list_one, list_two):
        res = []
        for i in range(0, self.collection_size, 1):
            if i in list_one or i in list_two:
                res.append(i)
        return res

    def boolean_and(self, list_one, list_two):
        res = []
        for i in range(0, self.collection_size, 1):
            if i in list_one and i in list_two:
                res.append(i)
        return res

    def files_by_indices(self, l):
        new_list = []
        for i in l:
            new_list.append(self.files[i])
        return new_list

    def parse_request(self, request):
        tokens = request.split()
        current = []
        if not self.word(tokens[0].upper()):
            return False
        for i in self.inverted_index[tokens[0].upper()]:
            current.append(i)

        for i in range(1, len(tokens)-1, 2):
            if tokens[i] == "&&":
                if self.word(tokens[i+1].upper()):
                    current = self.boolean_and(current, self.inverted_index[tokens[i+1].upper()])
                else:
                    return False
            elif tokens[i] == "||":
                if self.word(tokens[i+1].upper()):
                    current = self.boolean_or(current, self.inverted_index[tokens[i+1].upper()])
            else:
                return False
        self.print_result(req, self.files_by_indices(current))

    @staticmethod
    def print_result(string, list):
        print("Search results for: "+string+'\n\n')
        for l in list:
            print(l+'\n')

    def word(self, str):
        return str!="&&" and str!="||" and str in self.dict


if __name__ == '__main__':
    collection = []
    for filename in glob.glob("Data/Samples/*.txt"):
        print(filename)
        collection.append(filename)
    dictionary = Dictionary(collection)
    req = raw_input("Search request using '&&' (and) and '||' (or): ")
    dictionary.parse_request(req)
