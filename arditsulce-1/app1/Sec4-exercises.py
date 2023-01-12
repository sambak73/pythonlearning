'''
user_input_amount = int(input("How many dollars you got?"))
euro_amount = user_input_amount * 0.95
print(euro_amount)
'''
'''
while True:
    ranking = ['John', 'Sen', 'Lisa']
    print("The rankings are:")
    for rank in ranking:
        print(rank)
    user_input = int(input("Enter the rank to display person name:"))
    user_input = user_input - 1
    print(ranking[user_input])
    '''
'''    
ranking = ['John', 'Sen', 'Lisa']
print("The rankings are:")
for rank in ranking:
    print(rank)
user_input = input("Enter the person name to find our ranking:")
user_input = user_input.title()
for rank in ranking:
    rank = rank.title()
    print (rank)
    if rank == user_input:
        print(ranking.index(rank))
        #break
'''
'''
myList = ["one","two","3","4","five.",".six"] 
for i in range(len(myList)):
    myList[i] = myList[i].replace(".", "",1)    
print(myList)
myList.remove("two") 
print(myList)
myList.pop(1)
print(myList)
myList.clear()
print(myList)      
'''

myList = ["one","two","three"]
for index,item in list(enumerate(myList)):
    print(index+1,".",item)
    