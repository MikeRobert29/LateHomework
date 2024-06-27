#coding:utf-8

import csv

eastern_conference = []
western_conference = []

eaternConference_home_winLoss = []
eaternConference_away_winLoss = []

winLossRatio_home = []
winLossRatio_away = []

eastern_conference_Difference_PFPA = []
western_conference_Difference_PFPA = []

with open("pe8_data.csv", mode = "r") as file :

	reader = csv.reader(file)

	for row, value in enumerate(reader) :

		if 1 <= row <= 15 :
			eastern_conference.append(value)

	file.seek(0)
	next(reader)

	for row, value in enumerate(reader) :

		if row >= 15 :
			western_conference.append(value)

	del western_conference[len(western_conference) - 1]

#------------------------------First Treatement----------------------------------------------------------------------------------------------

	for team in eastern_conference[0:] :
		eaternConference_home_winLoss.append(team[7].split("-"))

	for team in eastern_conference[0:] :
		eaternConference_away_winLoss.append(team[8].split("-"))

	for data in eaternConference_home_winLoss :
		ratio = int(data[0]) / (int(data[0]) + int(data[1]))
		winLossRatio_home.append(ratio)

	for data in eaternConference_away_winLoss :
		ratio = int(data[0]) / (int(data[0]) + int(data[1]))
		winLossRatio_away.append(ratio)

	i = 0
	teams = ""
	while i < len(winLossRatio_home) :
		
		if winLossRatio_home[i] < winLossRatio_away[i] :

			teams += eastern_conference[i + 1][1] + " "

		i += 1

	print("\nThe teams from the Eastern Conference with the win-loss percentage at Home lower than the win-loss percentage of Away are : {}.\n".format(teams))

#------------------------------second Treatement---------------------------------------------------------------------------------------------

	for team in eastern_conference :
		diff = round(float(team[5]) - float(team[6]), 1)
		eastern_conference_Difference_PFPA.append(diff)

	for team in western_conference :
		diff = round(float(team[5]) - float(team[6]), 1)
		western_conference_Difference_PFPA.append(diff)

	avgEast, avgWest = 0, 0

	avgEast = round(sum(eastern_conference_Difference_PFPA) / len(eastern_conference_Difference_PFPA), 1)
	avgWest = round(sum(western_conference_Difference_PFPA) / len(western_conference_Difference_PFPA), 1)

	if avgEast > avgWest :
		print("The eastern conference had a higher average difference about “PF minus PA” wich is {}\n".format(avgEast))
	elif avgEast < avgWest :
		print("The western conference had a higher average difference about “PF minus PA” wich is {}\n".format(avgWest))
	else :
		print("Both conferences had the same average difference about “PF minus PA” wich is {}\n".format(avgEast))

#------------------------------Third Treatement-----------------------------------------------------------------------------------------------

TotalWins = {}

for team in eastern_conference :
	TotalWins[team[1]] = int(team[2][0:2])

for team in western_conference :
	TotalWins[team[1]] = int(team[2][0:2])

sortedWins = dict(sorted(TotalWins.items(), key = lambda item : item[1], reverse = True))

print("\n\t\t     -RANKING-\n")

for team, wins in sortedWins.items() :
	if team != "Trail Blazers" :
		team = team + " " * (len("Trail Blazers") - len(team))
	print("\t\t", team, ":", wins)

#--------------------------------------------END--------------------------------------------------------------------------------------------