for i in range(1,5):
    task = int(input(f"write down a daily task{i} "))
with open("diary.txt", 'w') as file:
    file.write(f"{task}")
with open("diary.txt", 'r') as file:
    content = file.read() 
    print(content)