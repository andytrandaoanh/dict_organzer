import sys
import system_handler as sysHandle


def processText(dirIn, dirOut):

	
	#print(pathIn)
	pathOut = sysHandle.getRawPath(dirOut)

	bigDict = sysHandle.loadDictionaries(dirIn)
	
	#newDict = [item.lower() for item in bigDict]
	newDict = []

	for item in bigDict:
		
		newItem = item.replace(u'\ufeff', '')
		newDict.append(newItem.lower())

	newDict = list(dict.fromkeys(newDict))
	newDict.sort()

	#print('new dictionary:', newDict)
	sysHandle.writeListToFile(newDict, pathOut)

	sysHandle.openDir(dirOut)
	sys.exit()




def processText2(dirIn, dirOut):
	#print('dirIn:', dirIn, '\ndirOut:', dirOut)
	
	pathOut = sysHandle.getOutPath(dirOut)
	
	#print('pathOut:', pathOut)

	bigDict = sysHandle.loadDictionaries(dirIn)
	
	tempDict = [item for item in bigDict if item]

	newDict = list(dict.fromkeys(tempDict))
	newDict.sort()

	#print('new dictionary:', newDict)
	sysHandle.writeListToFile(newDict, pathOut)

	sysHandle.openDir(dirOut)
	sys.exit()
