__author__ = 'yg.jang'

def sanitize(time_string):
    """
    분시간을 나타내는 문자열을 모두 '분.초' 형식로 변경

    :param time_string:  분을 나타내는 문자열
    :return:
    """

    if '-' in time_string:
        spliter = "-"
    elif ':' in time_string:
        spliter = ":"
    else:
        return(time_string)

    (mins, secs) = time_string.split(spliter)
    return(mins + '.' + secs)
##### sanitize function End

# with open('./records/james.txt', 'r') as james_file:
#     james = james_file.readline()
# james_list = james.strip().split(',')

# with open('./records/julie.txt', 'r') as julie_file:
#     julie = julie_file.readline()
# julie_list = julie.strip().split(',')
#
# with open('./records/mikey.txt', 'r') as mikey_file:
#     mikey = mikey_file.readline()
# mikey_list = mikey.strip().split(',')
#
# with open('./records/sarah.txt', 'r') as sarah_file:
#     sarah = sarah_file.readline()
# sarah_list = sarah.strip().split(',')


def makelistfromfile(filename):
    """
        파일명을 인자로 받아서 읽은후 ,를 구분자로 리스트객체로 만들어 반환하는 함수
    """
    try:
        with open(filename, 'r') as records_file:
            record_list = records_file.readline().strip().split(',')

        return record_list

    except IOError as err:
        print('IO Error: ' + str(err))
        return(None)
#

def make_unique(records):

    unique_list = []
    for each_record in records:
        if each_record not in unique_list:
            unique_list.append(each_record)

    return unique_list
### uniqueRecords End



james_list = makelistfromfile('./records/james.txt')
julie_list = makelistfromfile('./records/julie.txt')
mikey_list = makelistfromfile('./records/mikey.txt')
sarah_list = makelistfromfile('./records/sarah.txt')

# print(james_list)
# print(julie_list)
# print(mikey_list)

# 반복되는 for문 - 리스트의 값을 변환해 다른 리스트로 넣기 위해서
# for each_record in james_list:
#     new_james_list.append(sanitize(each_record))
#
# for each_record in james_list:
#     new_julie_list.append(sanitize(each_record))
#
# for each_record in james_list:
#     new_mikey_list.append(sanitize(each_record))
#
# for each_record in james_list:
#     new_sarah_list.append(sanitize(each_record))




# 지능형 리스트
# 기존 리스트의 각 데이터 항목에 변환을 적용해서 새로운 리스트를 만든다

# james_list = make_unique(sorted(sanitize(each_record) for each_record in james_list))
# julie_list = make_unique(sorted(sanitize(each_record) for each_record in julie_list))
# mikey_list = make_unique(sorted(sanitize(each_record) for each_record in mikey_list))
# sarah_list = make_unique(sorted(sanitize(each_record) for each_record in sarah_list))

james_list = sorted(set(sanitize(each_record) for each_record in james_list))[0:3]
julie_list = sorted(set(sanitize(each_record) for each_record in julie_list))[0:3]
mikey_list = sorted(set(sanitize(each_record) for each_record in mikey_list))[0:3]
sarah_list = sorted(set(sanitize(each_record) for each_record in sarah_list))[0:3]

print(james_list)
print(julie_list)
print(mikey_list)
print(sarah_list)
print('-------------------------------')

# print(sorted(new_james_list, reverse=True))

# 지능형 리스트 테스트
mins = [1,2,3]
sec = [(m*60) for m in mins]
print(sec)

lower = ["I", "don't", "like", "spam"]
upper = [low.upper() for low in lower]
print(upper)


dirty = ['2-42', '1:22', '5.22']
clean = sorted(float(s) for s in [sanitize(t) for t in dirty])
print(clean)