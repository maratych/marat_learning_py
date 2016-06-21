import csv
new_table = open('new_table.csv', 'w',encoding='utf-8')
with open('source_post1950_wordcount.txt') as csvfile:
    reader = csv.reader(csvfile, delimiter = '\t', quotechar = '"')
    for row in reader:
        wordcount = row[-1]
        if wordcount != '':
            wordcount = int(row[-1])
            if wordcount < 80000:
                wordcount = str(wordcount)
                p1 = str(row[:-2] + list(';' + wordcount + '\n'))
                new_table.write(p1)
                wordcount = int(wordcount)
            if wordcount > 80000 and wordcount < 140000:
                new_count = wordcount/2
                new_count = str(new_count)
                p1 = str(row[0] + list('1' + ';') + row[1:-2] + list(';' + new_count + '\n'))
                p2 = str(row[0] + list('2' + ';') + row[1:-2] + list(';' + new_count + '\n'))
                new_table.write(p1)
                new_table.write(p2)
            if wordcount > 140000:

                 new_count = wordcount/3
                 new_count = str(new_count)
                 p1 = str(row[0] + list('1' + ';') + row[1:-2] + list(';' + new_count + '\n'))
                 p2 = str(row[0] + list('2' + ';') + row[1:-2] + list(';' + new_count + '\n'))
                 p3 = str(row[0] + list('3' + ';') + row[1:-2] + list(';' + new_count + '\n'))
                 new_table.write(p1)
                 new_table.write(p2)
                 new_table.write(p3)

csvfile.close()
new_table.close()


