porog = float(input())
n = int(input())
j = n
cnt = 0
emergency = 0
res = []
for i in range(n):
    notes = str(input())
    if notes == "error":
        cnt += 1
        j -= 1
        continue
    else:
        notes = float(notes)
        res.append(notes)
    if notes > porog:
        emergency += 1

print(n)
print(cnt)
print(emergency)
print(float(f'{max(res):.1f}'))
print(float(f'{sum(res)/j:.1f}'))
