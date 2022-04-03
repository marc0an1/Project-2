import math

print("How many people are eating today?: ")
num_people = int(input())
print("How many hot dogs are you going to give per person?: ")
num_hd_per_person = int(input())

total_hot_dogs = num_people * num_hd_per_person

num_hot_dogs_packages = math.ceil(total_hot_dogs / 10)
num_hot_dogs_packages_leftovers = (num_hot_dogs_packages*10) - total_hot_dogs
num_hot_dogs_buns_packages = math.ceil(total_hot_dogs/8)
num_hot_dogs_buns_packages_leftovers = (num_hot_dogs_buns_packages*8) - total_hot_dogs


print("You have to buy", num_hot_dogs_packages, "packages of hot dogs")
print(num_hot_dogs_packages_leftovers, "hot dogs would be leftovers")
print("You have to buy", num_hot_dogs_buns_packages, "packages of hot dogs buns")
print(num_hot_dogs_buns_packages_leftovers, "hot dogs buns would be leftovers")
