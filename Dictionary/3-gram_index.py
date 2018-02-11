# 3-gram_index
# 
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 11/02/18

import re


class ThreeGramIndex:
    def __init__(self, file_list):
        self.three_gram_index = {}
        self.inverted_index = {}
        self.files = {}
        self.parse_files(file_list)
        self.save_index()

    def parse_files(self, file_list):
        file_count = 0
        for f in file_list:
            file = open(f, "r")
            content = file.read()
            self.parse_file(content, file_count)
            self.files.update({file_count: f})
            file_count += 1
            file.close()

    def parse_file(self, content, file_no):
        tokens = re.split("[,\s\n\-\u2014!?:.;()\"]+", content)
        for token in tokens:
            token = ('$'+token+'$').upper()
            # 3-gram indexing
            for i in range(0, len(token)-2):
                threegram = (token[i]+token[i+1]+token[i+2])
                if threegram not in self.three_gram_index.keys():
                    self.three_gram_index.update({threegram: []})
                if token not in self.three_gram_index.get(threegram):
                    self.three_gram_index.get(threegram).append(token)
            # regular inverted index
            if token not in self.inverted_index:
                self.inverted_index.update({token: []})
            if file_no not in self.inverted_index.get(token):
                self.inverted_index.get(token).append(file_no)

    def save_index(self):
        output = open("Dictionary Output/3-gram index.txt", "w+")
        for threegram in self.three_gram_index.keys():
            output.write(threegram+'\n')
            for word in self.three_gram_index.get(threegram):
                output.write('\t'+word+'\n')
        output.close()
