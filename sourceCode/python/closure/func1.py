#coding=utf-8

def dec(func):
	def in_dec(*arg):#my_sum -> dec.__closure__
		print ('in dec arg = ',arg)
		if len(arg)==0:
			return 0
		for val in arg:
			if not isinstance(val,int):
				return 0
		return func(*arg)
	print ('return in_dec')
	return in_dec

@dec#等价于my_sum = dec(my_sum)
def my_sum(*arg):
	return sum(arg)

def my_average(*arg):
	return sum(arg)/len(arg)

#my_sum = in_dex(*arg)
# my_sum = dec(my_sum)

print (my_sum(1,2,3,4,5))
print (my_sum(1,2,3,4,5,'6'))

# my_average = dec(my_average)
# print (my_average(1,2,3,4,5))
# print (my_average())