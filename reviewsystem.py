import os, random, glob, shutil


def ask():
	print "You have chosen to ask a question!"
	# script to extract content from WP: Backlogs

def answer():

	print "\nYou have chosen to answer a question!"
	try:
		qfilename = random.choice(glob.glob("./asked/*")+glob.glob("./answered/*q")+glob.glob("./tied/*q"))
	except:
		print "Looks like there are no more questions. Check back later!"
		return
	

	# question came from ./asked
	# dump question and answer in ./answered
	if qfilename[3] == 's':

		print "\nThe question is:\n"
		with open(qfilename, 'r') as qfile:
			print qfile.read()
		
		print "\nWhat do you wish to do?"
		print "1. Submit"
		print "2. Skip"
		choice = int(raw_input())
		
		# Skip
		if(choice == 2):
			return
		
		# Answer
		else:
			print "\nPlease provide your answer:"
			answer = raw_input()
			
			afilename = './answered/' + qfilename[-10:-1] + 'a'
			shutil.move(qfilename, './answered/'+qfilename[-10:])
			with open(afilename, 'w+') as afile:
				afile.write(answer)
			return


	# question came from ./answered
	elif qfilename[3] == 'n':
		
		print "\nThe question is:\n"
		with open(qfilename, 'r') as qfile:
			print qfile.read()
		
		afilename = qfilename[:-1] + 'a'
		print "\nThe original answer is:\n"
		with open(afilename, 'r') as afile:
			print afile.read()

		print "\nWhat do you wish to do?"
		print "1. Agree"
		print "2. Disagree"
		print "3. Skip"
		choice = int(raw_input())
		
		# Skip
		if(choice == 3):
			return

		# Agree
		# dump question, answer and comments in ./recommend
		elif (choice == 1):
			print "\nPlease provide your comment:"
			comment = raw_input()

			cfilename = './recommend/' + qfilename[-10:-1] + 'c'
			shutil.move(qfilename, cfilename[:-1]+'q')
			shutil.move(afilename, cfilename[:-1]+'a')
			with open(cfilename, 'w+') as cfile:
				cfile.write(comment)
			return

		# Disagree
		# dump question, answer and comments in ./tied
		else:
			print "\nPlease provide your comment:"
			comment = raw_input()

			cfilename = './tied/' + qfilename[-10:-1] + 'c'
			shutil.move(qfilename, cfilename[:-1]+'q')
			shutil.move(afilename, cfilename[:-1]+'a')
			with open(cfilename, 'w+') as cfile:
				cfile.write(comment)
			return


	# question came from tied
	else:
		print "\nThe question is:\n"
		with open(qfilename, 'r') as qfile:
			print qfile.read()
		
		afilename = qfilename[:-1] + 'a'
		print "\nThe original answer is:\n"
		with open(afilename, 'r') as afile:
			print afile.read()

		cfilename = qfilename[:-1] + 'c'
		print "\nThe opposing comment is:\n"
		with open(cfilename, 'r') as cfile:
			print cfile.read()

		print "\nWhat do you wish to do?"
		print "1. Endorse original answer"
		print "2. Endorse opposing comment"
		print "3. Skip"
		choice = int(raw_input())
		
		# Skip
		if(choice == 3):
			return

		# Endorse original answer
		# dump question, answer and all comments in ./recommend
		elif (choice == 1):
			print "\nPlease provide your comment:"
			comment = raw_input()

			efilename = './recommend/' + qfilename[-10:-1] + 'e'
			shutil.move(qfilename, efilename[:-1]+'q')
			shutil.move(afilename, efilename[:-1]+'a')
			shutil.move(cfilename, efilename[:-1]+'c')
			with open(efilename, 'w+') as efile:
				efile.write(comment)
			return

		# Endorse opposing comment
		# dump question, answer and all comments in ./recommend
		else:
			print "\nPlease provide your comment:"
			comment = raw_input()

			ofilename = './recommend/' + qfilename[-10:-1] + 'o'
			shutil.move(qfilename, ofilename[:-1]+'q')
			shutil.move(afilename, ofilename[:-1]+'a')
			shutil.move(cfilename, ofilename[:-1]+'c')
			with open(ofilename, 'w+') as ofile:
				ofile.write(comment)
			return


def recommend():

	print "\nYou have chosen to edit a recommendation!"
	try:
		qfilename = random.choice(glob.glob("./recommend/*q"))
	except:
		print "Looks like there are no more recommendations. Check back later!"
		return

	print "\nThe question is:\n"
	with open(qfilename, 'r') as qfile:
		print qfile.read()
	
	afilename = qfilename[:-1] + 'a'
	print "\nThe original answer is:\n"
	with open(afilename, 'r') as afile:
		print afile.read()

	cfilename = qfilename[:-1] + 'c'
	print "\nThe opposing comment is:\n"
	with open(cfilename, 'r') as cfile:
		print cfile.read()

	if os.path.isfile(qfilename[:-1] + 'e'):
		efilename = qfilename[:-1] + 'e'
		print "\nThis question had a tie."
		print "The original answer has been endorsed. Third Comment is below:\n"
		with open(efilename, 'r') as efile:
			print efile.read()

	elif os.path.isfile(qfilename[:-1] + 'o'):
		ofilename = qfilename[:-1] + 'o'
		print "\nThis question had a tie."
		print "The opposing comment has been endorsed. Third Comment is below\n"
		with open(ofilename, 'r') as ofile:
			print ofile.read()

	print "\nWhat do you wish to do?"
	print "1. Edit"
	print "2. Skip"
	choice = int(raw_input())
	
	# Skip
	if(choice == 2):
		return

	# Done
	else:
		print "\nPlease make necessary changes to the article and paste the diff link of the edit"
		diff = raw_input()

		dfilename = './archive/' + qfilename[-10:-1] + 'd'
		shutil.move(qfilename, './archive/'+qfilename[-10:])
		shutil.move(afilename, './archive/'+afilename[-10:])
		shutil.move(cfilename, './archive/'+cfilename[-10:])

		if(os.path.isfile(qfilename[:-1] + 'e')):
			shutil.move(efilename, './archive/'+efilename[-10:])
		elif(os.path.isfile(qfilename[:-1] + 'o')):
			shutil.move(ofilename, './archive/'+ofilename[-10:])

		with open(dfilename, 'w+') as dfile:
			dfile.write(diff)
		return

	
def logs():
	print "\nLogs"


if __name__ == '__main__':

	options = { 1: ask,
			2: answer,
			3: recommend,
			4: logs,
			5: exit
		}
	
	while True:
		print "\n-----What do you wish to do?-----"
		print "1. Ask"
		print "2. Answer"
		print "3. Recommend"
		print "4. View Logs"
		print "5. Exit"
		print "\nEnter a valid number to continue:"
		choice = int(raw_input())
		options[choice]()



