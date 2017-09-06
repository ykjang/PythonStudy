__author__ = 'yg.jang'

import nester
import pickle

man = []
other = []

try:

    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            line_spoken = line_spoken.strip()
            # print('role:'+role)
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    data.close()
except IOError as err:
    print('The datafile is missing: ' + str(err))

# print(man)
# print(other)

try:
    # with open('man_data.txt', 'w') as man_file:
    #     nester.print_lol(man, False, 0, man_file)
    # with open('other_data.txt', 'w') as other_file:
    #     nester.print_lol(other, False, 0, other_file)

    with open('man_data.txt', 'wb') as man_file:
        pickle.dump(man, man_file)
    with open('other_data.txt', 'wb') as other_file:
        pickle.dump(other, other_file)

except IOError as err:
    print('File IO Error: ' + str(err))

except pickle.PickleError as perr:
    print("Pickling Error: " + str(perr))






