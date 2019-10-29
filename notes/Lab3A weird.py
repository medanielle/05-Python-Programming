import random
my_dict = {}

print('Enter your answers to the following MAD LIBs or enter random')

my_dict = {'adj 1': input('Enter an adjective: '), 'adj 2': input('Enter an adjective: '),
'verb 1': input('Enter a verb (gerund): '), 'verb 2': input('Enter a verb (gerund): '), 
'noun 1': input('Enter a noun: '), 'noun 2': input('Enter a noun: ')}

adj_list = ['Happy','Sad','Mad']
noun_list = ['dog', 'cat', 'mouse']
verb_list = ['running', 'playing', 'golfing']

for x in my_dict.keys():
    if my_dict[x] == 'random':
        if 'adj' in str(x):
            my_dict[x] = random.choice(adj_list)
        elif 'noun' in str(x):
            my_dict[x] = random.choice(noun_list)
        elif 'verb' in str(x):
            my_dict[x] = random.choice(verb_list)
        else:
            print(f"This didn't work")

print("\nWe are {} a very {} {}.\n".format(my_dict['verb 1'], my_dict['adj 1'], my_dict['noun 1']))
print("\nWe are {} a very {} {}.\n".format(my_dict['verb 2'], my_dict['adj 2'], my_dict['noun 2']))