f = open("add.txt",encoding="utf-8")
sum = 0 
for item in f:
	strCount = item.split(":")[-1]
	sum = sum + int(strCount)
print(sum)
