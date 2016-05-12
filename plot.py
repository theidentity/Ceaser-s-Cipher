import numpy as np
import matplotlib.pyplot as plt
import operator

Freq = {}
	
def calculateFreq(infile):
	X = [x for x in range(1,26+1)]
	Freq = {el:0 for el in X}
	with open(infile,'r') as f:
		while True:
			c=f.read(1)
			if(c>='A' and c<='Z'):
				Freq[ord(c)-ord('A')+1]+=1
			elif(c>='a' and c<='z'):
				Freq[ord(c)-ord('a')+1]+=1
			if not c:
				break
	return Freq

def getShift(Msg_Freq,Enc_Msg_Freq):
	msgMax = max(Msg_Freq.iteritems(), key=operator.itemgetter(1))[0]
	encMsgMax = max(Enc_Msg_Freq.iteritems(), key=operator.itemgetter(1))[0]
	return (encMsgMax - msgMax)

def plot(msg,enc):
	fig = plt.figure()
	Freq = calculateFreq(msg)
	Msg_Freq = Freq 
	X = Freq.keys()
	Y = Freq.values()
	ax = fig.add_subplot(111)
	ax.bar(X,Y,color='red',alpha=0.8)

	Freq = calculateFreq(enc)
	Enc_Msg_Freq = Freq 
	X = Freq.keys()
	Y = Freq.values()
	ax = fig.add_subplot(111)
	ax.bar(X,Y,color='blue',alpha=0.8)

	shift = getShift(Msg_Freq,Enc_Msg_Freq)
	shift = 'Shift is by : '+str(shift)
	ax.set_title(shift)

	plt.show()

plot('msg','encrypted_msg')