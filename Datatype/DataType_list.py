#List : គឺសម្រាប់ store collection of data ដែលអាចផ្លាស់ប្ដូរបាន។ បង្កើត list ដោយប្រើ square brackets ។
# - Ordered : វាតាមលំដាប់ទៅតាម្វីដែលយើងបានកំណត់តម្លៃនៅពេលដែលយើងបង្កើត។ ហើយបើយើង add តម្លែថ្មីចូលវានោ ចូលទៅខាងក្រោយ។
# - Allow duplicated : អាចមានតម្លៃជាន់គ្នាបាន
# - Changeable : អាច remove, add, update បាន។
# - Allow mixed data types : អាចមាន data type ផ្សេងៗគ្នា

# Example of list
my_list = [1, 2, 3, 4, 5, 3, 4, 5]
print("List:", my_list)
# Accessing items in a list
print("First item:", my_list[0])

my_list = ["apple", 1, "banana", 2.5, True]
print("Mixed data types in list:", my_list)
# Accessing items in a list with mixed data types
print("First item in mixed list:", my_list[0])
# Length of a list
print("Length of list:", len(my_list))


List = [1, 2, 3, 4, 5]
List.remove(4)
print("List after removing 4:", List)

mixed_data_list = ["apple", 1, "banana", 2.5, True]
mixed_data_list[1] = "orange"
mixed_data_list.append("grape")
mixed_data_list.remove(True)
print("Mixed data list after modification:", mixed_data_list)

# for remove item by index need to use del keyword
del mixed_data_list[1:3]
print(mixed_data_list)

mixed_data_list.insert(0, "watermelon")
print("Mixed data list after inserting watermelon:", mixed_data_list)
