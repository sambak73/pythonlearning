'''
contents = ["This is doc content", "This is pdf content", "This is text file content"]

filenames  = ["doc.txt", "pdf.txt", "text.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"arditsulce-1/app1/{filename}", "w")
    file.write(content)
    file.close()
'''
'''
file=open("arditsulce-1/app1/essay.txt", "r")
essay = file.read()
essay = essay.title()
print(essay)   
'''
'''
file=open("arditsulce-1/app1/essay.txt", "r")
essay = file.read()
num_of_chars = len(essay)
print(num_of_chars)  
'''
'''
new_member = input("Enter new member name:") + "\n"
file = open("arditsulce-1/app1/members.txt", "r")
file_contents = file.readlines()
file.close()

file_contents.append(new_member)

file = open("arditsulce-1/app1/members.txt", "w")
file.writelines(file_contents)
file.close()
'''
tranposed = []
matrix = [[1,2,3,4],[4,5,6,8]]
for i in range(len(matrix[0])):
    #print(i)
    transposed_row = []
    for row in matrix:
        #print(i)
        print(row[i])  
        transposed_row.append(row[i])
        print(transposed_row)
    tranposed.append(transposed_row)    
    print(tranposed)