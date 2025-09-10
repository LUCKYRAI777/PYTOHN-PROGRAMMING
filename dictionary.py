d={"eno":35, "Ename":"xyz"}
print(d["eno"])
print(d.get("Ename"))
d["Ename"] = "lucky"
print(d)
d["age"]=19
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for key,value in d.items():
    print(key,":",value)
d.pop("Ename")
print(d)
d.popitem()
print(d)
d.clear()
print(d)



