cri = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj','s=', 'z=']
s = input()

for c in range(len(cri)):
    s = s.replace(cri[c], str(c))
print(len(s))


