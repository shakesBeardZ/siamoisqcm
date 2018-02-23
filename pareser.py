import re
text = open('test.txt')
chaine = text.read()
print(chaine)
# Read the text file
# path = 'test.txt'
# with open(path) as l:
# 	line = l.readline()
# 	while line:
# 		if (line.count('#')):
# 		 	ch = line
# 		 	line = l.readline()
#  			if( not line.count('$')):
#  			 	ch += line
#  			print(ch)		
#  		line = l.readline()		
# ch = ''
# for line in text:
# 	if (re.findall('^#',line)):
# 		ch += line
# 	elif (re.findall('^$',line)) :
# 		;;
# print(ch)			





#splited = mytext.split('$')
#result = re.split(r'#((?!\/)|[^*])*#', mytext)
#print(list(y.start() for y in x)) 
