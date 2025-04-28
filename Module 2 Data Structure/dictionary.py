# my_dict = {
#     "Name" : "Girish",
#     "Age" : 22,
#     "City" : "Sirohi"
# }

# my_dict["email"] = "girish@123gmail.com"

# name = my_dict["Name"]
# age = my_dict["Age"]
# city = my_dict["City"]
# email = my_dict["email"]

# print(f"name : {name}")
# print(f"age : {age}")
# print(f"City : {city}")
# print(f"Email : {email}")

# print(my_dict)

my_dict = {
    "Name" : "Naresh",
    "Age" : 22,
    "City" : "Odisha"
}

keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
# print(keys)
# print(values)
# print(items)

for key, value in items:
    print(f"{key} : {value}")

# name = my_dict.get("Name")
# print(name)

# email = my_dict.get("email", "No Email Available")
# print(email)