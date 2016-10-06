import xml.etree.ElementTree as ETree
import re

tree = ETree.parse('stal.xml')
root = tree.getroot()
chi_text = []
for line in root.iter('se'):
    if 'lang' in line.attrib:
        continue
    chi_text.append(line.text)

dictionary = dict()
with open('cedict_ts.u8', 'r', encoding='utf-8') as chi:
    for word in chi:
        if word[0] == '#':
            continue
        word = word.split()
        dictionary[word[1]] = dictionary.get(word[1], []) + [' '.join(word[2:])]


def parse_Strings(sentence, dictionary):
    parsed = []
    word = ''
    for character in sentence:
        if character not in dictionary and len(character) == 1:
            if word != '':
                parsed.append((word, dictionary[word]))
                word = ''
            parsed.append(character)
        else:
            word += character
            if word not in dictionary:
                parsed.append((word[:-1], dictionary[word[:-1]]))
                word = word[-1]
    return parsed
    html = ETree.Element('html')

    head = ETree.SubElement(html, 'head')
    body = ETree.SubElement(html, 'body')
    se = ETree.SubElement(body, 'se')
    for i in parsed:
        if len(i) == 1:
            ETree.SubElement(se, None).tail = i
            continue
        w = ETree.SubElement(se, 'w')
        for j in i[1]:
            transcr = re.findall('^(\[[\w:\s]+\])', j)[0].strip('[]')
            sem = re.findall('(/.*/)', j)[0].strip('/')
            sem = sem.replace('/', ', ')
            ETree.SubElement(w, 'ana', lex=i[0], transcr=transcr, sem=sem)
        ETree.SubElement(w, None).text = i[0]

    ETree.ElementTree(html).write(filename, encoding='utf-8', xml_declaration=True, short_empty_elements=False)

sent_no = 1
html = ETree.Element('html')
ETree.SubElement(html, None).text = '\n'
head = ETree.SubElement(html, 'head')
ETree.SubElement(head, None).text = '\n'
ETree.SubElement(html, None).text = '\n'
body = ETree.SubElement(html, 'body')
ETree.SubElement(body, None).tail = '\n'
for j in chi_text:
    sentence = parse_Strings(j, dictionary)
    se = ETree.SubElement(body, 'se')
    ETree.SubElement(se, None).text = '\n'
    for i in sentence:
        if len(i) == 1:
            ETree.SubElement(se, None).tail = i
            continue
        w = ETree.SubElement(se, 'w')
        for j in i[1]:
            transcr = re.findall('^(\[[\w:\s]+\])', j)[0].strip('[]')
            sem = re.findall('(/.*/)', j)[0].strip('/')
            sem = sem.replace('/', ', ')
            ETree.SubElement(w, 'ana', lex=i[0], transcr=transcr, sem=sem)
        ETree.SubElement(se, None).tail = '\n'
        ETree.SubElement(w, None).text = i[0]
    sent_no += 1
ETree.SubElement(body, None).tail = '\n'
ETree.SubElement(html, None).tail = '\n'
ETree.ElementTree(html).write('chin.xml', encoding='utf-8', xml_declaration=True, short_empty_elements=False)