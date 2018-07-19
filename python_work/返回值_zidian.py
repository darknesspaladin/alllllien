def build_person(frist_name,last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
    person = {'frist':frist_name,'last':last_name}
    return person
person_name = build_person('men','daguang')
print(person_name)
