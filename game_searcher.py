import collections
import requests
import results
import printers

game_information = collections.namedtuple(
    "game_info",
    "seasonYear, homeTeam, awayTeam, week, seasonType"
)

# json_object = json.loads(resp .text)

def search_for_specific_game(team, year, week, boolean):
    url = 'http://api.suredbits.com/nfl/v0/games/{}/{}/{}'.format(team, year, week)
    resp = requests.get(url)
    game_data = resp.json()
    gameResults = results.gameList(game_information, game_data)
    if boolean:
        printers.print_game_info(gameResults)
    return gameResults


# def search_skeleton():
#     game_information = collections.namedtuple(
#         "game_info",
#         "seasonYear, homeTeam, awayTeam, week, seasonType"
#     )