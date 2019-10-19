import re
import collections

text = open('book.txt').read().lower()
words = re.findall(r'\w+', text)
most_common_count = collections.Counter(words).most_common(10)
print(most_common_count) #convert this to a string before file output.
f = open('mostcommonwords.txt', 'w')

for word in most_common_count:
    section = word
    for couple in section:
        couple = str(couple) + "\n"
        f.write(couple)

# most_common_count = str(most_common_count).replace ('),', '),\n')
# f.writelines(str(most_common_count))
f.close()
