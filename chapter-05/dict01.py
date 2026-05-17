#empty dict
empty = {}

#dict with data
data = {"name": "German",
        "age": 26,
        "city": "Cherkasy"}

print(data["name"])
print(data["age"])

data["email"] = "kyperu07@gmail.com"
print(data["email"])

del data["city"]

if "city" in data:
    print("city is in data")
    del data["city"]
else :
    print("city is not in data")

data["second_name"] = "Gritsenko"
print(data.get("second_name"))
print(data.get("country"))

print(data.keys())
#print(data.values() & data.keys())
print(data.items())

data.update({"city": "Kyiv"})
print(data.items())

age = data.pop("age")
print(age)


for key in data:
    print(key)

for value in data.values():
    print(value)


for key, value in data.items():
    print(key, value)