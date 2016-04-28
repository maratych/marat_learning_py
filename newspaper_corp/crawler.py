import urllib.request
import re

import lxml.html as lh
initial_url = 'http://ulanmedia.ru/'
urls=[]
urls.append(initial_url)

def extract_links(url):
    try:
        content = urllib.request.urlopen(url).read().decode('utf-8')
    except UnicodeDecodeError:
        return([],'')
    except urllib.error.HTTPError:
        return([],'')
    except urllib.error.URLError:
        return([],'')
    except UnicodeEncodeError:
        return([],'')
    tree = lh.document_fromstring(content)
    #text = lh.tostring(tree)
    text = content
    
    links = tree.xpath('//a/@href')
        
    for i in range(len(links)):    
        if not links[i].startswith('http:'):
            links[i] = 'http://ulanmedia.ru' + links[i]
        links[i] = re.sub('#.*$','',links[i])
            
    links_good = []
    for i in links:
        
        if 'http://ulanmedia.ru' in i:
        #if not i.startswith('http://ulanmedia.ru'):
            
            #links.remove(i)
            links_good.append(i)

    return(links_good, text)
    
number_file = 0
table = open('table.csv','w')    
for i in urls:
    
    
    links, text = extract_links(i)
    if links != []:
        number_file += 1
        for n in links:
            if n not in urls:
                urls.append(n)
        file = open(str(number_file)+'.html','w', encoding = 'utf-8')
        file.write(text)
        file.close()
        table.write(str(number_file)+'.html'+'\t'+i+'\n')
    

table.close()

#links = re.findall('<a\shref="(.+?)"',content)


#f1 = open('main_page.txt','w') 
#f1.write(content) 

#for i in links:
    #new_content = urllib.request.urlopen(i).read().decode()
    #links2 = re.findall('<a\shref="(.|\S+)">',new_content)
    #for n in links2:
        #if n in links:
            #continue
        #else:
            #links.append(n)

#print(links)
##    #f2 = open('links.txt','w')
##    #f2.write(new_content)
##    #f2.close()
##
##f1.close()
