n = int(input("enter a number of elements:"))
sequence = []
for i in range(n):
    num = int(input(f"enter integer {i + 1}:"))
    sequence.append(num)

ascending = True
descending = True

for i in range (1, n):
    if sequence[i] <= sequence[i - 1]:
        ascending = False
    if sequence[i] >= sequence[i - 1]:
        descendingcending = False
if ascending:
    print("ascending sequence")
elif descending:
    print("descending sequence")
else:
    print("none of them")
