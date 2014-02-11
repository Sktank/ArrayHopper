__author__ = 'spencertank'

count = 0
n = 10000

for i in range(0, n + 1):
    if '7' in list(str(i)):
        count += 1

print count