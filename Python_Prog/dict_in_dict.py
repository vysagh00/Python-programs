d = {"name":["vys","sk"],"followers":2000,"online":True,"id":{123:22}}

print(d["id"][123])

d["following"] = 920
print(d)

print(d["name"][1])

print(d["name"][1][:1])

print(d["name"][1]+hello)

d.update({"live":"off"})
print(d)

del d["name"][0]
print(d)

del d
print(d)

d.clear()
print(d)