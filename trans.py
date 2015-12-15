letters= dict(ა='ɑ',ბ='b',გ='g',დ='d',ე='ɛ',ვ='v',ზ='z',თ='tʰ',ი='ɪ',კ='kʼ',ლ='l',მ='m',ნ='n',ო='ɔ',პ='pʼ',ჟ='ʒ',რ='r',ს='s',ტ='tʼ',ჳ='wi',უ='u',ფ='pʰ',ქ='kʰ',ღ='ʁ',ყ='qʼ',შ='ʃ',ჩ='tʃ',ც='ts',ძ='dz',წ='tsʼ',ჭ='tʃʼ',ხ='χ',ჴ='q',ჯ='dʒ',ჰ='h')

f = open('anthem.txt','r',encoding='utf-8')
text = f.read()
for letter in text:
    if letter in letters:
        text = text.replace(letter, letters[letter])

text1 = open('anthem1.txt','w',encoding='utf-8')
text1.write(text)


f.close()
text1.close()

