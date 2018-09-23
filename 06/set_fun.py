alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_to_set = set(alphabet)
phrase = 'the quick red fox jumps over the lazy brown dog'
phrase_to_set = set(''.join(phrase.split()))
print(phrase_to_set == alphabet_to_set)
print(sorted(alphabet_to_set))
print(sorted(phrase_to_set))
print(alphabet_to_set.issubset(phrase_to_set))
