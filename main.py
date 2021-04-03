import nltk
from nltk.corpus import stopwords

def func() :
    res = []
    string = input("What is your name ? Where do you live?\t(example : I am XYZ. I live in Srinagar) \n").lower()
    
    stop = stopwords.words('english')
    document = []
    for i in string.split() :
        if i not in stop:
            document.append(i)
    document = " ".join(document)
    sentences = nltk.sent_tokenize(document)

    name_word = nltk.word_tokenize(sentences[0].title())
    name = []
    for i in nltk.pos_tag(name_word) :
        if(i[1] == 'NNP') :
            name.append(i[0])
    name = " ".join(name)
    res.append(name)

    addr_word = nltk.word_tokenize(sentences[1].title())
    addr = []
    for i in nltk.pos_tag(addr_word) :
        if(i[1] == 'NNP') :
            addr.append(i[0])
    addr = " ".join(addr)
    res.append(addr)

    return res
