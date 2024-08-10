my_file = 'learning_python.txt'

with open(my_file) as f:
    lines = f.readlines()

for line in lines:
    line.rstrip()
    print(line.replace('Python', 'C'))