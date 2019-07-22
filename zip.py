a= [1,2,3,4,5]
names =['gaurav','garima','gajendra','sabitri','sagar']

new = list(zip(a,names))
print(new)

for letter,name in zip(a,names):
	print("{}: {}".format(letter,name))

nums, namess = zip(*new)
print(nums, namess)

for i, letter in enumerate(a):
	print(i,letter)