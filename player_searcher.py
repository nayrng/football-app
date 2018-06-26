import collections
import requests
import results
import printers

player_info = collections.namedtuple(
        "player_info",
        "weight, profileId, gsisName, uniformNumber, fullName, height, lastName, firstName, birthDate, profileUrl, status, team, playerId, position, yearsPro, college"

    )

player_stats_passing = collections.namedtuple(
        "player_stats_passing",
        "sack, cmp, passingTwoPointAttemptMade, passingTwoPointAttempt, passingInt, passingTds, att, sackYds, inCmp, passingYds"

    )

player_stats_rushing = collections.namedtuple(
        "player_stats_rushing",
        "fumblesLost, rushingTwoPointAttemptMade, rushingYds, tds, rushingTwoPointAttempt, loss, attempt, lossYds"
)

player_stats_receiving = collections.namedtuple(
        "player_stats_receiving",
        "receivingTwoPointAttemptMade, fumblesLost, yacYds, tds, rec, target, receivingYds, receivingTwoPointAttempt"
)

#TODO: Some players don't have teams, uniform numbers, etc. Fix Later
def findPlayerLastName(search_text):
    url = 'http://api.suredbits.com/nfl/v0/players/{}'.format(search_text)
    resp = requests.get(url)
    print(resp.status_code)
    player_data = resp.json()
    players = [
        player_info(**pl)
        for pl in player_data
    ]
    return players

def findPlayerFullName(search_text):

    url = 'http://api.suredbits.com/nfl/v0/players/{}/{}'.format(search_text[1], search_text[0])
    resp = requests.get(url)
    print(resp.status_code)
    # print(resp.text)
    player_data = resp.json()
    # print(type(player_data), player_data)
    players = [
        player_info(**pl)
        for pl in player_data
    ]

    # print("Found {} player with name {}".format(len(players), search_text))
    # for p in players:
    #     print(p)

    return players

def stat_query(player_name):
    query = None
    while query != 'x':
        print("a. Find player stats by game")
        print("b. Find player stats by season")
        print(" or type 'x' to go back")
        query = input()
        if query.lower() != 'x':
            if query.lower() == 'a':
                printers.stat_prompt()
                stat_query = input()
                while stat_query.lower() == 'help':
                    printers.help_stats()
                    printers.stat_prompt()
                    stat_query = input()

                # season_type = input("Would you like to see regular season or post-season stats? \n")
                game_year = input("Type the year the game was played: \n")
                game_week = input("Type the week the game was played: \n")
                stats_by_yr_week_statType(stat_query, player_name, game_year, game_week)


def stats_by_yr_week_statType(statType, name, year, week):
    name_split = name.split()
    first_name = name_split[0]
    last_name = name_split[1]
    url = 'http://api.suredbits.com/nfl/v0/stats/{}/{}/{}/{}/{}'.format(statType, last_name, first_name, year, week)
    resp = requests.get(url)

    if statType.lower() == 'passing':
        passing_data = resp.json()
        passing = results.passingStats(player_stats_passing, passing_data)
        print("Stats for {}".format(name))
        printers.print_passing_info(passing)
    elif statType.lower() == 'rushing':
        rushing_data = resp.json()
        rushing = results.rushingStats(player_stats_rushing, rushing_data)
        print("Stats for {}".format(name))
        printers.print_rushing_info(rushing)
    elif statType.lower() == 'receiving':
        receiving_data = resp.json()
        receiving = results.receivingStats(player_stats_receiving, receiving_data)
        print("Stats for {}".format(name))
        printers.print_receiving_info(receiving)
    elif statType.lower() == 'kick return':
        pass
    elif statType.lower() == 'fumbles':
        pass
    elif statType.lower() == 'defense':
        pass
    elif statType.lower() == 'kicking':
        pass
    elif statType.lower() == 'punting':
        pass