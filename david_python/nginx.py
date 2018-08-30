f = open("access.20180814.log",encoding="utf-8")
f2 = open("mm.log","w",encoding="utf-8")
for item in f:
	ip = item.split("-")[0].strip()
	f2.writelines(ip+"\n")