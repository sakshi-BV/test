#converting json str into python object
import json
x = '2457'
print(type(x))
y=json.loads(x)
print(type(y))
print(y)

#converting python object into json str
x = 2457
print(type(x))
y=json.dumps(x)
print(type(y))
print(y)

#convert list into json str
x = ['sakshi','ashish','krushal']
print(type(x))
y=json.dumps(x)
print(type(y))
print(y)

