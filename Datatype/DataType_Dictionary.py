# Dictionary: ប្រើសម្រាប store the value ជា key, pairs។ វាជាប្រភេទ ordered, changeable តែមិនអនុញ្ញាត្តឱ្យមាន duplicate key។
# វាត្រូវបានប្រើសម្រាប់ store data ដែលមាន structure ជា key-value pairs។
# វាត្រូវបានបង្កើតដោយប្រើ curly braces {} និង key-value pairs ដែលត្រូវបានបំបែកដោយ colon (:)


# example of dictionary
dictionary_example = {
    'name': 'phon sobon',
    'age': 22,
    'city': 'Phnom Penh',
    'is_student': True,
    'courses': ['Python', 'JavaScript', 'Java'],
    'address': {
        'street': '123 Main St',
        'zip_code': '12345'
    }
}

# Accessing items in a dictionary
print("Name:", dictionary_example['name'])

a = dictionary_example.keys()
b = dictionary_example.values()
c = dictionary_example.items()

print("Keys:", list(a))
print(b)

dictionary_example.update({'country': 'Cambodia'})
print("Updated Dictionary:", dictionary_example)
# Removing an item from a dictionary
dictionary_example.pop('age')
print("Dictionary after removing 'age':", dictionary_example)