__author__ = 'spencertank'
import string #fixed typo was using


s = 'Hello world'
a = s.split(' ')
size = len(a)

rot13 = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")

for i in range(0, size):
    if i % 2 == 0:
        a[i] = string.translate(a[i][::-1], rot13)
    else:
        a[i] = string.translate(a[i], rot13)


print a