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


def help_stats():
    print("available stats: ")
    print("     passing\n"
          "     rushing\n"
          "     receiving\n"
          "     kick return\n"
          "     fumbles\n"
          "     defense\n"
          "     kicking\n"
          "     punting\n")


def stat_prompt():
    print("Please type the stat you'd like to see (passing, rushing, etc.)")
    print("Leave blank to return all available stats")
    print("Type 'HELP' for all supported stat types")