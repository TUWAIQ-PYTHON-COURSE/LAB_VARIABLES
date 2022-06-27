from cgi import print_form


my_team = "Liverpool"
print(my_team)
x = 10
y = 3.14
print(x, y)
x1 = x2 = x3 = 10
print(x1, x2, x3)
var1, var2 = 5, 8
print(var1, var2)
# print(yield(my_team))
def generator():

   yield "Welcome"

   yield "to"

   yield "Simplilearn"

gen_object = generator()

print(type(gen_object))
print(gen_object)