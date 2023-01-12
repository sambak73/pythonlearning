import glob
import csv
import random
'''
data = glob.glob('arditsulce-1/app1/*.txt')
for dat in data:
    print(dat)
'''
with open('arditsulce-1/app1/weather.txt', 'r') as file:
    data = list(csv.reader(file))
#print(data)
'''
city = input("Enter city:")
city = city.strip()
city = city.title()
for row in data[1:]:
    if row[0] == city:
        print(row[1])
'''
'''
Questions = [
    {"Question 1": "What are Dolphins:"},{"Options:":["Fish","Bird","Mammals","Amphibians"]},{"Correct Answer": 3},
 {"Question 2": "How many colors are there in Rainbow:"},{"Options:":["7","5","1","9"]},{"Correct Answer": 1}
 ]
Q = ["First item","Second item","Third item"]
print(f"type of questions is {type(Questions)}")
print(f"type of questions is {type(Questions[0])}")
print(f"The first list item is {Questions[3]}")
print(Q[0])
'''
'''
Questions = {
    "Question1" : {
        "Question": "What are Dolphins",
        "Options": ["Fish","Bird","Mammals","Amphibians"],
        "Correct Answer": 3
    },
    "Question2" : {
        "Question": "Which is the smallest month of the year",
        "Options": ["January","Febuary","December","May"],
        "Correct Answer": 2
    },
    "Question3" : {
        "Question": "How many colors are there in Rainbow",
        "Options": ["7","1","9","5"],
        "Correct Answer": 1
    }
}
'''
'''
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


#print(Questions)
#print(Questions["Question1"]["Question"])
#print(type(Questions))

User1_Answer = {
    "Question1" : 2,
    "Question2" : 2,
    "Question3" : 1
}
User1_Results = {}
#answers = User1_Answer.values()
#print(f"The type of answers is {type(answers)}")

for item in Questions.items():
    #print(item)
    if item[1]["Correct Answer"] == User1_Answer[item[0]]:
        User1_Results[item[0]+ " : " +item[1]["Question"]] = "Correct"
    else:
        User1_Results[item[0]+" : "+item[1]["Question"]] = "Wrong" 
results = list(User1_Results.items())
#for item in results:
#    print(f"{item[0]} = {item[1]}")
#    #print(type(item))
           
for i,(q,a) in enumerate(results):
    print('     {}.{} is {}\n'.format(str(i+1),str(q),str(a)))
'''
lower_bound = int(input("Enter the lower bound value:"))
upper_bound = int(input("Enter the upper bound value:"))

generated_random_number = random.randint(lower_bound, upper_bound)
print(generated_random_number)


