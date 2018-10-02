longstr = 'helloworld'
shortstr = 'hello'
print(shortstr in longstr)
print(longstr[longstr.find(shortstr):len(shortstr)])
newstr = longstr.replace(shortstr, '<player_name>')
print(newstr)

strs = [longstr, shortstr]
print(sorted(strs, key=len, reverse=True))
