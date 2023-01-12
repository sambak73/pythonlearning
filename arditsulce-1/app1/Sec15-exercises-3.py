import json
with open('arditsulce-1/app1/questions.json','r') as file:
    content = file.read()
Questions = json.loads(content)
print(Questions)    
score = 0
for i,q in enumerate(Questions):
    print('{}.{}\n'.format(str(i+1),q["Question"]))
    for j,opt in enumerate(q["Options"]):
        print('     {}.{}\n'.format(str(j+1),opt))
    user_input = int(input(f"Enter the answer for {q['Question']}"))
    q["user_answer"] = user_input
    if q["user_answer"] == q["Correct_answer"]:
        score += 1
print(f"You scored {score} out of {len(Questions)} ")
  