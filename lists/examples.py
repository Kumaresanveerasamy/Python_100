name = " this is a sentence"
list = name.split()
print(list)

numbers= [1,2,3,4]
new_numbers= [n+1 for n in numbers]
print(new_numbers)

name = "kumaresan"
new_name = [ letter for letter in name]
print(new_name)

doubles= [2*n for n in range(1,5)]
print(doubles)