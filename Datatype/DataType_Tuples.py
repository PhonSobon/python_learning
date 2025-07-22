# Data type sequence
# Tuple: គឺសម្រាប់ store multiple item ក្នុងមួយ variable ឬក៏សម្រាប់ store the collections of data ។
# - Tuple item គឺ ordered ទៅតាមអ្វីដែលយើងបាន assigned ទៅក្នុង variable
# - Unchangeable: យើងមិនអាច remove or add item បន្ទាប់ពី tuple ត្រូវបានបង្កើត
# - Allow duplicates: tuple អាចឱ្យយើង store value ដូចគ្នាបាន


#example of tuple
# Tuple example
# A tuple is a collection of items that is ordered and unchangeable.
# Tuples are defined by enclosing the items in parentheses ().
# Example of a tuple
my_tuple = (1, 2, 3, 4, 5,3,4,5)
print("Tuple:", my_tuple)
# Accessing items in a tuple
print("First item:", my_tuple[0])

my_tuple = ("apple",1, "banana", 2.5, True)
print("Mixed data types in tuple:", my_tuple)
# Accessing items in a tuple with mixed data types
print("First item in mixed tuple:", my_tuple[0])
# Length of a tuple
print("Length of tuple:", len(my_tuple))
print(type(my_tuple))


