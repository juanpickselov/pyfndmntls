book_name = 'The Lord of The Rings Trilogy'.split()

print(book_name)

# The line below is an idiom for copying lists
lotr = book_name[:]
print(lotr is book_name)
print(lotr == book_name)
