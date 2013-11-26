#coding=utf-8
import freetype
import codecs
from sets import Set

face = freetype.Face('YOURTTF.ttf')
f = codecs.open('INPUT_TEXT_FILE', encoding='utf-8')
s = Set([])

for line in f:
	for c in line:	
		if c == '\r' or c == '\n' or c== '\t':
			continue
		if face.get_char_index(c) == 0:				
			s.add(repr(c))
		
print "lost characters:{}".format(len(s))
for c in s:
	print c
	


