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

def Time(testName, outfile, errfile):
	test = subprocess.Popen(["time", "testspace/%s" % (testName)], stdout = outfile, stderr = errfile)
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
	if CompileTest(testName, compileOut):
		if RunTest(testName, testOut):
			if CheckAns(testOutFilename, "testans/testans-%s" % (testName), diffOut):
				print("%s: %s: passed." % (stuName, testName))
				return 0
			else:
				print("%s: %s: failed (Wrong Answer)." % (stuName, testName))
				return 1
		else:
			print("%s: %s: failed (Runtime Error)." % (stuName, testName))
			return 2
	else:
		print("%s: %s: failed (Compile Error)." % (stuName, testName))
		return 3

def TimeTest(stuPath, stuName, testName):
	print("%s: starting the test %s, " % (stuName, testName))
	testOutFilename = stuPath + ("/testres/%s" % (testName))
	compileOut = open(stuPath + ("/compile-message/%s" % (testName)), "w")
	testOut = open(testOutFilename, "w")
	testErr = open(stuPath + ("/testres/time-%s" % (testName)), "w")
	diffOut = open(stuPath + ("/diff-%s" % (testName)), "w")
	if CompileTest(testName, compileOut):
		if Time(testName, testOut, testErr):
			if CheckAns(testOutFilename, "testans/testans-%s" % (testName), diffOut):
				print("%s: %s: passed." % (stuName, testName))
				return 0
			else:
				print("%s: %s: failed (Wrong Answer)." % (stuName, testName))
				return 1
		else:
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
		"list-basic",
		"list-spfa",
		"list-dijkstra",
	]
	timeTestList = [
		"list-benchmark"
	]
	resList = []
	resTimeList = []
	for test in testList:
		resList.append(Test(stuPath, stuName, test))
	for test in timeTestList:
		resTimeList.append(TimeTest(stuPath, stuName, test))
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
	for res in resTimeList:
		if res == 0:
			status.append("Pass")
		elif res == 1:
			status.append("Failed(Wrong Answer)")
		elif res == 2:
			status.append("Failed(Runtime Error)")
		elif res == 3:
			status.append("Failed(Compile Error)")
	Clean(stuName)
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
