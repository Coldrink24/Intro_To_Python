_aboutMe = {
    "Structural Languages": {
        "HTML": "Hyper Text Markup Language",
        "CSS": "Cascading Style Sheets",
    },
    "Spoken Language": {
        "ar": "Arabic",
        "en": "English"
    },
    "Hobbies": {
        1: "Reading",
        2: "Drawing",
        3: "Embroidering"
    },
    "Favourite Films": ("Invisible Guest", "Don't Worry,Darling", "Scream", "Divergent"),
    True: "I am Temperamental",
    False: "I am evil"
}

''' 
[0] Enclosed by {}, syntax: {key:value, key:value}
[1] Any immutable data Types, No lists
[2] Keys should be unique, values not
[3] Not indexed
'''
print(_aboutMe)

print(_aboutMe.keys())
print(_aboutMe.values())

print(_aboutMe["Structural Languages"])
print(_aboutMe["Hobbies"][1])

print(_aboutMe.get("Not Found Key"))
# Get VS [] : get won't print an error if the key
# doesn't exist, instead "None"

print(_aboutMe.update({"Extra": "I am unique"}))
_aboutMe.popitem()
print(_aboutMe.items())  # print as tuples
_aboutMe.setdefault(True, "You are better")  # add if doesn't exist

dic = _aboutMe.copy()  # shallow copy
dic1 = _aboutMe  # two references for the same thing





# 2d Dictionary - different way
One = {
        "Name": "HTML",
        "Progress": "80%"
    }
Two = {
         "Name": "CSS",
        "Progress": "70%"
}
Three = {
        "Name": "JS",
        "Progress": "60%"
    }

Lan2 = {
    1: One,
    2: Two,
    3: Three
}

