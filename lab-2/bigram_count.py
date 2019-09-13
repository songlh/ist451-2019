
import sys

if __name__=='__main__':
	sFileName = sys.argv[1]
	countDict = {}
	with open(sFileName) as f:
		while True:
			line = f.readline()
			if not line:
				break

			words = line.split()

			for word in words:
				for i in range(len(word)-1):
					if word[i:i+2] not in countDict:
						countDict[word[i:i+2]] = 0

					countDict[word[i:i+2]] += 1

	d_view = [ (v,k) for k, v in countDict.iteritems() ]
	d_view.sort(reverse=True) # natively sort tuples by first element
	
	i = 0 
	for v, k in d_view:
		print "%s: %d" % (k,v)
		i += 1
		if i == 20:
			break
