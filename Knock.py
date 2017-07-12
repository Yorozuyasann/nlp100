import random

def q1():
    str = "stressed"
    print(str[::-1])

def q2():
    str = "パタトクカシーー"
    print(str[0::2])

def q3():
    str1 = "パトカー"
    str2 = "タクシー"
    ans = ""
    for (s1,s2) in zip(str1,str2):
        ans += s1 + s2
    print(ans)

def q4():
    str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    strs = str.replace(",","",10).replace(".","",10).split(" ")
    list = []
    for s in strs:
        list.append(s[0])
    print(list)

def q5():
    str ="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    strs = str.split(" ")
    dict = {}
    for i in [1,5,6,7,8,9,15,16,19]:
        dict[i-1] = strs[i-1][0]
    for i in [2,3,4,10,11,12,13,14,17,18]:
        dict[i-1] = strs[i-1][:2]
    print(dict)

def q5(text,n):
    text = text.replace(" ","",100)
    ans = []
    for i in range(0,len(text),n):
        ans.append(text[i:i+n:])
    return ans

def q6():
    str = "paraparaparadise"
    str2 = "paragraph"
    str_bi = q5(str,2)
    str2_bi = q5(str2,2)
    str_set = set(str_bi)
    str2_set = set(str2_bi)
    list_seki = list(str_set & str2_set)
    list_wa = list(str_set | str2_set)
    list_sa = list(str_set ^ str2_set)
    print(list_wa)
    print(list_seki)
    print(list_sa)

def q7(x,y,z):
    return "%s時の%sは%s" % (x,y,z)

def cipher(text):
    ans = ""
    for s in text:
        if (ord(s)>=97 and ord(s) <= 122):
            #print(s + "-->" + chr(210-ord(s)))
            ans+=chr(210-ord(s))
        else:
            #print(s)
            ans+=s
    return ans

def q9(text):
    buf = text.split(" ")
    ans = "";
    for i in range(0,len(buf)):
        if(len(buf[i]) > 4):
            str2 = buf[i][1:len(buf[i])-1]
            str2 = random.sample(str2,len(str2))
            line2 = buf[i][0] + ''.join(str2) + buf[i][len(buf[i])-1]
            ans += line2 + " "
        else:
            ans += buf[i] + " "

    return ans

#q1()
#q2()
#q3()
#q4()
#q5("I am an NLPer",1)
#q5("I am an NLPer",2)
#q6()
print(q7(12,"気温",22.4))
print(cipher("sdfasdfa21321"))
ans = q9("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
print(ans)