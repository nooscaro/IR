# 3-gram_index
# 
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 11/02/18

import re


def parse_into_threegrams(string):
    string = '$'+string+'$'
    res = []
    for i in range(0, len(string)-2):
        res.append((string[i]+string[i+1]+string[i+2]))
    return res


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
            token = token.upper()
            threegrams = parse_into_threegrams(token)
            # 3-gram indexing
            for i in threegrams:
                if i not in self.three_gram_index.keys():
                    self.three_gram_index.update({i: []})
                if token not in self.three_gram_index.get(i):
                    self.three_gram_index.get(i).append(token)
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

    def process_request(self, req):
        req = '$'+req.upper()+'$'
        request = req.split('*')
        requested_tokens = []
        for r in request:
            if len(r) >= 3:
                for i in range(0, len(r)-2):
                    requested_tokens.append(r[i]+r[i+1]+r[i+2])
        current = self.three_gram_index.get(requested_tokens[0])
        for i in range(1, len(requested_tokens)):
            if current:
                current = self.boolean_and(current, self.three_gram_index.get(requested_tokens[i]))
            else:
                return False
        print("Here's what we found for your request:\n")
        if current:
            for word in current:
                print(word+'\n')
                for n in self.inverted_index.get(word):
                    print('\t'+self.files.get(n)+'\n')




    @staticmethod
    def boolean_and(one, two):
        res = []
        for word in one:
            if word in two:
               res.append(word)
        for word in two:
            if word in one and word not in res:
                res.append(word)
        if len(res) < 1:
            return False
        return res


