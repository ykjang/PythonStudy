__author__ = 'yg.jang'

import nester
import pickle


new_man = []


try:

    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File Error:' + str(err))
except pickle.PickleError as perr:
    print('Picking Error: ' + str(perr))


nester.print_lol(new_man)







