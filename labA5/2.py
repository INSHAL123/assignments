d1={'a':10,'b':20,'c':30,'d':40}
d2={'c':12,'e':15,'f':18}
for each in d2.keys():
    if each in d1.keys():
        d1[each]=d1[each]+d2[each]
    else:
        d1.setdefault(each,d2[each])
print(d1)

