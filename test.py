from xml.etree.ElementTree import parse
logins = parse('data/logins.xml')
name = lname = password = ''
# Extract and output tags of interest
for item in logins.iterfind('logins'):
    name = item.findtext('name')
    lname = item.findtext('lname')
    password = item.findtext('password')
print('<<__start__>>')
print(name)
print(lname)
print(password)    
print('<<__end__>>')
