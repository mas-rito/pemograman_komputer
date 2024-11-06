with open('data.txt', 'r') as file:
    print(file.read())

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

with open('data.txt', 'r') as file:
    line = file.readline().strip()
    while line != '':
        print(line)
        line = file.readline().strip()

with open('data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

with open('output.txt', 'w') as file:
    file.write("Hello World!")

with open('output.txt', 'w') as file:
    lines_to_write = ["Line One", "Line Two"]
    file.writelines(lines_to_write)
