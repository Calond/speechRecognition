import xml.etree.ElementTree
import os

two_up =  os.path.abspath(os.path.join("bayesian.py" ,"../.."))
rel_path = "HuricCorpus1.2\\v1.2\\Robocup\\xml\\"
abs_file_path = os.path.join(two_up, rel_path)

behaviours = []
totalOccurances = []
for filename in os.listdir(abs_file_path):
	root = xml.etree.ElementTree.parse(str(abs_file_path + filename)).getroot()

	if(root[3][0][0].get("name") not in behaviours):
		behaviours.append(root[3][0][0].get("name"))
		totalOccurances.append(0)

print(behaviours)

for filename in os.listdir(abs_file_path):
	print(filename)
	root = xml.etree.ElementTree.parse(str(abs_file_path + filename)).getroot()
	for i in range(len(behaviours)):
		if(root[3][0][0].get("name") == behaviours[i]):
			print(root[3][0][0].get("name"))
			sentenceOccurences = len(root[4].getchildren())
			print(sentenceOccurences)
			totalOccurances[i] += sentenceOccurences
		#Error check, behaviour not in list
		if root[3][0][0].get("name") not in behaviours:
			print("Behaviour not found")
			print(root[3][0][0].get("name"))
			quit()
		

print(behaviours)

print(totalOccurances)
