# Members of the group:Paul Moturayo Adunola, Adenike Babalola, Ark Ifeanyi, Akingbasote Mary, Blessing Ademola,
# Deborah Adetayo Adedigba.


"""import of the text file"""
div = open("C:/Users/adedi_tpk1ys1/OneDrive/Documents/PYTHON/Project/divine_freedom.txt")
def extract_country(top):
    divine = top.read()
    """striping and splitting of the divine data to ease accessibility"""
    line = divine.strip()
    words = line.split()
    word_lst = []
    word_dict = {}
    """extraction of the country code from the separated words"""
    for word in words:
        if word.startswith('('):
            word_lst.append(word[1:])
    """counting of the country codes and inserting values in a dictionary"""
    for country_code in word_lst:
        if country_code == '':
            continue
        word_dict[country_code] = word_dict.get(country_code, 0) + 1
    return word_dict

free_dict = extract_country(div)
"""Answer 1"""
print(free_dict)

import urllib.request as request
import json
"""import of the json file"""
with request.urlopen(
        'https://pkgstore.datahub.io/core/country-list/data_json/data/8c458f2d15d9f2119654b29ede6e45b8/data_json.json') as response:
    if response.getcode() == 200:
        source = response.read()
        country_name = json.loads(source)
    else:
        print('An error occurred while attempting to retrieve data from the API.')
"""converting the json data into one single dictionary"""
def country_code(dic):
    code_dict = {}
    for i in country_name:
        for k in i:
            code_dict[i["Code"]] = i["Name"]
    """assigning the values of the two dictionaries to each other"""
    trans_dict = {}
    for j in dic:
        for key in code_dict:
            if j == key:
                trans_dict[code_dict[key]] = dic[j]
    """reordering the dictionary to return in a descending order"""
    import operator
    res = dict(sorted(trans_dict.items(), key=operator.itemgetter(1), reverse=True))
    """returning the top 20 countries"""
    top_country = dict(list(res.items())[:20])
    return top_country

"""Answer 2"""
print (country_code(free_dict))

"creating a bar chart of country name and count"
import matplotlib.pyplot as plt
data = country_code(free_dict)
x = list(data.keys())
values = data.values()
plt.bar(x, values, tick_label=x)
plt.xlabel('Countries', fontsize=15)
plt.xticks(fontsize=10, rotation='vertical')
plt.ylabel('Counts', fontsize=15)
plt.title('Country Code and Count')
"""Answer 3"""
plt.show()

"""import of the text file for Q4"""
fhandle = open("C:/Users/adedi_tpk1ys1/OneDrive/Documents/PYTHON/Project/network_type.txt")
net_type = fhandle.read()
lines = net_type.rstrip()
networks = lines.split()
network_dictio = {}

"""creating a dictionary of the network types with their counts"""
for network in networks:
    network_dictio[network] = network_dictio.get(network, 0) + 1

"creating a bar chart of network type and count"
data1 = dict(sorted(network_dictio.items(), key = lambda y: y[1], reverse=True))
x_values = list(data1.keys())
y_values = data1.values()
plt.bar(x_values, y_values, tick_label=x_values)
plt.xlabel('Networks', fontsize=15)
plt.xticks(fontsize=10, rotation='vertical')
plt.ylabel('Counts', fontsize=15)
plt.title('Networks Vs Count')
"""Answer 4"""
plt.show()

"""Calling defined functions to solve Q5"""
with open("C:/Users/adedi_tpk1ys1/OneDrive/Documents/PYTHON/Project/showers.txt") as bottom:
    cont_dic = (extract_country(bottom))
answer5 = (country_code(cont_dic))
"""Answer 5"""
print(answer5)