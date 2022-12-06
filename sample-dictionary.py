var_dict = {}

print(type(var_dict))

objs = {"fruit" : "grapes", "number" : "7"}

print(objs)

objs["food"] = "pizza"
objs[1] = 493

print(objs)

objs["food"] = "fish filet"
objs["Food"] = "fish filet" # these are different outputs
print(objs)

for k, v in objs.items(): # iterate over dictionary
    print(k,v)