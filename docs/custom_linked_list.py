'''
Create a linked list that supported add and remove.
Numbers are added in ascending order, so if the list
	was 1,3,5 and 4 was added it would look like 1,3,4,5.
'''
class custom_linked_list:
	def __init__(self):
		self.custom_list = []

	def add(self, number):
		if len(self.custom_list) == 0:
			self.custom_list.append(number)
			return
		for i, n in enumerate(self.custom_list):
			if n >= number:
				self.custom_list.insert(i, number)
				return
		self.custom_list.append(number)

	def remove(self, number):
		if len(self.custom_list) == 0:
			raise
		for i, n in enumerate(self.custom_list):
			if n == number:
				del self.custom_list[i]
				return

cll = custom_linked_list()
cll.add(4)
cll.add(9)
cll.add(1)
cll.add(7)
cll.add(0)
assert cll.custom_list == [0, 1, 4, 7, 9]
cll.remove(4)
assert cll.custom_list == [0, 1, 7, 9]
