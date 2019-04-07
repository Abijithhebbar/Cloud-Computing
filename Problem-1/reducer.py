
import sys
if __name__ == '__main__':
	doclist = {}	
	for line in sys.stdin:
		word = line.strip().split('\t')
		if(word[0] in doclist):
			doclist[word[0]].append(word[1])
		else :
			doclist[word[0]] = [word[1]]
	for w in doclist:
		print('%s\t%s'%(w, doclist[w]))
