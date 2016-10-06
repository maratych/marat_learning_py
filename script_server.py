import urllib.request

url = 'http://lenta.ru'
a = urllib.request.Request(url, headers = {'UserAgent' : 'name'})
response = urllib.request.urlopen(a)
page = response.read().decode('utf-8')

text_file = open('server_file.html','w', encoding = 'utf-8')
text_file.write(page)

