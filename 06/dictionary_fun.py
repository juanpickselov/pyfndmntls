from collections import OrderedDict

urls = {'github':'https://github.com/juanpickselov/',
    'Pluralsight':'https://app.pluralsight.com/library/',
    'Developerworks':'https://developer.ibm.com'}

sorted_urls = OrderedDict(sorted(urls.items()))
print(urls['github'])
# below is worth looking into further
# note the sorting appeas to be case sensitive
print(sorted(urls, key=urls.__getitem__))
print(sorted_urls)