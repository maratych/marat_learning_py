import urllib.request

url1 = 'http://lenta.ru/'
url2 = 'http://utro.ru/'
url3 = 'http://mail.ru/'

content1 = urllib.request.urlopen(url1).read().decode('utf-8')
file1 = open('lenta.html', 'w', encoding = 'utf-8')
file1.close()
content2 = urllib.request.urlopen(url2).read().decode('utf-8')
file2 = open('utro.html', 'w', encoding = 'utf-8')
file2.close()
content3 = urllib.request.urlopen(url3).read().decode('utf-8')
file3 = open('mail.html', 'w', encoding = 'utf-8')
file3.close()


