book_name = 'The Lord of The Rings Trilogy'.split()

print(book_name)

# The line below is an idiom for copying lists
lotr = book_name[:]
print(book_name[:3])
print(book_name[3:])
print(book_name[::-1])
print('lotr is book_name: ' + str(lotr is book_name))
print('lotr == book_name: ' + str(lotr == book_name))
