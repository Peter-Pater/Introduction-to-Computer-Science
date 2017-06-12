import pickle

class Index:
    def __init__(self, name):
        self.name = name
        self.msgs = [];
        self.index = {}
        self.total_msgs = 0
        self.total_words = 0

    def get_total_words(self):
        return self.total_words

    def get_msg_size(self):
        return self.total_msgs

    def get_msg(self, n):
        return self.msgs[n]

    # implement
    def add_msg(self, m):
        self.msgs.append(m)
        self.total_msgs += 1
        return

    def add_msg_and_index(self, m):
        self.add_msg(m)
        line_at = self.total_msgs - 1
        self.indexing(m, line_at)

    # implement
    def indexing(self, m, l):
        list_msg = m.split()
        self.index[l] = list_msg
        return

    #implement: query interface

    def search(self, term):
        msgs = []
        punc = ['','.', ',', ':', ';', "'", '"','?', '/']
        append = False
        #coping with the problems with punctuations
        if ' ' not in term:
            for puncs in punc:
                term_adjust = term + puncs
                for keys in self.index:
                    if term_adjust in self.index[keys]:
                        msgs.append((keys,' '.join(self.index[keys])))
            msgs.sort()
        elif ' ' in term:
            # print('you searched for a phrase!')
            for puncs in punc:
                term_adjust = term + puncs
                term_list = term_adjust.split()
                for keys in self.index:
                    if term_list[0] in self.index[keys]:
                        i = 0
                        idx1 = self.index[keys].index(term_list[0])
                        for item in term_list:
                            try:
                                if item == self.index[keys][idx1 + i]:
                                    append = True
                                else:
                                    append = False
                                    break
                            except:
                                append = False
                                break
                            i = i + 1
                        if append == True:
                            msgs.append((keys,' '.join(self.index[keys])))
                        else:
                            pass
        #The problem with duplicates didn't appear for me in the firt place,
        #and I guess the trick is to search line by line instead of word by word?
        return msgs



class PIndex(Index):
    def __init__(self, name):
        super().__init__(name)
        roman_int_f = open('roman.txt.pk', 'rb')
        self.int2roman = pickle.load(roman_int_f)
        roman_int_f.close()
        self.load_poems()
        #print(self.int2roman)

        # Implement: 1) open the file for reading, then call
        # the base class's add_msg_and_index
    def load_poems(self):
        lines = open(self.name, 'r').readlines()
        for l in lines:
            self.add_msg_and_index(l)
        #print(self.index)
        return

        # Implement: p is an integer, get_poem(1) returns a list,
        # each item is one line of the 1st sonnet
    def get_poem(self, p):
        poem = []
        p_roman_starts = self.int2roman[p] + '.'
        p_roman_ends = self.int2roman[p + 1] + '.'
        index_start = self.search(p_roman_starts)
        index_end = self.search(p_roman_ends)
        for i in range(index_start[0][0],index_end[0][0]):
            poem.append(' '.join(self.index[i]))
        return poem

if __name__ == "__main__":
    # The next three lines are just for testing
    # You are encouraged to add to this and create your own tests!
    # Call your functions as you implement them and see if they work
    sonnets = PIndex("AllSonnets.txt")
    p3 = sonnets.get_poem(3)
    s_love = sonnets.search("love")
    s_search1 = sonnets.search('five')
    s_search2 = sonnets.search('five hundred')
    s_search3 = sonnets.search('For as the sun is daily new and old')
    print(s_love, '\n')
    print(s_search1, '\n')
    print(s_search2, '\n')
    print(s_search3, '\n')
    # my_idx = Index('hahaha')
    # my_idx.add_msg_and_index("what is the thing")
    # my_idx.add_msg_and_index("who knows who?")

