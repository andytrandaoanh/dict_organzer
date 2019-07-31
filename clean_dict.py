import re
from system_handler import getLineFromTextFile, writeListToFile
from pprint import pprint

def isNormalWord(inputString):

	temp = str(inputString)
	regPat = r'^\w+[\w\s\-\']+\w$'
	pattern = re.compile(regPat, re.M)
	match = re.search(pattern, temp)
	return bool(match)


def generateCleanDict(inPath):
	dictLines = getLineFromTextFile(inPath)
	cleanDict = []
	for line in dictLines:
		if(line):
			if isNormalWord(line):
				cleanDict.append(line)
	cleanDict = sorted(cleanDict)
	return cleanDict

def compareTwoDict(inPath1, inPath2):
	#print('inPath1', inPath1, 'inPath2', inPath2)
	dict1 = getLineFromTextFile(inPath1)
	#print(dict1)
	dict2 = getLineFromTextFile(inPath2)
	#print(dict2)
	dirtyDict = []
	for item in dict1:
		if item not in dict2:
			dirtyDict.append(item)
			print('found:', item)
	#print(dirtyDict)

	return dirtyDict



if __name__ == "__main__":
	inPath1 = 'E:/FULLTEXT/DICTIONARY/NORMALCASE/Lexico_Full_LIst_2019.txt'
	inPath2 = 'E:/FULLTEXT/DICTIONARY/NORMALCASE/Lexico_Clean_List_2019.txt'
	outPath = 'E:/FULLTEXT/DICTIONARY/NORMALCASE/Lexico_Dirty_List_2019.txt'
	
	dirtyDict = compareTwoDict(inPath1, inPath2)
	writeListToFile(dirtyDict, outPath)

	#pprint(dirtyDict)






