# tree_index
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 12/02/18

import re
import pygtrie

class TreeIndex:
    def __init__(self, file_list):
        self.trie = pygtrie.StringTrie()
        self.pattern = re.compile("[,\s\n\-\u2014!?:.;()\"]+")
        self.files = {}
        self.process_files(file_list)
        self.save_index()

    def save_index(self):
        output = open("Dictionary Output/trie index.txt", "w+")
        for word in self.trie.iterkeys():
            output.write(word+'\n')
            for i in self.trie.get(word):
                output.write('\t'+self.files.get(i)+'\n')
        output.close()

    def process_files(self, list):
        file_count = 0
        for f in list:
            file = open(f, "r")
            self.process_file(file.read(), file_count)
            self.files.update({file_count: f})
            file_count += 1
            file.close()

    def process_file(self, content, number):
        tokens = re.split(self.pattern, content)
        for t in tokens:
            t = t.upper()
            if t not in self.trie.iterkeys():
                self.trie.update({t:[]})
            if number not in self.trie.get(t):
                self.trie.get(t).append(number)