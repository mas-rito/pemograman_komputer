# with open('data.txt', 'w') as file:
#     file.write("Hello World!")

with open('data.txt', 'a') as file:
    array = ["data 1", "data 2", "data 3", "data 4", "data 5"]
    # file.writelines(array)
    for i in array:
        file.write(i + "\n")