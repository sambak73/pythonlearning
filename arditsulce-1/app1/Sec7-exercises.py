'''
names = ["john smith", "jay santi", "eva kuki"]
title_names = [name.title() for name in names]
print(title_names)
'''
'''
usernames = ["john 1990", "alberta1970", "magnola2000"]
lengths = [len(username) for username in usernames]
print(lengths)
'''
'''
user_entries = ['10', '19.1', '20']
total = [float(entry) for entry in user_entries]
print(sum(total))
'''
temperatures = [10, 12, 14]
 
file = open("file.txt", 'w')
 
file.writelines(temperatures)
