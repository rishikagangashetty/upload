from collections import Counter

filename = ''
data_list = []

print("Select files that have to be read:-")
print("1. do.txt\n 2.something.txt\n 3.what.txt")
select_txt = int(input("Select: "))

if select_txt == 1:
    filename = 'do.txt'
elif select_txt == 2:
    filename = 'something.txt'
elif select_txt == 3:
    filename = 'what.txt'

f = open(filename, 'r', encoding='utf-8')
read_data = f.read()
data_list = read_data.split('\n')
data_list.pop()
# print(data_list)
f.close

n_value = int(input("\nSelect the value of TOP 'n' for the user '@theobserver': "))
n = str(n_value)

print("\nSelect any of the following:-")
print("1. The top "+n+" users who have tweeted the most for the entire timeline\n2. The top "+n+" users who have tweeted the most for every hour\n3. The top "+n+" users who have the maximum followers\n4. The top "+n+" tweets which have the maximum retweet count")
select_input = int(input("Select: "))

def splitwise(split_value):
    global n_value
    max_list_user_input = []
    max_list_user_input_temp = []
    max_list_user_input_fin = []
    max_object = {}

    max_list_user_input_all = []

    for i in data_list:
        max_list_user_input.append(i.split('*"'))
        
    if split_value == 1:
        ite = 0
        for i in max_list_user_input:
            max_list_user_input_temp.append(i[0].split(' '))
            max_list_user_input_fin.append(str(max_list_user_input_temp[ite][0]))
            ite += 1
        max_list_user_input_all = Counter(max_list_user_input_fin)
    elif split_value == 3 or split_value == 4:
        ite = 0
        for i in max_list_user_input:
            max_list_user_input_temp.append(i[0].split(' '))
            max_list_user_input_fin.append(i[2].split(' '))
            if split_value == 3:
                max_object.update({max_list_user_input_temp[ite][0] : int(max_list_user_input_fin[ite][1])})                       
            else:
                max_object.update({i[1] : int(max_list_user_input_fin[ite][2])})
            ite+=1
        max_list_user_input_all = Counter(max_object)
    get_max(max_list_user_input_all, n_value, split_value)

def get_max(list_list, max_val, s_value):
    if s_value == 1:
        print("\nThe top "+str(max_val)+" people who tweeted the most with the number of tweets are:")
        if max_val <= len(list_list):
            print(list_list.most_common(max_val))
        else:
            print("Out of boundary")
    elif s_value == 3 or s_value == 4:
        if max_val <= len(list_list):
            print("\nThe top "+str(max_val)+" are:")
            print(list_list.most_common(max_val))
        else:
            print("Out of boundary")

def maxFollowers(split_value):
    splitwise(split_value)

if select_input == 1:
    maxFollowers(1)
elif select_input == 2:
    maxFollowers(2)
elif select_input == 3:
    maxFollowers(3)
elif select_input == 4:
    maxFollowers(4)