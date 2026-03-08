piano_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

"""prints from 2 to 4"""
print(piano_keys[2:5])
"""prints from 2 to 4 and from 7 to 7"""
print(piano_keys[2:5],piano_keys[7:8])
"""prints from 2 to the end of the list"""
print(piano_keys[2:])
"""Prints from the beginning of the list to 4"""
print(piano_keys[:5])
"""Prints from 2 to 8 with an interval of 2"""
print(piano_keys[2:9:2])
"""Prints from the beginning of the list to 9 with an interval of 3"""
print(piano_keys[:9:3])
"""Prints every other items"""
print(piano_keys[::2])
"""Prints the reversed list"""
print(piano_keys[::-1])
"""Prints every other items in the reversed list"""
print(piano_keys[::-2])

piano_keys_tuple = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
"The same logic applies to tuples"
print(piano_keys_tuple[2:5])

