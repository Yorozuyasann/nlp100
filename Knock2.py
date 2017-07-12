import math

def q10():
    f = open('hightemp.txt','r')
    i = 0;
    for s in f:
        i += 1
    f.close()
    return i
def q11(text):
    text = text.replace("\t"," ",10)
    return text

def q12():
    f = open('hightemp.txt','r')
    fw = open('col1.txt','w')
    fw2 = open('col2.txt','w')
    fw.write(f.readline())
    fw2.write(f.readline())
    f.close()
    fw.close()
    fw2.close()

def q13():
    f = open('col1.txt','r')
    f2 = open('col2.txt', 'r')
    fw = open('col3.txt','w')
    fw.write(f.readline().replace("\n","") + "\t" +f2.readline())
    f.close()
    f2.close()
    fw.close()

def q15(N):
    f = open('hightemp.txt','r')
    s = f.readlines()
    for i in range(len(s)-1,len(s)-1-N,-1):
        print(s[i])
    f.close()

def q14(N):
    f = open('hightemp.txt','r')
    for i in range(0,N):
        print(f.readline())
    f.close()

def q16(N):
    f = open('hightemp.txt', 'r')
    s = f.readlines()
    size = int(len(s) / N)
    for i in range(0,len(s),size):
        for j in range(i,i+size):
            print(s[j])
        print("**************************")
    f.close()

def q17():
    f = open('hightemp.txt', 'r')
    for line in f:
        print(set([line.split("\t")[0]]))
    f.close()

def q18():
    f = open('hightemp.txt', 'r')
    lines = [line.split("\t") for line in f]
    print(lines)
    for line in sorted(lines,key=lambda x:float(x[2]),reverse=True):
        print("\t".join(line), end="")
    f.close()

def q19():
    f = open('hightemp.txt', 'r')
    lines = [line.split("\t") for line in f]
    words = {}
    for i in range(0,len(lines)):
        if(lines[i][0] in words):
            words[lines[i][0]] += 1
        else:
            words[lines[i][0]] = 1
    for line in sorted(words.items(), key=lambda x: float(x[1]), reverse=True):
        print(line, end="")
    f.close()


#print(q10())
#print("hello\tworld")
#print(q11("hello\tworld"))
#q12()
#q13()
#q14(2)
#q15(3)
#q16(5)
#q17()
#q18()
q19()