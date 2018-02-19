# permu_index
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 11/02/18

import re


class PermuIndex:
    def __init__(self, file_list):
        self.index = {}
        self.files = {}
        self.inverted_index = {}
        self.pattern = re.compile("[,\s\n\-\u2014!?:.;()\"]+")
        self.process_collection(file_list)
        self.save_index()

    def save_index(self):
        output = open("Dictionary Output/permu-term index.txt", "w+")
        for permuterm in self.index.keys():
            output.write(permuterm+'\n')
            for word in self.index.get(permuterm):
                output.write('\t'+word+'\n')
        output.close()

    def process_collection(self, list):
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
            self.add_one_permuterm(t)
            if t not in self.inverted_index.keys():
                self.inverted_index.update({t:[]})
            if number not in self.inverted_index.get(t):
                self.inverted_index.get(t).append(number)

    def add_one_permuterm(self, term):
        if len(term) < 1:
            return
        for i in range(0, len(term)):
            permu_term = ""
            for j in range(0, i):
                permu_term += term[j]
            permu_term += '$'
            permu_term += term[i]
            for j in range(i+1, len(term)):
                permu_term += term[j]
            if permu_term not in self.index.keys():
                self.index.update({permu_term: []})
            if term not in self.index.get(permu_term):
                self.index.get(permu_term).append(term)
        permu_term = term + '$'
        if permu_term not in self.index.keys():
            self.index.update({permu_term: []})
        if term not in self.index.get(permu_term):
            self.index.get(permu_term).append(term)
