this_list = (123,'aurelija',[123,456])

this_list[2].append(789)

for item in this_list[2]:
    for char in str(item):
        print(char)
