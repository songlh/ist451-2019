import sys
import md5


if __name__ == '__main__':
	sFileName = sys.argv[1]
	dictMD5 = {} # dictMD5 is a dict using MD5 hash value string as key and using corresponding ascii character as value

	for num in range(256): #num will be 0, 1, 2, 3, ... 255
		c = chr(num) # chr() will change the input number into its corresponding ascii character
		m = md5.new() # create a md5 object to calculate MD5 hash string
		m.update(c) # pass an ascii character to md5 object
		dictMD5[m.hexdigest()] = c # m.hexdigest() will return MD5 hash value string

	with open(sFileName, 'r') as f: # open a file
		lines = f.readlines() # read file content line by line

		sResult = ''
		for line in lines:
			sResult += dictMD5[line[:-1]] # each line of the file is a MD5 hash string, and we change each line back to its corresponding ascii character. 

		print sResult # print result