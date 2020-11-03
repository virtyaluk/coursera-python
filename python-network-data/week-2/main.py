import re

fd = open('regex_sum_1056347.txt')
text = fd.read()
number_final, total = re.findall('[0-9]+', text), 0

for i in number_final:
    i = int(i)
    total = total + i;

print(total)

fd.close()