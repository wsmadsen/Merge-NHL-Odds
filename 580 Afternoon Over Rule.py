import requests

# variables for finding afternoon games
Pacific1 = ["Vegas Golden Knights", "Anaheim Ducks",
            "Vancouver Canucks", "San Jose Sharks", "Los Angeles Kings"]
Pacific2 = ["Vegas Golden Knights", "Anaheim Ducks", "Vancouver Canucks", "San Jose Sharks",
            "Los Angeles Kings", "Arizona Coyotes", "Phoenix Coyotes"]
Mountain1 = ["Calgary Flames", "Colorado Avalanche",
             "Arizona Coyotes", "Phoenix Coyotes", "Edmonton Oilers"]
Mountain2 = ["Calgary Flames", "Colorado Avalanche", "Edmonton Oilers"]

Central = ["St. Louis Blues", "Chicago Blackhawks", "Minnesota Wild",
           "Winnipeg Jets", "Nashville Predators", "Dallas Stars"]

Eastern = ["Carolina Hurricanes", "Pittsburgh Penguins", "Tampa Bay Lightning", "Detroit Red Wings",
           "Columbus Blue Jackets", "Washington Capitals", "Buffalo Sabres", "Florida Panthers", "Toronto Maple Leafs",
           "Montréal Canadiens", "New Jersey Devils", "Boston Bruins", "Philadelphia Flyers", "New York Rangers",
           "New York Islanders", "Ottawa Senators", "Atlanta Thrashers"]


PST1 = ["T18:00:00Z", "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z", "T20:30:00Z", "T21:00:00Z",
        "T21:30:00Z", "T22:00:00Z", "T22:30:00Z", "T23:00:00Z", "T23:30:00Z", "T00:00:00Z", "T00:30:00Z"]
PST2 = ["T17:00:00Z", "T17:30:00Z", "T18:00:00Z", "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z",
        "T20:30:00Z", "T21:00:00Z", "T21:30:00Z", "T22:00:00Z", "T22:30:00Z", "T23:00:00Z", "T23:30:00Z"]
MST1 = ["T17:00:00Z", "T17:30:00Z", "T18:00:00Z", "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z",
        "T20:30:00Z", "T21:00:00Z", "T21:30:00Z", "T22:00:00Z", "T22:30:00Z", "T23:00:00Z", "T23:30:00Z"]
MST2 = ["T16:00:00Z", "T16:30:00Z", "T17:00:00Z", "T17:30:00Z", "T18:00:00Z", "T18:30:00Z", "T19:00:00Z",
        "T19:30:00Z", "T20:00:00Z", "T20:30:00Z", "T21:00:00Z", "T21:30:00Z", "T22:00:00Z", "T22:30:00Z"]
CST1 = ["T16:00:00Z", "T16:30:00Z", "T17:00:00Z", "T17:30:00Z", "T18:00:00Z", "T18:30:00Z", "T19:00:00Z",
        "T19:30:00Z", "T20:00:00Z", "T20:30:00Z", "T21:00:00Z", "T21:30:00Z", "T22:00:00Z", "T22:30:00Z"]
CST2 = ["T15:00:00Z", "T15:30:00Z", "T16:00:00Z", "T16:30:00Z", "T17:00:00Z", "T17:30:00Z", "T18:00:00Z",
        "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z", "T20:30:00Z", "T21:00:00Z", "T21:30:00Z"]
EST1 = ["T15:00:00Z", "T15:30:00Z", "T16:00:00Z", "T16:30:00Z", "T17:00:00Z", "T17:30:00Z", "T18:00:00Z",
        "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z", "T20:30:00Z", "T21:00:00Z", "T21:30:00Z"]
EST2 = ["T14:00:00Z", "T14:30:00Z", "T15:00:00Z", "T15:30:00Z", "T16:00:00Z", "T16:30:00Z", "T17:00:00Z",
        "T17:30:00Z", "T18:00:00Z", "T18:30:00Z", "T19:00:00Z", "T19:30:00Z", "T20:00:00Z", "T20:30:00Z"]
# importing schedule info
url = "https://statsapi.web.nhl.com/api/v1/schedule?startDate=2009-11-01&endDate=2010-03-13"
url2 = "https://statsapi.web.nhl.com/api/v1/schedule?startDate=2010-03-14&endDate=2010-04-30"
r = requests.get(url)
r2 = requests.get(url2)
schedule_data = r.json()
schedule_data2 = r2.json()
scoretotals = []
dates = schedule_data['dates']
for date in dates:
    for game in date['games']:
        x = []
        hometeamname = game['teams']['home']['team']['name']
        gametime = game['gameDate']
        if hometeamname in Pacific1:
            for time in PST1:
                if time in gametime:
                    x = True
        elif hometeamname in Mountain1:
            for time in MST1:
                if time in gametime:
                    x = True
        elif hometeamname in Central:
            for time in CST1:
                if time in gametime:
                    x = True
        elif hometeamname in Eastern:
            for time in EST1:
                if time in gametime:
                    x = True
        if x == True and game['gameType'] == 'R':
            hometeamrecord = game['teams']['home']['leagueRecord']
            if 'ot' in hometeamrecord.keys():
                hometeamWLratio = hometeamrecord['wins'] / (
                    hometeamrecord['wins'] + hometeamrecord['losses'] + hometeamrecord['ot'])
            else:
                hometeamWLratio = hometeamrecord['wins'] / (
                    hometeamrecord['wins'] + hometeamrecord['losses'])
            if hometeamWLratio >= 0.58:
                homescore = game['teams']['home']['score']
                awayscore = game['teams']['away']['score']
                scoretotal = homescore + awayscore
                print(hometeamname)
                print(gametime)
                scoretotals.append(scoretotal)
dates2 = schedule_data2['dates']
for date in dates2:
    for game in date['games']:
        x = []
        hometeamname = game['teams']['home']['team']['name']
        gametime = game['gameDate']
        if hometeamname in Pacific2:
            for time in PST2:
                if time in gametime:
                    x = True
        elif hometeamname in Mountain2:
            for time in MST2:
                if time in gametime:
                    x = True
        elif hometeamname in Central:
            for time in CST2:
                if time in gametime:
                    x = True
        elif hometeamname in Eastern:
            for time in EST2:
                if time in gametime:
                    x = True
        if x == True and game['gameType'] == 'R':
            hometeamrecord = game['teams']['home']['leagueRecord']
            if 'ot' in hometeamrecord.keys():
                hometeamWLratio = hometeamrecord['wins'] / (
                    hometeamrecord['wins'] + hometeamrecord['losses'] + hometeamrecord['ot'])
            else:
                hometeamWLratio = hometeamrecord['wins'] / (
                    hometeamrecord['wins'] + hometeamrecord['losses'])
            if hometeamWLratio >= 0.58:
                homescore = game['teams']['home']['score']
                awayscore = game['teams']['away']['score']
                scoretotal = homescore + awayscore
                print(gametime)
                print(hometeamname)
                print(scoretotal)
                scoretotals.append(scoretotal)
print(scoretotals)
avgscore = sum(scoretotals)/len(scoretotals)
print(avgscore)
print(len(scoretotals))


# carvswshWLrecord = schedule_data['dates'][2]['games'][1]['teams']['home']['leagueRecord']
# print(carvswshWLrecord)
# carvswshWLratio = carvswshWLrecord['wins']/(carvswshWLrecord['wins']+carvswshWLrecord['losses'] + carvswshWLrecord['ot'])
# print(carvswshWLratio)
# print(schedule_data['dates'][1]['games'][1]['teams']['home']['score'])
