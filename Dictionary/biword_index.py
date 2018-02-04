# biword_index
# in IR/Dictionary
# Constructs a biword index from a collection of documents
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 04/02/18
import re


def request(request):
    # TODO process requests with NOT AND OR (left to right, no parentheses allowed)

def parse_to_biword_tokens(str):
    tokens = re.split('\s+', str)
    res = []
    for i in range(0, len(tokens) - 2):
        biword = tokens[i] + ' '+tokens[i + 1]
        res.append(biword)
    return res


class BiwordIndex:
    def __init__(self, file_list):
        self.biword_index = {}
        self.file_count = 0
        self.files = {}
        for f in file_list:
            file = open(f, "r")
            self.add_words_from_file(file)
            self.files.update({self.file_count: f})
            self.file_count += 1
            file.close()
        self.save_index()

    def add_words_from_file(self, file):
        text = file.read()
        tokens = parse_to_biword_tokens(text)
        for biword_token in tokens:
            if biword_token not in self.biword_index.keys():
                self.biword_index.update({biword_token: []})
            self.biword_index.get(biword_token).append(self.file_count)

    def save_index(self):
        index_file = open("Dictionary Output/biword_index.txt", "w+")
        for word in self.biword_index.keys():
            index_file.write(word + '\n')
            index_file.write(self.files_by_indices(self.biword_index.get(word)) + '\n')
        index_file.close()

    def files_by_indices(self, file_number_list):
        res = ""
        for i in file_number_list:
            res += '\t' + self.files.get(i) + '\n'
        return res
