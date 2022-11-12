# TODO решить с помощью list comprehension и распечатать его

import pprint
dict_dict = []
for num in range(16):
    dict_dict.append({'bin': bin(num), 'dec': num, 'hex': hex(num), 'oct': oct(num)})

pprint.pprint(dict_dict)

