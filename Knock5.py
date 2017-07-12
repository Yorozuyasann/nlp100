import CaboCha
import re
from graphviz import Digraph

class Morph:
    def __init__(self):
        self.surface = ""
        self.base = ""
        self.pos = ""
        self.pos1 = ""
    def __repr__(self):
        return self.surface
        #return self.surface + "\t" + self.pos + ',' + self.pos1 + ','+ self.base

class Chunk():
    def __init__(self):
        self.id = 0
        self.morphs = []
        self.dst = -1
        self.srcs = []
    def __repr__(self):
        return '%s,dst:%s,src:%s' % (self.morphs,self.dst,self.srcs)

    def __str__(self):
        text = ''
        for m in self.morphs:
             text+=m.surface
        return text

    def PosList(self):
        poss = []
        for m in self.morphs:
            poss.append(m.pos)
        return poss


def make_neko():
    c = CaboCha.Parser()
    f = open('neko.txt','r')
    fw = open('neko.txt.cabocha','w')
    for line in f:
        fw.write(c.parse(line).toString(CaboCha.CABOCHA_FORMAT_LATTICE))
        #print(c.parse(line).toString(CaboCha.CABOCHA_FORMAT_LATTICE))
    f.close()
    fw.close()


def q40():
    f = open('/Files/neko.txt.cabocha','r')
    sentence = []
    sentences = []
    for line in f:
        if line != 'EOS\n':
            if line[0] != '*':
                morph = Morph()
                words = line.replace('\t',',').split(',')
                #print(words)
                morph.surface = words[0]
                morph.pos = words[1]
                morph.pos1 = words[2]
                morph.base = words[7]
                sentence.append(morph)
        else:
            sentences.append(sentence)
            sentence = []
    for m in sentences[3]:
        print(m)
    f.close()

def q41():
    f = open('./Files/neko.txt.cabocha','r')
    sentences = []
    c_list = []
    c = Chunk()
    pattarn = re.compile('(?P<send>.*)D')
    for line in f:
        if line == 'EOS\n':
            #print(c_list)
            for list in c_list:
                if list.dst != -1:
                    c_list[list.dst].srcs.append(list.id)
            sentences.append(c_list)
            #print(sentences)
            c_list = []
        elif line[0] == '*':
            c = Chunk()
            cs = line.split(' ')
            c.id = int(cs[1])
            if pattarn.search(cs[2]):
                tosend = int(pattarn.search(cs[2]).groupdict()['send'])
                c.dst = tosend
            #print(c)
            c_list.append(c)
            #print(c_list)
        else:
            morph = Morph()
            words = line.replace('\t',',').split(',')
            morph.surface = words[0]
            morph.pos = words[1]
            morph.pos1 = words[2]
            morph.base = words[7]
            #print(morph)
            c.morphs.append(morph)
    f.close()
    #print(sentences[7])
    return sentences

def q42():
    sentences = q41()
    with open('pair.txt','w') as fw:
        for sentence in sentences:
            for chunk in sentence:
                if len(chunk.srcs) != 0:
                    text = str(chunk).replace('、','').replace('。','').replace('「','').replace('」','') + ":"
                    for src in chunk.srcs:
                        if str(sentence[src]) != '　':
                            text += str(sentence[src]).replace('、','').replace('。','').replace('「','').replace('」','') + "\t"
                    fw.write(text[0:-1].replace('　','')+'\n')

def q43():
    sentences = q41()
    with open('pair_verb.txt','w') as fw:
        for sentence in sentences:
            for chunk in sentence:
                if len(chunk.srcs) != 0 and '動詞' in chunk.PosList():
                    text = str(chunk)+ ":"
                    i = 0
                    for src in chunk.srcs:
                        if str(sentence[src]) != '　' and '名詞' in sentence[src].PosList():
                            text += str(sentence[src]) + "\t"
                            i = 1
                    if i == 1:
                        fw.write(text[0:-1].replace('、','').replace('。','').replace('「','').replace('」','') .replace('　','')+'\n')

def q44():
    sentences = q41()
    sentence = sentences[7]
    print(sentence)
    g = Digraph(format='png')
    g.attr('node',shape='circle')
    for c in sentence:
        g.node(str(c),str(c))
    for c in sentence:
        if c.dst != -1:
            g.edge(str(c),str(sentence[c.dst]))
    print(g)
    g.render('graph')

def q45():
    sentences = q41()
    with open('./Files/pattern.txt','w') as fw:
        for sentence in sentences:
            for chunk in sentence:
                if '動詞' in chunk.PosList():
                    joshi = []
                    text = ''
                    flug = 0
                    for morph in chunk.morphs:
                        if morph.pos == '動詞':
                            text += morph.base + "\t"
                            break
                    for src in chunk.srcs:
                        if '助詞' in sentence[src].PosList():
                            flug = 1

                            for j in sentence[src].morphs:
                                if j.pos == '助詞':
                                    joshi.append(j.surface)
                    if flug == 1:
                        #print(joshi)
                        if len(joshi) > 1:
                            sorted(joshi)
                            text += joshi[0]
                            for i in range(1,len(joshi)):
                                text += " " + joshi[i]
                        else:
                            text += ' '+joshi[0]
                        fw.write(text + '\n')

def q46():
    sentences = q41()
    with open('./Files/pattern2.txt','w') as fw:
        for sentence in sentences:
            for chunk in sentence:
                if '動詞' in chunk.PosList():
                    joshi = []
                    text = ''
                    flug = 0
                    for morph in chunk.morphs:
                        if morph.pos == '動詞':
                            text += morph.base + "\t"
                            break
                    for src in chunk.srcs:
                        joshis = []
                        if '助詞' in sentence[src].PosList():
                            flug = 1

                            for j in sentence[src].morphs:
                                if j.pos == '助詞':
                                    joshis.append(j.surface)
                                    joshis.append(str(sentence[src]).replace('　',''))
                            joshi.append(joshis)
                    if flug == 1:
                        #print(joshi)
                        if len(joshi[0]) > 1:
                            sorted(joshi)
                            #print(joshi)
                            text += joshi[0][0]
                            for i in range(1,len(joshi)):
                                text += " " + joshi[i][0]
                            text += '\t' + joshi[0][1]
                            for i in range(1, len(joshi)):
                                text += " " + joshi[i][1]
                        else:
                            text += ' '+joshi[0][0] + '\t' + joshi[0][1]
                        fw.write(text + '\n')

def q47():
    sentences = q41()
    with open('./Files/pattern3.txt', 'w') as fw:
        for document in sentences:
            for chunk in document:
                text = ''
                if '動詞' in chunk.PosList() and len(chunk.srcs) > 1:
                    if chunk.id - document[chunk.srcs[-1]].id == 1:
                        flug = 0
                        for m in document[chunk.srcs[-1]].morphs:
                            if m.pos == '名詞' and m.pos1 == 'サ変接続':
                                flug = 1
                            if flug == 1 and m.base == 'を':
                                flug = 2
                                text += str(document[chunk.srcs[-1]]) + str(chunk) + '\t'
                                break
                        if flug == 2:
                            joshis = []
                            for i in range(len(chunk.srcs)-1):
                                src = chunk.srcs[i]
                                if '助詞' in document[src].PosList():
                                    joshi = []
                                    for m in document[src].morphs:
                                        if m.pos == '助詞':
                                            joshi.append(m.base)
                                            joshi.append(str(document[src]))
                                            joshis.append(joshi)
                                            break

                            for joshi in joshis:
                                text += joshi[0] + ' '
                            text += '\t'
                            for joshi in joshis:
                                text += joshi[1] + ' '
                            print(text)

q47()