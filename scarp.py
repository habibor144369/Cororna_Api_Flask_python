# All countries data here -----
import requests
from bs4 import BeautifulSoup


def webScrap():
    res = requests.get('https://www.worldometers.info/coronavirus/')
    if res.status_code != 200:
        return {'message': 'server error!'}

    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.table
    heading = table.thead.tr.find_all('th')
    data = []
    text = []
    for i in heading:
        text.append(i.text)
    data.append(text)

    # # for loop and inline for loop there are same !
    # text = [i.text for i in heading]
    # data.append(text)

    tableRow = table.find_all('tr')
    for row in tableRow:
        td = row.find_all('td')
        check = False

        list = [
           'World', 'USA', 'India', 'Brazil', 'Russia', 'France', 'UK', 'Turkey', 'Italy', 'Spain', 'Argentina', 'Colombia',
           'Germany', 'Mexico', 'Poland', 'Iran', 'Peru', 'Ukraine', 'South Africa', 'Indonesia', 'Netherlands', '	Belgium',
           'Czechia', 'Iraq', 'Chile', 'Romania', 'Bangladesh', 'Canada', 'Philippines', 'Pakistan', 'Morocco', 'Switzerland'
        ]

        for j in td:
            if j.text in list:
                check = True
        if check:
            item = [i.text for i in td]
            data.append(item)


    res = {'data': []}
    for i in range(1, 32):
        temp = {}
        for j in range(len(data[i])):
            if data[i][j] == '':
                data[i][j] = 0
            temp[data[0][j]] = data[i][j]
        res['data'].append(temp)
    return res



##################################################################
# Particular countries data here -------only World and Bangladesh corona data here--
# import requests
# from bs4 import BeautifulSoup
#
# def webScrap():
#     res = requests.get('https://www.worldometers.info/coronavirus/')
#     if res.status_code != 200:
#         return {'message': 'server error!'}
#
#     soup = BeautifulSoup(res.text, 'html.parser')
#     table = soup.table
#     heading = table.thead.tr.find_all('th')
#     data = []
#     text = []
#     for i in heading:
#         text.append(i.text)
#     data.append(text)
#
#     # # for loop and inline for loop there are same !
#     # text = [i.text for i in heading]
#     # data.append(text)
#
#     tableRow = table.find_all('tr')
#     for row in tableRow:
#         td = row.find_all('td')
#         check = False
#         for j in td:
#             if j.text == 'Bangladesh' or j.text == 'World':
#                 check = True
#         if check:
#             item = [i.text for i in td]
#             data.append(item)
#
#
#     res = {'data': []}
#     for i in range(1, 4):
#         temp = {}
#         for j in range(len(data[i])):
#             if data[i][j] == '':
#                 data[i][j] = 0
#             temp[data[0][j]] = data[i][j]
#         res['data'].append(temp)
#     return res
#

