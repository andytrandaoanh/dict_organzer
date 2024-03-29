import os, sys
from datetime import datetime

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)


	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  


def getRawPath(dirOut):
	FILNAME_OUT = "Custom_Dictionary.txt"
	#temp_path = pathIn
	#temp_path = os.path.basename(temp_path)
	#fname, fext = os.path.splitext(temp_path)
	#pathOut =  os.path.join(dirOut, fname + JSON_EXTENSION) 
	pathOut =  os.path.join(dirOut, FILNAME_OUT) 
	return(pathOut)

def getOutPath(dirOut):
	now = datetime.now()
	dateTime = now.strftime("%Y%m%d_%H%M")
	fileName = "Normal_Case_Dictionary_" + dateTime + ".txt"
	pathOut =  os.path.join(dirOut, fileName ) 
	return(pathOut)


def getWordFromTextFile(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    
        

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")



def openExclusionList():
	FILE_NAME = 'exclusion.txt'
	try:
	    fh = open(FILE_NAME, 'r', encoding ='utf-8')
	    # Store configuration file values
	    data = fh.read()
	    fh.close()   
	    mylist = data.split('\n')
	    return mylist   
	    
	except FileNotFoundError:
		print('file not found')
		return None

def fileToList(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        words = data.split()
        return words
    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)    

def loadDictionaries(dirDic):
	dicFiles = os.listdir(dirDic)
	bigDic = []
	for fp in dicFiles:
		bigDic  += fileToList(os.path.join(dirDic, fp))

	dicData = list(dict.fromkeys(bigDic))
	dicData.sort()
	return dicData


def getLineFromTextFile(filepath):
    try:
        ofile = open(filepath, 'r', encoding = 'utf-8') 
        data = ofile.read()
        lines = data.split('\n')
        return lines

    except FileNotFoundError:
        print("file not found")    
    except Exception as e:
        print(e)   