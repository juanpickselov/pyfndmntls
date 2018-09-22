book_name = 'The Lord of The Rings Trilogy'.split()

# The line below is an idiom for copying lists
lotr = book_name[:]

tolkien_text = list(book_name)
middle_earth = book_name.copy()

print(book_name)
print(book_name[:3])
print(book_name[3:])
print(book_name[::-1])
print('lotr is book_name: ' + str(lotr is book_name))
print('lotr == book_name: ' + str(lotr == book_name))
print('tolkien_text is book_name: ' + str(tolkien_text is book_name))
print('tolkien_text == book_name: ' + str(tolkien_text == book_name))
print('middle_earth is book_name: ' + str(middle_earth is book_name))
print('middle_earth == book_name: ' + str(middle_earth == book_name))
