from distutils.ccompiler import new_compiler
from phonebook import Phonebook

new_list = Phonebook()
new_list.add("Clark", "1234")

new_dict = {}

new_dict["Clark"] = "1234"
new_dict["Scott"] = "1234"
new_dict["Clark"] = "1234"
new_dict["Clark"] = "1234"

print(new_dict)

#print(new_list.lookup("Clark"))


