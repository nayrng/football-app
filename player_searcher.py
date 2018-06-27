import collections
import requests
import results
import printers
import game_searcher

player_info = collections.namedtuple(
    "player_info",
    "weight, profileId, uniformNumber, fullName, height, lastName, firstName, birthDate, profileUrl, status, team, position, yearsPro, college"

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

player_stats_defensive = collections.namedtuple(
    "player_stats_defensive",
    "tackleLoss, recoveredFumbles, assistedTackles, tackleLossYards, qbHit, miscTds, defenseInt, defenseSack, intTds, recoveredFumbleTD, tacklePrimary, defenseSackYds, tackle, safety, passDef, intYds, forcedFumbles"
)


# TODO: Some players don't have teams, uniform numbers, etc. Fix Later
def findPlayerLastName(search_text):
    url = 'http://api.suredbits.com/nfl/v0/players/{}'.format(search_text)
    resp = requests.get(url)
    print(resp.status_code)
    player = resp.json()
    player_data = results.playerInfo(player_info, player)
    yield player_data


def findPlayerFullName(search_text):
    url = 'http://api.suredbits.com/nfl/v0/players/{}/{}'.format(search_text[1], search_text[0])
    resp = requests.get(url)
    print(resp.status_code)
    # print(resp.text)
    player = resp.json()
    player_data = results.playerInfo(player_info, player)

    return player_data


def stat_grabber(statType, name, year, week, singleGame):
    name_split = name.split()
    first_name = name_split[0]
    last_name = name_split[1]

    url = None
    if singleGame:
        url = 'http://api.suredbits.com/nfl/v0/stats/{}/{}/{}/{}/{}'.format(statType, last_name, first_name, year, week)
    elif not singleGame:
        url = 'http://api.suredbits.com/nfl/v0/stats/{}/{}/{}'.format(last_name, first_name, year)
    resp = requests.get(url)

    if statType.lower() == 'passing':
        passing_data = resp.json()
        passing = results.passingStats(player_stats_passing, passing_data)
        return passing

    elif statType.lower() == 'rushing':
        rushing_data = resp.json()
        rushing = results.rushingStats(player_stats_rushing, rushing_data)
        return rushing

    elif statType.lower() == 'receiving':
        receiving_data = resp.json()
        receiving = results.receivingStats(player_stats_receiving, receiving_data)
        return receiving

    elif statType.lower() == 'defensive':
        defensive_data = resp.json()
        defensive = results.defensiveStats(player_stats_defensive, defensive_data)
        return defensive


def stat_query(player_name, player_results):
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
                if stat_query.lower() == 'all' or stat_query == '':
                    pos_query = input("Offensive or defensive stats? ")
                    if pos_query.lower().strip() == 'offense' or pos_query.lower() == 'offensive':
                        game_year = input("Type the year the game was played: \n")
                        game_week = input("Type the week the game was played: \n")
                        print("\n\n")
                        print("Week {} of the {} NFL Season\n".format(game_week, game_year))
                        teams = game_searcher.search_for_specific_game(player_results[0]['team'], game_year, game_week,
                                                                       False)

                        print("{} at {}\n".format(teams[0]['awayTeam']['team'], teams[0]['homeTeam']['team']))

                        if player_results[0]['position'] == 'QB':
                            QB_pass_stats = stat_grabber('passing', player_name, game_year, game_week, True)
                            printers.print_passing_info(QB_pass_stats)
                            print()
                            QB_rush_stats = stat_grabber('rushing', player_name, game_year, game_week, True)
                            printers.print_rushing_info(QB_rush_stats)
                        elif player_results[0]['position'] == 'RB':
                            RB_rush_stats = stat_grabber('rushing', player_name, game_year, game_week, True)
                            printers.print_rushing_info(RB_rush_stats)
                            print()
                            RB_receive_stats = stat_grabber('receiving', player_name, game_year, game_week, True)
                            printers.print_receiving_info(RB_receive_stats)
                        elif player_results[0]['position'] == 'WR':
                            WR_receive_stats = stat_grabber('receiving', player_name, game_year, game_week, True)
                            printers.print_receiving_info(WR_receive_stats)
                            print()
                            WR_rush_stats = stat_grabber('rushing', player_name, game_year, game_week, True)
                            printers.print_rushing_info(WR_rush_stats)
                    elif pos_query.lower().strip() == 'defense' or pos_query.lower().strip() == 'defensive':
                        game_year = input("Type the year the game was played: \n")
                        game_week = input("Type the week the game was played: \n")
                        teams = game_searcher.search_for_specific_game(player_results[0]['team'], game_year, game_week, False)

                        print("{} at {}\n".format(teams[0]['awayTeam']['team'], teams[0]['homeTeam']['team']))

                        printers.print_defensive_info(stat_grabber('defensive', player_name, game_year, game_week, True))

            elif query.lower() == 'b':
                printers.stat_prompt()
                stat_query = input()
                while stat_query.lower() == 'help':
                    printers.help_stats()
                    printers.stat_prompt()
                    stat_query = input()
                if stat_query.lower() == 'all' or stat_query == '':
                    pos_query = input("Offensive or defensive stats? ")
                    season_year = input("Type the year this player played in: ")
                    if pos_query.lower().strip() == 'offense' or pos_query.lower() == 'offensive':

                        print("\n\n")

                        if player_results[0]['position'] == 'QB':
                            QB_pass_stats = stat_grabber('passing', player_name, season_year, 0, False)
                            printers.fullprint_passing_info(QB_pass_stats)
                            print()
                            QB_rush_stats = stat_grabber('rushing', player_name, season_year, 0, False)
                            printers.fullprint_rushing_info(QB_rush_stats)
                        elif player_results[0]['position'] == 'RB':
                            RB_rush_stats = stat_grabber('rushing', player_name, season_year, 0, False)
                            printers.fullprint_rushing_info(RB_rush_stats)
                            print()
                            RB_receive_stats = stat_grabber('receiving', player_name, season_year, 0, False)
                            printers.fullprint_receiving_info(RB_receive_stats)
                        elif player_results[0]['position'] == 'WR':
                            WR_receive_stats = stat_grabber('receiving', player_name, season_year, 0, False)
                            printers.fullprint_receiving_info(WR_receive_stats)
                            print()
                            WR_rush_stats = stat_grabber('rushing', player_name, season_year, 0, False)
                            printers.fullprint_rushing_info(WR_rush_stats)
                        else:
                            print("error")
                    elif pos_query.lower().strip() == 'defense' or pos_query.lower().strip() == 'defensive':
                        print("\n\n")
                        printers.fullprint_defensive_info(stat_grabber('defensive', player_name, season_year, 0, False))