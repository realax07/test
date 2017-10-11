# def parse_molecule(formula):
#     a, i, alp, num, s = [], -1, 'abcdefghijklmnopqrstuvwxyz', "1234567890", ''
#     for f in formula:
#         if (f in alp.upper() or f == "(" or f == "[") and s != '(' and s != '[':
#             a.append(f)
#             i += 1
#             s = f
#         elif f in alp or f == ")" or f == "]" or s == '[' or s == '(':
#             a[i] += f
#             s = f
#         elif f in num:
#             a[i] += "*" + f
#             s = f
#
#     for f in a:
#         if f[0] in alp.upper():
#
#     a = '+'.join(a)
#
#     return a
# print parse_molecule('Kn4[ON(SO3)2]2')

import re


# def zeroes(base, number):
#     f, count, b = 1, 0, base
#     for i in range(1, number+1): f *= i
#     print f
#     while True:
#         print base
#         if f % base == 0:
#             count += 1
#             base *= b
#         else: break
#
#     return count
#
#
#
# print zeroes(17, 15687216586)


# 75
#
# class pop:
#     x, lol = 0, False
#     def create_pop(self):
#         while not self.lol:
#             self.x += 1
#             yield "%s pop" % self.x
#
# p = pop()
#
# pool = p.create_pop()
#
# print [pool.next() for cash in range(10)]
#
