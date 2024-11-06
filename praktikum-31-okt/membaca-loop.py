with open('data.txt', 'r') as file:
    content = file.read().splitlines()

    for line in content:
        print(line + '\n')