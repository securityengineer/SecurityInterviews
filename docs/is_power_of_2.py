def is_power_of_2(number):
	binary = bin(number)
	there_has_been_a_1 = False
	for i in binary:
		if i == '1':
			if there_has_been_a_1:
				return False
			there_has_been_a_1 = True
	return there_has_been_a_1


assert True == is_power_of_2(2)
assert True == is_power_of_2(4)
assert True == is_power_of_2(8)
assert True == is_power_of_2(1)
assert False == is_power_of_2(7)
