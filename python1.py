#!/usr/local/bin/python3.6

a = 7
print(type(a))
a = float(a)
print(type(a))
a = str(a)
print(type(a))

print(int(True))	# Transfer data type

print('Na'*4 + '\n')

name = 'Henny'
print(name)
name = name.replace('H', 'P')
print(name)
print(name.replace('n', 'r'))

todos = 'get gloves,get mask,give cat vitamins,call ambulance'
split = todos.split(',')
print(split)
print(','.join(split))

words = "Henry is a handsome man"
print(words, "starts with Henry", words.startswith("Henry"))
print(words, "ends with man", words.endswith("man"))
print(words, "find Henry", words.find("Henry"))
print(words, "find #1 handsome array", words.find("handsome"))
print(words, "find #-1 handsome array", words.rfind("handsome"))
print(words, "appear handsome count", words.count("handsome"))
print(words, "are there any #", words.isalnum())

# List []: changable
list1 = ['a', 'b', 'c']
list2 = list('abc')	# Data transformation
print(type(list1))
print(list1)
print(list2)

# Tuple (): nonchangable
tuple1 = ('ab', 'cd', 'ef')
print(type(tuple1))
print(tuple1, "is a tuple")
print(list(tuple1), "is a list")

# dict {}: can use dict() to transfer either list or tuple
dict1 = {"1": "a", "2": "b", "3": "c"}
print(dict1)


splitme = "a/b//c/d///e"
print(splitme, splitme.split('/'))

# list operation1: extend += append insert
mares = ["Groucho", "Chico", "Harpo", "Zeppo"]
others = ["Gummo", "Karl"]
mares.extend(others)
print("extend: ", mares)
mares += others
print("+=: ", mares)
mares.append(others)
print("append: ", mares)
mares.insert(3, 'Gummo')
print("insert: ", mares)

# lis operation2: del remove pop
del mares[-1]
print("after del: ", mares)
mares.remove("Gummo")
print("after remove Gummo: ", mares)
mares.pop()
print("after pop: ", mares)

# list operation3: index in count join sort len copy
print("Chico" in mares)
print("Count Karl", mares.count("Karl"))

# Tuple operation1
a, b, c = tuple1
print("Tuple assiagn: ", a, b, c)

# Dict operation1: update del clear in
print(dict1)
print(dict1["1"])
others = {"4": "z", "5": "y"}
dict1.update(others)
print("after update dict1 from others: ", dict1)

print("Keys: ", list(dict1.keys()))
print("Values: ", list(dict1.values()))
print("(Keys, Values) with lsit: ", list(dict1.items()))
print("back to dict: ", dict(list(dict1.items())))

# range(start: stop: step) usage
print(list(range(0, 2)))

# def
def is_none(thing):
	if thing is None:
		print("It's None")
	elif thing:
		print("It's True")
	else:
		print("It's False")

is_none(None)
is_none(True)
is_none(False)
is_none([])

# def with function
def sum_args(*args):
	return sum(args)

def run_with_positional_args(func, *args):
	return func(*args)

print(run_with_positional_args(sum_args, 1,2,3,4))





