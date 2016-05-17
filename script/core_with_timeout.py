import os
import sys
import subprocess
stuList = open("students-list", "r")

fileList = [
	"algorithm.hpp",      
	"list.hpp",           
	"queue.hpp",          
	"vector.hpp",
	"deque.hpp",          
	"map.hpp",            
	"stack.hpp",
	"exceptions.hpp",     
	"priority_queue.hpp", 
	"unordered_map.hpp",
	"utility.hpp"
]

def Prepare(stuName):
	print("%s: preparing the test..." % (stuName))
	dirname = "./testspace/"
	for filename in fileList:
		targetFile = open(dirname + filename, "w")
		targetFile.write("#include \"../students-source/%s/%s\"" % (stuName, filename))
		targetFile.close()
	print("%s: generated the headers." % (stuName))

def Clean(stuName):
	print("%s: clean test file." % (stuName))
	dirname = "./testspace/"
	for filename in fileList:
		os.remove(dirname + filename)

def CompileTest(testName, outfile):
	testCompile = subprocess.Popen(["g++", "-std=c++11", "-O2", "./testspace/%s.cc" % (testName), "-o", "./testspace/%s" % (testName)], stderr = outfile);
	testCompile.wait()
	if testCompile.returncode != 0:
		return False
	else:
		return True

def RunTest(testName, outfile):
	test = subprocess.Popen(["testspace/%s" % (testName)], stdout = outfile)
	test.wait()
	if test.returncode != 0:
		return False
	else:
		return True

def MemCheck(stuPath, stuName, testName):
	print("%s: %s: checking memory use," % (stuName, testName))
	errFilename = stuPath + ("/testres/mem-%s" % (testName))
	errfile = open(errFilename, "w")
	test = subprocess.Popen(["valgrind", "testspace/%s" % (testName)], stdout = subprocess.PIPE, stderr = errfile)
	test.wait()
	print("%s: %s: memory check completed, report at '%s'." % (stuName, testName, errFilename))
	if test.returncode != 0:
		return False
	else:
		return True	

def CheckAns(file1, file2, outfile):
	child = subprocess.Popen(["diff", file1, file2], stdout = outfile)
	child.wait()
	if child.returncode != 0:
		return False
	else:
		return True

def Test(stuPath, stuName, testName):
	print("%s: %s: start test, " % (stuName, testName))
	testOutFilename = stuPath + ("/testres/%s" % (testName))
	compileOut = open(stuPath + ("/compile-message/%s" % (testName)), "w")
	testOut = open(testOutFilename, "w")
	diffOut = open(stuPath + ("/diff-%s" % (testName)), "w")
	timeLimitFile = open("limit/limit-%s" % (testName), "r")
	timeLimit = int(timeLimitFile.readline())
	timeLimitFile.close()
	if CompileTest(testName, compileOut):
		try:
			subprocess.run(["testspace/%s" % (testName)], stdout = testOut, timeout = timeLimit, check = True)
			if CheckAns(testOutFilename, "testans/testans-%s" % (testName), diffOut):
				print("%s: %s: passed." % (stuName, testName))
				return 0
			else:
				print("%s: %s: failed (Wrong Answer)." % (stuName, testName))
				return 1
		except subprocess.TimeoutExpired:
			print("%s: %s: failed (Timeout)." % (stuName, testName))
			return 4
		except subprocess.CalledProcessError:
			print("%s: %s: failed (Runtime Error)." % (stuName, testName))
			return 2
	else:
		print("%s: %s: failed (Compile Error)." % (stuName, testName))
		return 3

def TestStudent(stuName):
	print("core: start testing %s" % (stuName))
	stuPath = "res/%s" % (stuName)
	compileMsgPath = stuPath + "/compile-message"
	testRes = stuPath + "/testres"
	try:
		os.stat(stuPath)
	except:
		os.mkdir(stuPath)
	try:
		os.stat(compileMsgPath)
	except:
		os.mkdir(compileMsgPath)
	try:
		os.stat(testRes)
	except:
		os.mkdir(testRes)
	Prepare(stuName)
	testList = [
		"deque-basic",
		"deque-advan-1",
		"deque-advan-2",
		"deque-advan-3",
		"deque-advan-4",
		"deque-advan-5"
	]
	status = []
	resList = []
	resTimeList = []
	for test in testList:
		resList.append(Test(stuPath, stuName, test))
	status = []
	for res in resList:
		if res == 0:
			status.append("Pass")
		elif res == 1:
			status.append("Failed(Wrong Answer)")
		elif res == 2:
			status.append("Failed(Runtime Error)")
		elif res == 3:
			status.append("Failed(Compile Error)")
		elif res == 4:
			status.append("Failed(Timeout)")
	return status

try:
	os.stat("res")
except:
	os.mkdir("res")

resCsv = open("test-result.csv", "w")

for line in stuList:
	stuName = line.strip()
	status = TestStudent(stuName)
	resCsv.write(stuName + ',')
	for res in status:
		resCsv.write(res + ',')
	resCsv.write('\n')

resCsv.close()

