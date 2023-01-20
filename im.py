import random
print("create a list of random integers")
population=range(0,100)
num_list=random.sample(population,10)
print(num_list)
no_elements=4
print("randomly select",no_elements,"multiple item from the said list")
result_elements=random.sample(num_list,no_elements)
print(result_elements)
no_elements=8
print("randomly select elements")
result_elements=random.sample(num_list,no_elements)
print(result_elements)