import requests
import csv

def column(answer):
    answer.writerow(['ID', 'Фамилия', 'Имя', 'Пол', 'Дата рождения', 'Место деятельности', 'Религия'])
def getInfo(answer):
    main_method = 'https://api.vk.com/method/users.search'
    parameters = {'access_token': '81e8ea058f6c032498db196aee439ca94eb47e1908c80b53768119744dc9ad9d4190f20e2a0046a82561e3282b512',
        'count': 500, 'country': 1, 'city': 4658, 'fields': 'bdate, last_name, first_name, sex, occupation, personal'}
    users = requests.get(main_method, params=parameters)
    data = users.json()

    for i in range(1, len(data['response'])):
        if data['response'][i]['sex'] is not None:
            if data['response'][i]['sex'] == 1:
                gender = 'female'
            else:
                gender = 'male'
        if data["response"][i].get('bdate') is not None:
            bd = data["response"][i].get("bdate")
        if data['response'][i].get('occupation') is not None:
            uni = data['response'][i]['occupation']['name']
        if data['response'][i].get('occupation') is None:
            uni = ''
        if data['response'][i].get('personal') is not None:
            if type(data['response'][i].get('personal')) is dict:
                for key, value in data['response'][i].get('personal').items():
                    if key == 'religion':
                        belief = value
        if data['response'][i].get('personal') is None:
            belief = ''


        socioling = (data['response'][i]['uid'], data['response'][i]['last_name'], data['response'][i]['first_name'], gender, bd, uni, belief)
        answer.writerow(socioling)

        accaunt = data['response'][i]['uid']
        getPosts = requests.get('https://api.vk.com/method/wall.get', params={'owner_id': accaunt, 'count': 100, 'filter': 'owner'})
        wallPosts = getPosts.json()

        try:
            for wall in wallPosts['response'][1:]:
                wall['text'] = wall['text'].replace('<br>', '\n')
                if len(wall['text']) > 1:
                    with open('corpora/wall_' + str(accaunt) + '.txt', 'a', encoding='utf-8') as f_out:
                        f_out.write(wall['text'] + '\n')
        except:
            pass


def main():
    answerFile = open('vk_table.csv', 'w', encoding='utf-8')
    answer = csv.writer(answerFile, delimiter="\t", quotechar='', quoting=csv.QUOTE_NONE)
    column(answer)
    getInfo(answer)
if __name__ == '__main__':
    main()