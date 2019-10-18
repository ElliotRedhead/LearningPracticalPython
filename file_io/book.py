import re
import collections

text = open('book.txt').read().lower()
words = re.findall(r'\w+', text)
most_common_count = collections.Counter(words).most_common(10)
most_common_count #convert this to a string first.
f = open('mostcommonwords.txt', 'a')
f.writelines(most_common_count)
f.close()
