#!/usr/bin/python
#       Name: Frank Lewis
#       NSID: fbl773
# Student ID: 11194945
#    Lecture: 04
#   Tutorial: T08
# Assignment: lab _
#   Synopsis: python - beans on toast... weird
import math
import sys

class DataSet:
	rows = "0"
	cols = "0"
	numELem = int(rows) * int(cols)
	listOfElem = []
	
	def __init__(self):
		self.rows = raw_input("How Many Rows?: ")
		self.cols = raw_input(" How Many Cols?: ")
		self.numElem = int(self.rows) * int(self.cols)
		inFile = open('./formated.txt')
		
		#create List
		cap = self.numElem
		print "Enter your Elements:"
		while (cap > 0):
			elem = inFile.readline()
			self.listOfElem.append(float(elem))
			cap = int(cap) - 1
			
		inFile.close()
		return
	
	"""
		getAverage(l)
		l - a list of elements
		return sum(l)
	"""
	def getAverage(self):
		return sum(self.listOfElem)/len(self.listOfElem)

	"""
		displayStats(elemList)
		-----------------------
		elemList - a list of all the given elements
		return - nothing.
	"""
	def getStats(self):
		#sumElements=sum(l)
		statStr=""
		statStr += "Summation is: " + str(sum(self.listOfElem))
		statStr += "\nAverage is: " + str(self.getAverage())
		statStr += "\nMedian is: "  + str(self.getMedian())
		statStr +=  "\nVariance is: " + str(self.getVariance())
		statStr +=	"\nSampleVariance: " + str(self.getSVariance())
		statStr +=  "\nStandard Deviation is: " + str(self.getStdDev())
		statStr +=	"\nSample std Deviation is: " + str(math.sqrt(self.getSVariance()))
		statStr +=  "\nMean Absolute Deviation: " + str(self.getMeanDeviance())
		statStr +=  "\nRange is: " + str(self.getRange())
		statStr +=  "\nQuartiles are: " + str(self.getQuartiles())
		statStr +=	"\nIQR: " + str(self.getIQR())
		statStr +=	"\nUpper Fence: " + str(self.getFences()[1])
		statStr +=	"\nLower Fence: " + str(self.getFences()[0])
		statStr +=  "\nGrid:" + self.makeGrid() 
	
		return statStr

	"""
		getRange(l)
		-----------------
		l - a list of elements
		return - the difference between the largest and smallest elements
	"""
	def getRange(self):
		self.listOfElem.sort()
		return float(abs(self.listOfElem[len(self.listOfElem)-1] - self.listOfElem[0]))

	"""
		getMeanDeviance(l)
		l - a list of elements
		return - whatever the f a mean Deviance is. (sum of the difference)^2
		"""
	def getMeanDeviance(self):
		meanDevList = [] # will hold the modified elements
		avg = self.getAverage()
		for e in self.listOfElem:
			meanDevList.append((abs(float(e-avg))))

		return (float(1.0/self.numElem) * sum(meanDevList))

	"""
		variance(l)
		l - a list of elements
		return - the variance of the data set!
	"""
	def getVariance(self):
		variedList = [] # will hold the modified elements
		avg = self.getAverage()
		for e in self.listOfElem:
			variedList.append(pow(float(e-avg),2))
		
		return (float(1.0/self.numElem) * sum(variedList))
		
	"""
		getStdDev(l)
		--------------
		l - a list of elements
		return - the Standard Deviation
	"""
	def getStdDev(self):
		return math.sqrt(self.getVariance())
		
	"""
		getMedian(l)
		-------------
		l - a list of elements
		return if even, 2 middle most averaged
				else, middle most element
	
	"""
	def getMedian(self):
		self.sortList()
		center = (int(self.numElem) + 1)/2 # yes I'm mad i used american "center" not the proper centre, but its written...
		if(float(self.numElem)%2 == 0):
			return (float(self.listOfElem[center-1]) + float(self.listOfElem[center]))/2.0
		else:
			return float(self.listOfElem[center])

	"""
		makeGrid(l)
		l - a list of elements
		return a string that represents the data as a matrix/list
	"""
	def makeGrid(self):
		count = 0
		print "Length of list is: " + str(int(len(self.listOfElem)))
		rowStr  = "\n\n"
		while (count < len(self.listOfElem)):
			if(count % int(self.cols) == 0 and count != 0):
				rowStr += '\n'
			rowStr += str(self.listOfElem[count]) + ' '
			count += 1

		return rowStr + '\n'

	"""
		sortList(l):
		l - a list of elements.
		return a sorted list (hopefully)
	"""
	def sortList(self):
		self.listOfElem.sort()
		return 
		
	"""
	getQuartiles()
	return - a list of the quartiles
	"""
	def getQuartiles(self):
		#prepare list and get positions
		self.listOfElem.sort()
		quartList = []

		#Quartile Postions
		pQ1 = (float(self.numElem)+1)/4.0
		pQ2 = (float(self.numElem)+1)/2.0
		pQ3 = (3.0*(float(self.numElem)+1))/4.0
		
		#Quartile Modifiers
		mQ1 = (float(pQ1) - int(pQ1))
		mQ2 = (float(pQ2) - int(pQ2))
		mQ3 = (float(pQ3) - int(pQ3))
		
		
		if(float(pQ1) % 4.0 == 0):
			quartList.append(self.listOfElem[int(pQ1) -1])
		else:
			quartList.append(self.listOfElem[int(pQ1)-1] + (mQ1 * (self.listOfElem[int(pQ1)] - self.listOfElem[int(pQ1)-1])))
	
		if(float(pQ2) % 2.0 == 0):
			quartList.append(self.listOfElem[int(pQ2)-1])
		else:
			quartList.append(self.listOfElem[int(pQ2)-1] + (mQ2 * (self.listOfElem[int(pQ2)] - self.listOfElem[int(pQ2)-1])))
	
		if(float(pQ3) % 4.0 == 0):
			quartList.append(self.listOfElem[int(pQ3)-1])
		else:
			quartList.append(self.listOfElem[int(pQ3)-1] + (mQ3 * (self.listOfElem[int(pQ3)] - self.listOfElem[int(pQ3)-1])))
	
		return quartList
	
	"""
		getIQR()
		return: the difference between first and third quartiles!
	"""
	def getIQR(self):
		quarts = self.getQuartiles()
		return (quarts[2] - quarts[0])
	
	"""
		getFences()
		uses the quartiles to grab upper and lower fences and put them in a list!
		return the list! [lower,upper]
	"""
	def getFences(self):
		quarts = self.getQuartiles()
		fences = []
		
		fences.append(quarts[0] - (1.5 * self.getIQR()))
		fences.append(quarts[2] + (1.5 * self.getIQR()))
		
		return fences
		
	def getSVariance(self):
		variedList = [] # will hold the modified elements
		avg = self.getAverage()
		for e in self.listOfElem:
			variedList.append(pow(float(e-avg),2))
		
		return (float(1.0/(self.numElem - 1)) * sum(variedList))
			

		

###############################################
print "Begin Adder"

#take data

testSet = DataSet()

print testSet.getStats()





#Create List and Grab Total
# listOfElem = createList(int(rows)*int(cols))
# print "unsorted is: " + makeGrid(listOfElem)
# print " \nsorted is: " + makeGrid(sortList(listOfElem))
# print getStats(listOfElem)



	