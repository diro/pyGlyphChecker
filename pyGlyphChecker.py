#coding=utf-8
import sys
import freetype
import codecs
from sets import Set

#cmdargs = str(sys.argv)

face = freetype.Face(sys.argv[1])
f = codecs.open(sys.argv[2], encoding='utf-8')
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
	


