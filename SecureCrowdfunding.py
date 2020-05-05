import time

### Start project.
def StartProject(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp, title, whitePaper, yellowPaper, tokensTotalSupply):
	# if project just started
	if(milestoneArr[i] == milestoneArr[0]):
		print('/////////////////////////////////////////////////')
		print('Project example:')
		print('* Project title: ', title)
		print('* Project whitepaper: ', whitePaper)
		print('* Project yellowpaper: ', yellowPaper)
		print('* Project tokens total supply: ', tokensTotalSupply)
		print('* Project tokens for investors: ', tokensForInvestors)
		print('* Project tokens for entrepreneur: ', tokensForEntrepreneur)
		print('* Project cost: ', projectCost)
		print('* Project time assumptions %d (10 years): ' % timeAssumption)
		print('* Project milestones:')
		print('    number;name;time;cost;stage')
		for j in range(len(milestoneArr)):
			print(milestoneArr[j])
		print('/////////////////////////////////////////////////\n')
		time.sleep(1)
		print('START...\n')
		projectCost -= milestoneArr[i][3]
		print('$ %d funds has been sent to the entrepreneur for the project start' % milestoneArr[i][3])
		print('$ Project balance decreased from %d to %d\n' % (projectCost+milestoneArr[i][3], projectCost))

	CheckMilestone(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)

# Checking progress by Krelos.
def CheckMilestone(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp):
	print('waiting...')
	time.sleep(0.25)
	question = input('$ %d of %d time have passed and Entrepreneur did not report.\n(Kleros) Is milestone "%s" completed? (y/n): ' % (temp, timeAssumption, milestoneArr[i][1]))

	if (question == 'y'):
		UnlockFunds(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
	elif(question == 'n'):
		ExtraChance(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
	else:
		print('\n###')
		print('$ Type: y or n')
		print('###\n')
		CheckMilestone(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)

# If milestone completed unlock funds for next one.
def UnlockFunds(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp):
	temp += milestoneArr[i][2]
	projectCost -= milestoneArr[i][3]
	milestoneArr[i][-1] = True
	if (milestoneArr[i] != milestoneArr[-1]):
		i+=1
		time.sleep(0.5)	
		print('\n$ %d funds has been released for realize "%s" milestone' % (milestoneArr[i][3], milestoneArr[i][1]))
		print('$ Project balance has been decreased from %d to %d:' % (projectCost+milestoneArr[i][3], projectCost))
		print('---------------------------------------------------------------------------------')
		StartProject(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp, title, whitePaper, yellowPaper, tokensTotalSupply)
	else:
		FinishProject(tokensForEntrepreneur)

# Option for entrepreneur if milestone not finished in predetermined time.
def ExtraChance(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp):
	question = input('\n(Entrepreneur) Do you want to open the case in Kleros court? (y/n): ')

	if (question == 'y'):
		DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
	elif (question =='n'):
		EndProject(projectCost, tokensForEntrepreneur)
	else:
		print('\n###')
		print('$ Type: y or n')
		print('###\n')
		ExtraChance(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)

# Entrepreneur declare:
# * how much extra time is needed to complete current milestone,
# * how much of the entrepreneur frozen tokens will be forwarded to investors for the extra time.
def DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp):
	timeDif = input('(Entrepreneur) How much extra time do you need to finish "%s" milestone?: ' % milestoneArr[i][1])
	tokenDif = input('(Entrepreneur) How much tokens from your frozen %d you are willing to give for extra time?: ' % tokensForEntrepreneur)
	try:
		val = int(timeDif)
		if(val<0):
			print('\n###')
			print('$ Type integers higher than 0')
			print('###\n')
			DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
		val1 = int(tokenDif)
		if(val1<0):
			print('\n###')
			print('Type integers higher than 0')
			print('###\n')
			DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
		if(val1>tokensForEntrepreneur):
			print('\n###')
			print('$ Insufficient balance, you have only %d tokens' % tokensForEntrepreneur)
			print('###\n')
			DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)
		
		KlerosCourt(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, val, val1, temp)
	except ValueError:
		print('\n###')
		print('$ Type integers')
		print('###\n')
		DeclareRequest(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)

# Kleros decide if entrepreneur will get extra chance.
def KlerosCourt(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, timeDif, tokenDif, temp):
	print('...')
	time.sleep(0.5)
	question = input('(Kleros) Do you accept Entrepreneur propostion? (y/n): ')

	if(question == 'y'):
		ChangeRules(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, timeDif, tokenDif, temp)
	elif(question == 'n'):
		EndProject(projectCost, tokensForEntrepreneur)
	else:
		print('\n###')
		print('$ Type: y or n')
		print('###\n')
		KlerosCourt(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, timeDif, tokenDif, temp)

# If Kleros agree, the project assumptions will be changed.
def ChangeRules(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, timeDif, tokenDif, temp):
	tokensForInvestors += tokenDif
	tokensForEntrepreneur -= tokenDif
	timeAssumption += timeDif
	temp += timeDif

	time.sleep(1)
	print('\nRules has changed...')
	print('Entrepreneur gets extra %d days to complete the "%s" milestone' % (timeDif, milestoneArr[i][1]))
	print('Project time assumption increased from %d to %d' % (timeAssumption-timeDif, timeAssumption))
	print('Tokens for investors increased from %d to %d' % (tokensForInvestors-tokenDif, tokensForInvestors))
	print('Entrepreneur tokens balance decreased from %d to %d' % (tokensForEntrepreneur+tokenDif, tokensForEntrepreneur))
	print('-------------------------------\n')
	
	CheckMilestone(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp)

# Case if entrepreneur can't or won't have extra chance.
def EndProject(projectCost, tokensForEntrepreneur):
	print('\n~~~The project failed')
	print('~%d funds go back to the investors' % projectCost)
	print('~%d tokens were burned' % tokensForEntrepreneur)
	exit()

# Case if project is completed.
def FinishProject(tokensForEntrepreneur):
	print('\n~~~The project success')
	print('~%d frozen tokens were sent to the entrepreneur' % tokensForEntrepreneur)
	exit()


### Declarations
title = 'Example'
whitePaper = 'whitepaper.pdf'
yellowPaper = 'yellowpaper.pdf'

# Declare tokens distribution
tokensTotalSupply = 1000
tokensForInvestors = 800
tokensForEntrepreneur = 200

# Declare project assumptions
projectCost = 10000000
timeAssumption = 3652

# Declare milestones (Number, Name, Time, Cost, State)
milestoneArr = [[0,'Start', timeAssumption*0.25, 0.25*projectCost, False],
		[1,'Beta', timeAssumption*0.25, 0.25*projectCost, False],
		[2,'Test', timeAssumption*0.25, 0.25*projectCost, False],
		[3,'Finish', timeAssumption*0.25, 0.25*projectCost, False]]

# Helpers
i = 0
temp = milestoneArr[0][2]

StartProject(milestoneArr, i, projectCost, tokensForEntrepreneur, timeAssumption, tokensForInvestors, temp, title, whitePaper, yellowPaper, tokensTotalSupply)

