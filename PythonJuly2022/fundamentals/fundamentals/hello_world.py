from collections import abc
from sre_constants import _NamedIntConstant


print("Hello World!")

name="Nico"
print(name)

print("hello " + name)

number=(11)
print("hello ", number)
print("Hello " + str(number))
print("Hello " + name)

fave_food1="BBQ"
fave_food2="Salads"
print(f"Iove to eat {fave_food2}")
print("I love to eat {}{}.".format(fave_food1, fave_food2))
print("I love to eat{}{}.".format(fave_food2, fave_food1))

x = "Hello Python"
print(x)
y = 42
print(y)

print("Hello World!{name}.".format("I like to eat"(fave_food1)(fave_food2)))


abc