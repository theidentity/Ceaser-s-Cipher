def charToNum(c):
	if(c>='a' and c<='z'):
		return int(c-'a'+1)
	elif(c>='A' and c<='Z'):
		return int(c-'A'+1)
	else:
		return int(c)

def shiftLetter(c,shift):
	if(c>='a' and c<='z'):
		c = (ord(c)-ord('a')+shift)%26
		c = c + ord('a')
		c = chr(c)
	elif(c>='A' and c<'Z'):
		c = (ord(c)-ord('A')+shift)%26
		c = c + ord('A')
		c = chr(c)
	return c

def encrypt(infile,outfile):
	fout=open(outfile,'w')
	shift = 5
	with open(infile,'r') as f:
		while True:
			c=f.read(1)
			c = shiftLetter(c,shift)
			if not c:
				break
			out = c
			# print(c)
			fout.write(out)
	fout.close()