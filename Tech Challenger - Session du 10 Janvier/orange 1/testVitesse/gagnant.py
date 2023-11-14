s1, s2 = input(), input()
common_elements = set(s1) & set(s2)
order1 = ''.join(c for c in s1 if c in common_elements)
order2 = ''.join(c for c in s2 if c in common_elements)
if order1 != '' and order1 == order2:
    print('TEMPETE')
    print(order1)
else:
    print('NORMAL')

