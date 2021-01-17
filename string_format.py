name = "Eric"
age = 74

print("Hello, %s." % name)
print("Hello, %s. You are %s." % (name, age))

print("--------------------------------------------------")

print("Hello, {}. You are {}.".format(name, age))
print("Hello, {1}. You are {0}.".format(age, name))

print("--------------------------------------------------")

person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(
    name=person['name'], age=person['age']))

print("--------------------------------------------------")

print("Hello, {name}. You are {age}.".format(**person))

print("----------------- F-STRINGS ---------------------")

print(f"Hello, {name}. You are {age}.")

print("----------------- F-STRINGS ---------------------")

print(f"{2 * 37}")


def to_lowercase(input):
    return input.lower()


name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.")
