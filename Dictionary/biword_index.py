# biword_index
# in IR/Dictionary
# Constructs a biword index from a collection of documents
# Vera Baklanova (@nooscaro)
# Applied Mathematics @ FI, NAUKMA-2020
# https://github.com/nooscaro
# 04/02/18
import re

MIN_RESULT = 1
PROMPT = "Greetings! Welcome to biword index CLI. Simply type in your search request and we'll do our best to find something for you. To exit the CLI, press 0"

def parse_to_biword_tokens(str):
    tokens = re.split('\s+', str)
    if len(tokens) == 1:
        print("It seems rather odd that you would search for one word in a two-word index... Please don't do that again")
        return False
    res = []
    if len(tokens) == 2:
        res.append(tokens[0]+' '+tokens[1])
        return res
    for i in range(0, len(tokens) - 1):
        biword = tokens[i] + ' '+tokens[i + 1]
        res.append(biword)
    return res


def list_interception(l):
    if len(l) == 1:
        return l[0]
    current = l[0]
    for i in range(1,len(l)):
        current = boolean_and(current, l[i])
    if len(current) >= MIN_RESULT:
        return current
    return False


def list_union(l):
    if len(l)==1:
        return l[0]
    current = l[0]
    for i in range(0, len(l)):
        current = boolean_or(current, l[i])
    return current


def boolean_or(one, two):
    res = []
    for i in range(0, len(one)):
        if i in one or i in two:
            res.append(i)
    return res


def boolean_and(one, two):
    res = []
    for i in range(0,len(one)):
        if i in one and i in two:
            res.append(i)
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
            if self.file_count not in self.biword_index.get(biword_token):
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

    def get_biword_index(self, token):
        return self.biword_index.get(token)

    def process_request(self, request):
        requested_tokens = parse_to_biword_tokens(request)
        if not requested_tokens:
            return False
        biword_indices = []
        for token in requested_tokens:
            if self.get_biword_index(token) is not None:
                biword_indices.append(self.get_biword_index(token))
        intercept = list_interception(biword_indices)
        if intercept:
            return intercept
        return list_union(biword_indices)

    def request(self):
        while True:
            req = input(PROMPT)
            if req == "0":
                print("See ya soon")
                return
            res = self.process_request(req)
            if res:
                result = self.files_by_indices(res)
                print("Here's what we've found for \""+req+"\":")
                print(result)
            else:
                print("Unfortunately, there was nothing we could find")
