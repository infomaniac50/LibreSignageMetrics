#####
#importing modules
import glob, re, sys, os, fnmatch
br = "\n"
tab = "\t"
 
 
#####
#exiting if all 3 arguments are not passed via command line
def fail():
    print ("ERROR: " + str(len(sys.argv)-1) + " of 3 required arguments provided.")
    sys.exit()
 
 
#####
#getting arguments passed via command line
    
#testing for root DIRECTORY string
try: myDir = sys.argv[1]
except: fail()
 
#testing for RECURSION boolean
try: myRec = sys.argv[2]
except: fail()
 
#testing for OUTPUT filename string
try: myFile = sys.argv[3]
except: fail()
 
 
#####
#making list of PHP files within DIRECTORY
if myRec == "0": #without recursion
    myDir2 = myDir + "/*.php"
    PHP_list = glob.glob(myDir2)
elif myRec == "1": #with recursion
    PHP_list = []
    for dirname, dirnames, filenames in os.walk(myDir):
        for filename in filenames:
            if fnmatch.fnmatch (filename,("*.php")):
                match = os.path.join(dirname,filename)
                PHP_list.append(match)
 
#make an empty list;
#tuples will go in the list;
#each tuple will contain a PHP filename and a PHP filename it includes
includeList = []
 
#iterate through each PHP file and place tuples in the list
for phpFile in PHP_list:
    fileOpen = open(phpFile, "r")
    #for each line in a PHP file
    for line in fileOpen:
            m = re.match(r"(.*)include(.*\()(.*)\)", line) #for include(),include_once()
            if m:
                matchFile = m.group(3)[0:-1]
                if matchFile[-4::] == ".php": #only PHP files
                    phpFile = phpFile.replace("\\","/")
                    phpFile = phpFile.replace('$_SERVER[DOCUMENT_ROOT]./', "")
                    phpFile = phpFile.replace('./', "")
                    matchFile = matchFile.replace("\\","/")
                    matchFile = matchFile.replace("\"","")
                    matchFile = matchFile.replace('\'',"")
                    matchFile = matchFile.replace('$_SERVER[DOCUMENT_ROOT]./', "")
                    matchFile = matchFile.replace('./', "")
                    includeList.append([phpFile[len(myDir):], matchFile])
            else: pass
 
            m = re.match(r'(.*)require(.*\()(.*)\)', line) #for require(), require_once()
            if m:
                matchFile = m.group(3)[0:-1]
                if matchFile[-4::] == '.php': #only PHP files
                    phpFile = phpFile.replace("\\","/")
                    phpFile = phpFile.replace('$_SERVER[DOCUMENT_ROOT]./', "")
                    phpFile = phpFile.replace('./', "")
                    matchFile = matchFile.replace("\\","/")
                    matchFile = matchFile.replace("\"","")
                    matchFile = matchFile.replace('\'',"")
                    matchFile = matchFile.replace('$_SERVER[DOCUMENT_ROOT]./', "")
                    matchFile = matchFile.replace('./', "")
                    includeList.append([phpFile[len(myDir):], matchFile])
            else: pass
 
 
#####
#creating DOT file
dot = open(myFile, "w")
 
#writing to DOT file
dot.write("digraph {" + br)
for a,b in includeList:
    dot.write(tab)
    dot.write("\"")
    dot.write(a)
    dot.write("\"")
    dot.write(" -> ")
    dot.write("\"")
    dot.write(b)
    dot.write("\"")
    dot.write(";")
    dot.write(br)
dot.write("}")
dot.close()
 
 
#####
#exiting
sys.exit()