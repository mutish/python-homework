class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return "Test a:%s b:%s" % (self.a, self.b)

	def __str__(self):
		return "From str method of Test: a is %s," \
			"b is %s" % (self.a, self.b)

# Driver Code
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()



class myclass:
	x = 5
p1 = myclass()
print(p1.x)

class People:
	def __init__(abc, name, age):
		abc.name = name
		abc.age = age

	def myfunc(self):
		print("hello my name is" + " " + self.name)
p2 = People("Stacey", "18")
p2.myfunc()






class Person:
	def __init__(self, fname, lname,age,gender):
		self.fname = fname
		self.lname = lname
		self.age = age
		self.gender = gender
	def printname(self):
		print("hello" + " " +  self.lname, self.fname + " "  + "to Kenyatta University")

student1 = Person("Ann", "Wangui","18", "female")
student1.printname()


# mytuple = ("Ariana Grande", "Selena Gomez", "3")
# it = iter(mytuple)
# print(next(it))
# print(next(it))
# print(next(it))
# for x in mytuple:
# 	print(x)
#
# class myNumbers:
# 	def __iter__(self):
# 		self.a = 1
# 		return self
# 	def __next__(self):
# 		if self.a <= 20:
# 		   x = self.a
# 		   self.a += 1
# 		return x
# else:
# raise StopIteration
# myclass = myNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
# 	print(x)
a = 12

try:
	print(a)
except:
	print("something went wrong")
else:
	print("nothing went wrong")
finally:
	print("try except process is complete")

b = -1
if b < 0:
	raise Exception("sorry, no numbers below zero")







