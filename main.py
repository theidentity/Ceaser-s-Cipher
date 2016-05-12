import encrypt
import decrypt
import plot

def printFiles(listOfFiles):
	for file in listOfFiles:
		print('_________',file,'_________')
		with open(file) as f:
			line=f.read()
			print(line)
		f.close()

encrypt.encrypt('msg','encrypted_msg')
decrypt.decrypt('encrypted_msg','decrypted_msg')

listOfFiles = ['msg','encrypted_msg','decrypted_msg']
printFiles(listOfFiles)
