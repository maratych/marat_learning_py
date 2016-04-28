# -*- coding: utf-8 -*-

import os
import sys 
import lxml.html as lh
import csv
import datetime
import re 

def file_structure(year, month):
    
    plain = 'corp_text\\' + year + '\\' + month
    plain_mystem = 'corp_plain_mystem\\' + year + '\\' + month
    xml_mystem = 'corp_xml_mystem\\\\' + year + '\\' + month
    if not os.path.exists(plain):
        os.makedirs(plain, exist_ok = True)
    if not os.path.exists(plain_mystem):
        os.makedirs(plain_mystem, exist_ok = True)
    if not os.path.exists(xml_mystem):
        os.makedirs(xml_mystem, exist_ok = True)
    return(plain, plain_mystem, xml_mystem)
     
    

meta_table = open('meta_table.csv', 'w', encoding='utf-8')
field_names = ['path', 'author', 'sex', 'birthday', 'header', 'created', 'sphere', 'genre_fi', 'type', 'topic', 'chronotop', 'style', 'audience_age', 'audience_level', 'audience_size', 'source', 'publication', 'publisher', 'publ_year', 'medium', 'country', 'region', 'language']
writer = csv.DictWriter(meta_table, field_names, restval='', extrasaction='raise', delimiter='\t', lineterminator='\n')
writer.writeheader()

text1 = open('text_','a',encoding='utf-8')

with open('table.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t', quotechar = '"')
    for row in reader:
        filename = row[0]
        url = row[1]
        
        with open(filename, encoding = 'utf-8') as htmlfile:
            htmlfile_str = htmlfile.read()
            tree = lh.document_fromstring(htmlfile_str)
            header = tree.xpath('//title')            
            header = header[0].text_content().strip()
            dict_table = {}
            try:
                date = re.search('http://ulanmedia.ru/.+?/.+?/(\d\d.\d\d.\d\d\d\d)/',url).group(1)
            except AttributeError:
                date = 'не указана'
            topic = tree.xpath("//ul[@class='nav navbar-sub']/li[@class='active']")
            try:
                topic = topic[0].text_content().strip()
            except IndexError:
                topic = 'не указана'
            try:
                publ_year = re.search('http://ulanmedia.ru/.+?/.+?/\d\d.\d\d.(\d\d\d\d)/',url).group(1)
            except AttributeError:
                publ_year = 'не указана'
            dict_table['path'] = filename
            dict_table['author'] = "не указан"
            dict_table['header'] = header
            dict_table['created'] = date
            dict_table['sphere'] = 'публицистика'
            dict_table['topic'] = topic
            dict_table['style'] = 'нейтральный'
            dict_table['audience_age'] = 'н-возраст'
            dict_table['audience_level'] = 'н-уровень'
            dict_table['audience_size'] = 'городская'
            dict_table['source'] = url
            dict_table['publication'] = 'UlanMedia.ru'
            dict_table['publ_year'] = publ_year
            dict_table['medium'] = 'Интернет-издание'
            dict_table['country'] = 'Россия'
            dict_table['region'] = 'республика Бурятия'
            dict_table['language'] = 'ru'
            
            
            text = tree.xpath("//div[@class='page-content']")
            try:
                text = text[0].text_content().strip()
            except IndexError:
                text = ''
            
            try:
                month = re.search('http://ulanmedia.ru/.+?/.+?/\d\d.(\d\d).\d\d\d\d/',url).group(1)
                plain, plain_mystem, xml_mystem = file_structure(publ_year, month)
                if text != '':
                    plain_path = plain + '\\' + filename + '.txt'
                    text2 = open(plain_path,'w',encoding = 'utf-8')
                    text2.write(text)
                    
                    text2.close()
                    command_plain = 'C:\\Users\\marat\\mystem.exe -cid ' + plain_path + ' ' + plain_mystem + '\\' + filename + '.txt'
                    command_xml = "C:\\Users\\marat\\mystem.exe -cid --format xml " + plain_path + ' ' + xml_mystem + '\\' + filename + '.txt'
                    print(command_xml)
                    os.system(command_plain)
                    os.system(command_xml)
                    text2 = open(plain_path,'w',encoding = 'utf-8')
                    text2.write('@au Noname\n@ti ' + header +'\n@da ' + date +'\n@topic ' + topic + '\n@url ' + url + '\n\n' + text)
                    
                    text2.close()
                    writer.writerow(dict_table)
            except AttributeError:
                pass
            
            
meta_table.close()
            
        