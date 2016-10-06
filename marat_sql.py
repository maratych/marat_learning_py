import mysql.connector, csv
sql = mysql.connector.connect(host ='localhost', user='guest1', passwd='n76Je4=wx6H')

with open('vk_table.csv', encoding='utf-8') as table:
    reader = csv.reader(table, delimiter='\t')
    cursor = sql.cursor()
    db = """create database guest1_mnyakubov"""
    cursor.execute(db)
    change_db = """use guest1_mnyakubov"""
    cursor.execute(change_db)
    table = """create table vk_people (
               ID varchar(15),
               last_name varchar(25),
               first_name varchar(25),
               sex varchar(6),
               date_of_birth varchar(11),
               location varchar(100),
               religion varchar(50))"""
    cursor.execute(table)
    query = ("insert into vk_people (ID, last_name, first_name, sex, date_of_birth, location, religion) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    for row in reader:
        user = tuple(row)
        cursor.execute(query, user)
        sql.commit()
    sql.close()