import json, time

jsonFile = open("questions.json", 'r')
questions = json.load(jsonFile)

def runQuiz():

	__result = 0

	print("----------------------------Welcome to the quiz---------------------------------------")
	
	print("1. Sport")
	print("2. Maths")
	print("3. Exit")
	choice = int(input("Select any one group:"))


	print("--------------------------------------------------------------------------------------")

	if choice == 1:
		for qno,que in questions["quiz"]["sport"].items():
			print("{}. {}".format(qno, que["question"]))
			answer = que["answer"]
			print("Options:")
			cnt = 0
			for opt in que['options']:
				cnt += 1
				print("{}. {}".format(cnt,opt))

			userAns = int(input("Answer : "))
			if userAns > 0 and userAns < 5:
				if que["options"][userAns - 1] == answer:
					__result += 1
			else:
				print("Invalid Choice!")

			print("--------------------------------------------------------------------------------------")


	elif choice == 2:
		for qno,que in questions["quiz"]["maths"].items():
			print("{}. {}".format(qno, que["question"]))
			answer = que["answer"]
			print("Options:")
			cnt = 0
			for opt in que['options']:
				cnt += 1
				print("{}. {}".format(cnt,opt))

			userAns = int(input("Answer : "))
			if userAns > 0 and userAns < 5:
				if que["options"][userAns - 1] == answer:
					__result += 1
			else:
				print("Invalid Choice!")

			print("--------------------------------------------------------------------------------------")
			
					
	else: 
		print("Exiting...")
		time.sleep(1)
		return


	print("Your Score -> ", __result)
	print("Exiting...")
	time.sleep(1)



runQuiz()