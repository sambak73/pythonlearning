Question1 = {
    "Question": "What are Dolphins",
    "Options": ["Fish","Bird","Mammals","Amphibians"],
    "Correct Answer": 3
}
Question2 = {
    "Question": "Which is the smallest month of the year",
    "Options": ["January","Febuary","December","May"],
    "Correct Answer": 2
}
Question3 = {
    "Question": "How many colors are there in Rainbow",
    "Options": ["7","1","9","5"],
    "Correct Answer": 1
}

Questions = {
    "Question1" : Question1,
    "Question2" : Question2,
    "Question3" : Question3 
}

questions = [[key,value] for key,value in Questions.items()]
#print(questions)
#print(type(questions))
#print(questions[2][1]["Question"])
user_answer = {}
for i,(item) in enumerate(questions):
    #print(item)
    print('{}.{}\n'.format(str(i+1),item[1]["Question"]))
    #print(questions[i][1]["Options"])
    #print(type(questions[i][1]["Options"]))
    for i,opt in enumerate(questions[i][1]["Options"]):
        print('     {}.{}\n'.format(str(i+1),opt))
    user_input = input(f"Enter the answer for {item[0]}:")
    user_answer[f"{item[0]}"] = user_input
user_answer_list = list(user_answer.items())
user_result = {}
for i,(item) in enumerate(questions):
    #print(i)
    if str(item[1]["Correct Answer"]) == user_answer_list[i][1]:
        user_result[item[0]+ " : " +item[1]["Question"]] = "Correct"
    else:
        user_result[item[0]+" : "+item[1]["Question"]] = "Wrong" 
results = list(user_result.items())
           
for i,(q,a) in enumerate(results):
    print('     {}.{} is {}\n'.format(str(i+1),str(q),str(a)))