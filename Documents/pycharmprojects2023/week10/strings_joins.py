line = 'root::0:0:superuser:/root:/bin/sh'
elems = line.split(':')
print(elems)

elems[0] = 'avatar'
elems[4] = 'The super-user (zero)'

print(elems)

line = ':'.join(elems)
print(line)

