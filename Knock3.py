
import json
import re
import urllib.request

def getJson():
    jawiki = []
    for line in open('jawiki-country.json','r'):
        jawiki.append(json.loads(line))
    return jawiki

def q20():
    json_ja = getJson()

    for j in json_ja:
        if j['title'] == 'イギリス':
            print(str(j['text']))

def q21():
    json_ja = getJson()
    pattern = re.compile('^\[\[Category:.*\]\]$')
    for j in json_ja:
        if j['title'] == 'イギリス':
            lines = j['text'].split("\n")
            #print(lines)
            for line in lines:
                if pattern.match(line):
                    print(line)

def q22():
    json_ja = getJson()
    pattern = re.compile('^\[\[Category:.*\]\]$')
    for j in json_ja:
        if j['title'] == 'イギリス':
            lines = j['text'].split("\n")
            for line in lines:
                if pattern.match(line):
                    print(line[11:-2])

def q23():
    json_ja = getJson()
    pattern = re.compile('^=+.*=+$')
    for j in json_ja:
        if j['title'] == 'イギリス':
            lines = j['text'].split("\n")
            for line in lines:
                if pattern.match(line):
                    print(line.replace("=","",10) + " : " + str(int(line.count("=")/2)))

def q24():
    json_ja = getJson()
    pattern = re.compile('^\[\[File:(.*?)\|')
    for j in json_ja:
        if j['title'] == 'イギリス':
            lines = j['text'].split('\n')
            for line in lines:
                if pattern.match(line):
                    print(pattern.search(line).group(0).replace('[[File:','',100)[0:-1])

def q25():
    json_ja = getJson()
    pattern = re.compile('^\|.+ = .+$')
    for j in json_ja:
        if j['title'] == 'イギリス':
            line = j['text'].replace('\n','',1000)
            #print(line)
            #for line in lines:
            print(pattern.search(line).group(0))

def q26():
    json_ja = getJson()
    pattern = re.compile('^\|.+ = .+$')
    dict = {}
    for j in json_ja:
        if j['title'] == 'イギリス':
            lines = j['text'].split('\n')
            #line = j['text'].replace('\n', '', 1000)
            #print(line)
            for line in lines:
                if pattern.match(line):
                    ls = line.split(' = ')
                    dict[ls[0][1:]] = ls[1]
            #print(dict)
    return dict

def q27():
    dict = q26()
    pattern = re.compile('')
    for temp in dict:
        dict[temp] = dict[temp].replace("'''","").replace("''","")
        #print(temp + ":" + dict[temp])
    return dict

def q28():
    dict = q27()
    pattern = re.compile("\[\[.+?\]\]")
    pattern2 = re.compile("\[\[(?P<first>.*)\|(?P<second>.*)\]\]")

    for temp in dict:
        if pattern.search(dict[temp]):
            #print(pattern.search(dict[temp]).group(0))
            if pattern2.search(dict[temp]):
                p_dict = pattern2.search(dict[temp]).groupdict()
                dict[temp] = dict[temp].replace(pattern2.search(dict[temp]).group(0),p_dict['second'])
            dict[temp] = dict[temp].replace("[[","").replace("]]","")
        #print(temp + ":" +dict[temp])
    return dict

def q29():
    dict = q28()
    p = re.compile("\{\{(?P<value>.*)\}\}.+?")
    p2 = re.compile("(?P<sentence>.*)<ref(.*?)>.*</ref>")
    p3 = re.compile("(?P<sentence>.*)<ref(.+?)/>")
    for temp in dict:
        if p.search(dict[temp]):
            dict[temp] = p.search(dict[temp]).groupdict()['value']

        if p2.search(dict[temp]):
            dict[temp] = p2.search(dict[temp]).groupdict()['sentence']
        if p3.search(dict[temp]):
            dict[temp] = p3.search(dict[temp]).groupdict()['sentence']
        #print(temp +":"+dict[temp])
    return dict

def q29_2():
    dict = q29()
    url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:'+dict['国旗画像'].replace(' ','%20')+'&format=json&prop=imageinfo&iiprop=url'
    #url = 'https://www.mediawiki.org/w/api.php?action=query&titles=File:Test.jpg&prop=imageinfo&iilimit=50&iiend=2007-12-31T23:59:59Z&iiprop=timestamp%7Cuser%7Curl'

    request = urllib.request.Request(url)
    con = urllib.request.urlopen(request)
    lines = str(con.read())
    pattern = re.compile('{"url":"(?P<value>.+?)"')
    if pattern.search(lines):
        print(pattern.search(lines).groupdict()['value'])



#q20()
q29_2()