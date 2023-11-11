# list
mySong = ["do", "ri", "mi"]
i = 0
while i < len(mySong):  # the same in other langs
    print(mySong[i])
    i += 1
# tuple
myBFF = ("Youssef", "Aya", "Emy", "Yomna")
for i in myBFF:    # the same with foreach
    print(i * 2)

# set
myNum = {1, 2, 3, 4, 6}
for i in myNum:
    if i % 2 == 0 and not i == 2:
        print(i)
    else:
        print("5")

# string
myName = "Somaya"
for letter in myName:
    print(letter.upper())

# dict
mySkills = {
    "Embroidry": "80%",
    "Fast Reading": "50%"
}
for i in mySkills:
    print(i)  # print keys in mySkills
    print(mySkills[i])   # print values
    print(f"Then My progress in {i} is {mySkills[i]}")

# nested loops

Names = ["osama ", "youssef", "nasser"]
Skills = ["html", "css"]

for name in Names:
    print(f"{name} skills is: ")

    for skill in Skills:
        print(skill)

#  nested loops - advanced dictionary

peoples = {
    "Osama": {
        "HTML": "70%",
        "CSS": "80%",
        "JS": "20%"
    },
    "Ahmed": {
        "HTML": "70%",
        "CSS": "80%",
        "JS": "20%"
    },
    "Sayed": {
        "HTML": "70%",
        "CSS": "80%",
        "JS": "20%"
    }
}

#  first way to print
for people in peoples:
    print(f"In the group there is {people} and his skills are {peoples[people]}")

#  second way to print

for main_keys, main_values in peoples.items():
    print(f"In the group there is {main_keys}")
    print(f"& His skills are =>")

    for child_keys, child_values in main_values.items():
        print(f" {child_keys} with {child_values} progress")

