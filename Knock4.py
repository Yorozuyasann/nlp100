import MeCab
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import collections

def neko_mecab():
    f = open('neko.txt','r')
    fw = open('neko.txt.mecab','w')
    m = MeCab.Tagger('-d /usr/lib/mecab/dic/mecab-ipadic-neologd')
    for txt in f:
        fw.write(m.parse(txt))
    f.close()
    fw.close()

def q30():
    f = open('neko.txt.mecab','r')
    maps = [[]]
    map = []
    m = {}
    i = 0
    for txt in f:
        if txt != 'EOS\n':
            sentences = txt.replace('\t',',').split(',')
            #print(sentences)
            m['surface'] = sentences[0]
            m['base'] = sentences[7]
            m['pos'] = sentences[1]
            m['pos1'] = sentences[2]
            map.append(m)
            m = {}
        else:
            maps.append(map)
            map = []
    return maps

def q31():
    maps = q30()
    for map in maps:
        for m in map:
            if m['pos'] == '動詞':
                print(m['surface'])


def q32():
    maps = q30()
    for map in maps:
        for m in map:
            if m['pos'] == '動詞':
                print(m['base'])


def q33():
    maps = q30()
    for map in maps:
        for m in map:
            if m['pos'] == '名詞' and m['pos1'] == 'サ変接続':
                print(m['surface'])

def q34():
    maps = q30()
    for map in maps:
        for i in range(len(map)-2):
            if map[i]['pos'] == '名詞' and map[i+1]['surface'] == 'の' and map[i+2]['pos'] == '名詞':
                print(map[i]['surface'] + map[i+1]['surface'] + map[i+2]['surface'])

def q35():
    maps = q30()
    a = ''
    max_len = 0
    for map in maps:
        for i in range(len(map)):
            j = 0
            b = ''
            if map[i]['pos'] == '名詞':
                j = i+1
                b = map[i]['surface']
                while j != len(map) and map[j]['pos'] == '名詞':
                    b += map[j]['surface']
                    j += 1

                if (j-i) > max_len:
                    max_len = j
                    print(max_len)
                    a = b

    print (a)

def q36():
    maps = q30()
    exist = {}
    for map in maps:
        for m in map:
            if not m['base'] in exist:
                exist[m['base']] = 1
            else:
                exist[m['base']] = exist[m['base']]+1
    dict_sorted = collections.OrderedDict()
    for key, value in sorted(exist.items(), key=lambda x: -x[1]):
        #print(str(key) + ":" + str(value))
        dict_sorted[key] = value

    return dict_sorted

def q37():
    dict = q36()
    fp = '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
    nt_prop = FontProperties(fname=fp)
    matplotlib.rcParams['font.family'] = nt_prop.get_name()

    keys = []
    values = []
    left = []
    i = 0
    for key in dict:
        left.append(i)
        i += 1
        keys.append(key)
        values.append(dict[key])
    plt.title('出現頻度TOP10')
    plt.bar([0,1,2,3,4,5,6,7,8,9],values[0:10])
    plt.xticks([0,1,2,3,4,5,6,7,8,9],keys[0:10])
    plt.show()

def q38():
    dict = q36()
    fp = '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
    nt_prop = FontProperties(fname=fp)
    matplotlib.rcParams['font.family'] = nt_prop.get_name()

    x = []
    y = []
    left = []
    i = 0
    j = 1
    for key in dict:
        if j != dict[key]:
            x.append(i)
            y.append(dict[key])
            j = dict[key]
        else:
            i += 1
    plt.title('ヒストグラム')
    plt.bar(x,y,width=3)
    #plt.xticks(left,keys[0:10])
    plt.show()

def q39():
    dict = q36()
    fp = '/usr/share/fonts/truetype/takao-gothic/TakaoGothic.ttf'
    nt_prop = FontProperties(fname=fp)
    matplotlib.rcParams['font.family'] = nt_prop.get_name()

    left = []
    values = []
    i = 0
    for key in dict:
        left.append(i)
        i += 1
        values.append(dict[key])
    plt.title('Zipfの法則')
    plt.plot(left,values)
    plt.xscale('log')
    plt.yscale('log')
    plt.show()


q39()