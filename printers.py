from texttable import Texttable


def print_player_info(input):
    print("Full Name = {}\n"
          "Height = {}\n"
          "Weight = {}\n"
          "Date of Birth = {}\n"
          "Position = {}\n"
          "Team = {}\n"
          "Status = {}\n"
          "Years played = {}\n"
          "College = {}\n"
          "Profile URL = {}\n".format(
        input.fullName,
        input.height,
        input.weight,
        input.birthDate,
        input.position,
        input.team,
        input.status,
        input.yearsPro,
        input.college,
        input.profileUrl
    ))
    print()


def print_game_info(resultList):
    for g in resultList:
        print("Week {} of the {} NFL season".format(g['week'], g['seasonYear']))
        print()
        print("Score Summary: ")
        score_board = Texttable()
        score_board.add_rows([['Team', '1st Quarter', '2nd Quarter', '3rd Quarter', '4th Quarter', 'Overtime'],

                              [g['homeTeam']['team'], g['homeTeam']['scoreQ1'], g['homeTeam']['scoreQ2'],
                               g['homeTeam']['scoreQ3'], g['homeTeam']['scoreQ4'], g['homeTeam']['score'] - (
                                       g['homeTeam']['scoreQ1'] + g['homeTeam']['scoreQ2'] + g['homeTeam']['scoreQ3'] +
                                       g['homeTeam']['scoreQ4'])],
                              [g['awayTeam']['team'], g['awayTeam']['scoreQ1'], g['awayTeam']['scoreQ2'],
                               g['awayTeam']['scoreQ3'], g['awayTeam']['scoreQ4'], g['awayTeam']['score'] - (
                                       g['awayTeam']['scoreQ1'] + g['awayTeam']['scoreQ2'] + g['awayTeam']['scoreQ3'] +
                                       g['awayTeam']['scoreQ4'])]]

                             )

        print(score_board.draw())
        print()
        print("Final Score: ")
        print("     {}: {}".format(g['homeTeam']['team'], g['homeTeam']['score']))
        print("     {}: {}".format(g['awayTeam']['team'], g['awayTeam']['score']))
        print()


# "sack": 0,
# "cmp": 19,
# "passingTwoPointAttemptMade": 0,
# "cmpAirYds": 121,
# "passingTwoPointAttempt": 0,
# "passingInt": 0,
# "passingTds": 2,
# "att": 26,
# "sackYds": 0,
# "inCmpAirYds": 50,
# "passingTwoPointAttemptMissed": 0,
# "inCmp": 7,
# "passingYds": 222

def print_passing_info(resultList):
    stats = Texttable()
    stats.add_rows([['CMP', 'ATT', 'YDS', 'CMP %', 'AVG Y/A', 'TD', 'INT', 'SCK', 'SCK YDS', '2PT COMP', '2PT ATT'],
                    [resultList[0]['cmp'],
                     resultList[0]['att'],
                     resultList[0]['passingYds'],
                     float(resultList[0]['cmp'] / resultList[0]['att']) * 100,
                     float(resultList[0]['passingYds'] / resultList[0]['att']),
                     resultList[0]['passingTds'],
                     resultList[0]['passingInt'],
                     resultList[0]['sack'],
                     resultList[0]['sackYds'],
                     resultList[0]['passingTwoPointAttempt'],
                     resultList[0]['passingTwoPointAttemptMade']
                     ]

                    ])

    print(stats.draw())

def print_rushing_info(resultList):
    stats = Texttable()
    stats.add_rows([['ATT', 'YDS', 'AVG', 'TD', 'FUM LOST', 'RUSH 2PT MADE', 'RUSH 2PT ATT'],
                    [resultList[0]['attempt'],
                     resultList[0]['rushingYds'],
                     float(resultList[0]['rushingYds'] / resultList[0]['attempt']),
                     resultList[0]['tds'],
                     resultList[0]['fumblesLost'],
                     resultList[0]['rushingTwoPointAttemptMade'],
                     resultList[0]['rushingTwoPointAttempt']
                     ]

                    ])

    print(stats.draw())

def print_receiving_info(resultList):
    stats = Texttable()
    stats.add_rows([['REC',' TARGETS', 'YDS', 'AVG', 'YAC YDS', 'TD', 'FUM LOST', 'REC 2PT MADE', 'REC 2PT ATT'],
                    [resultList[0]['rec'],
                     resultList[0]['target'],
                     resultList[0]['receivingYds'],
                     float(resultList[0]['receivingYds'] / resultList[0]['rec']),
                     resultList[0]['yacYds'],
                     resultList[0]['tds'],
                     resultList[0]['fumblesLost'],
                     resultList[0]['receivingTwoPointAttemptMade'],
                     resultList[0]['receivingTwoPointAttempt']
                     ]

                    ])

    print(stats.draw())

def print_defensive_info(resultList):
    stats = Texttable()
    stats.add_rows([['SOLO TCKL', 'AST', 'TOTAL', 'TFL', 'TFL YDS', 'INT', 'PASS DEF', 'QB HIT', 'SACKS', 'FF', 'DEF TD', 'SFTY'],
                    [resultList[0]['tackle'],
                     resultList[0]['assistedTackles'],
                     resultList[0]['tackle'] + resultList[0]['assistedTackles'],
                     resultList[0]['tackleLoss'],
                     resultList[0]['tackleLossYards'],
                     resultList[0]['defenseInt'],
                     resultList[0]['passDef'],
                     resultList[0]['qbHit'],
                     resultList[0]['defenseSack'],
                     resultList[0]['forcedFumbles'],
                     resultList[0]['miscTds'] + resultList[0]['intTds'] + resultList[0]['recoveredFumbleTD'],
                     resultList[0]['safety']
                     ]

                    ])

    print(stats.draw())


def help_stats():
    print("available stats: ")
    print("     passing\n"
          "     rushing\n"
          "     receiving\n"
          "     defensive\n"
          )


def stat_prompt():
    print("Please type the stat you'd like to see (passing, rushing, etc.)")
    print("Leave blank to return all available stats")
    print("Type 'HELP' for all supported stat types")

def team_prompt():
    print("Please enter which team you'd like to look up")
    print("or type 'HELP' to view all teams and their keys")

def team_help():
    print("ARI -- Arizona Cardinals\n"
          "ATL -- Atlanta Falcons\n"
          "BAL -- Baltimore Ravens\n"
          "BUF -- Buffalo Bills\n"
          "CAR -- Carolina Panthers\n"
          "CHI -- Chicago Bears\n"
          "CIN -- Cincinnati Bengals\n"
          "CLE -- Cleveland Browns\n"
          "DAL -- Dallas Cowboys\n"
          "DEN -- Denver Broncos\n"
          "DET -- Detroit Lions\n"
          "GB  -- Green Bay Packers\n"
          "HOU -- Houston Texans\n"
          "IND -- Indianapolis Colts\n"
          "JAC -- Jacksonville Jaguars\n"
          "KC  -- Kansas City Chiefs\n"
          "LA  -- Los Angeles Rams\n"
          "MIA -- Miami Dolphins\n"
          "MIN -- Minnesota Vikings\n"
          "NE  -- New England Patriots\n"
          "NO  -- New Orleans Saints\n"
          "NYG -- New York Giants\n"
          "NYJ -- New York Jets\n"
          "OAK -- Oakland Raiders\n"
          "PHI -- Philadelphia Eagles\n"
          "PIT -- Pittsburgh Steelers\n"
          "SF  -- San Diego Chargers\n"
          "SEA -- Seattle Seahawks\n"
          "SF  -- San Francisco 49ers\n"
          "TB  -- Tamba Bay Buccanners\n"
          "TEN -- Tennessee Titans\n"
          "WAS -- Washington Redskins\n")