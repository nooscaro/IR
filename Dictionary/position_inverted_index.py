    # position_inverted_index
    # Vera Baklanova (@nooscaro)
    # Applied Mathematics @ FI, NAUKMA-2020
    # https://github.com/nooscaro
    # 04/02/18
import re


class PositionInvertedIndex:

    def __init__(self, list_of_files):
        self.word_index = {}
        self.files = {}
        self.file_count = 0
        pattern = re.compile("[,\s\n\-\u2014!?:.;()\"]+")
        for f in list_of_files:
            file = open(f,"r")
            self.files.update({self.file_count: f})
            self.add_words_with_positions(file.read(),pattern, self.file_count)
            self.file_count += 1
            file.close()
        self.save_position_index()

    def save_position_index(self):
        index_file = open("Dictionary Output/position_index.txt","w+")
        for word in self.word_index.keys():
            index_file.write(word+'\n')
            index_file.write(self.files_by_indices(self.word_index.get(word)))
        index_file.close()

    def add_words_with_positions(self, text, regex, fileNo):
        tokens = re.split(regex,text)
        word_count = 0
        for w in tokens:
            word = w.upper()
            if word not in self.word_index:
                self.word_index.update({word: {}})
            if fileNo not in self.word_index.get(word).keys():
                self.word_index.get(word).update({fileNo: []})
            self.word_index.get(word).get(fileNo).append(word_count)
            word_count += 1

    def files_by_indices(self, list):
        res = ""
        for entry in list.keys():
            res += '\t'+self.files.get(entry)+":\n"
            for i in list.get(entry):
                res += '\t\t'+str(i)+'\n'
        return res

    def process_request(self):
        while True:
            req = input("Simple boolean AND search. Left to right, no parentheses allowed. Specify the k-distance"
                       " after your search request and we'll do"
                       "our best to find something for you. To stop CLI press 0"+'\n')
            if req == "0":
                return
            if len(req)>=1:

                dist = int(input("Distance: "))
                request = req.upper().split()
                current = self.word_index.get(request[0])
                for i in range(1,len(request)):
                    if not self.word(request[i]):
                        break
                    current = self.interception_with_distance(dist, current, self.word_index.get(request[i]))
                print("Here's what we've found for \""+req+"\":\n")
                if current is not None:
                    print(self.files_by_indices(current))

    def interception_with_distance(self, dist, dictOne, dictTwo):
        res = {}
        for i in range(0, self.file_count):
            if i in dictOne.keys() and i in dictTwo.keys():
                listOne = dictOne.get(i)
                listTwo = dictTwo.get(i)
                res.update({i:[]})
                for j in listOne:
                    for k in listTwo:
                        if abs(k-j) <= dist:
                            res.get(i).append((j, k))
                if len(res.get(i))==0:
                    res.pop(i)
        return res

    def word(self, str):
        return self.word_index.get(str) is not None
