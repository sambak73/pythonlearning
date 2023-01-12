import json
'''
print(Questions)
print(f'First item in the 1st list index is {Questions[0]["Question"]}')
print(f'second item in the 1st list index are {Questions[0]["Options"]}')
print(f'Third item in the 1st list index is  {Questions[0]["Correct_answer"]}')
'''
user_answer = {}
with open('arditsulce-1/app1/questions.json','r') as file:
    content = file.read()
Questions = json.loads(content)
print(Questions)    
for i,q in enumerate(Questions):
    print('{}.{}\n'.format(str(i+1),q["Question"]))
    for j,opt in enumerate(q["Options"]):
        print('     {}.{}\n'.format(str(j+1),opt))
    user_input = input(f"Enter the answer for {q['Question']}")
    user_answer[f"{q['Question']}"] = user_input
user_answer_list = list(user_answer.items())
user_result = {}
for i,(item) in enumerate(Questions):
    #print(i)
    if str(item["Correct_answer"]) == user_answer_list[i][1]:
        user_result[item["Question"]] = "Correct"
    else:
        user_result[item["Question"]] = "Wrong" 
results = list(user_result.items())
           
for i,(q,a) in enumerate(results):
    print('     {}.{} is {}\n'.format(str(i+1),str(q),str(a)))