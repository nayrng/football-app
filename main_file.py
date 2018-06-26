import player_searcher
import game_searcher
import requests
import printers

def searchPlayers():
    search = None
    while search != 'x':

        search = input("Which player would you like to search? (Enter a last name, or a full name) ")

        if search != 'x':
            search_split = search.split()

            if len(search_split) < 2:
                results = player_searcher.findPlayerLastName(search)
                print("Found {} results for last name {}".format(len(results), search))

                for p in results:
                    printers.print_player_info(p)



            elif len(search_split) == 2:
                results = player_searcher.findPlayerFullName(search_split)
                print("Found {} results for full name {}".format(len(results), search))
                for p in results:
                    printers.print_player_info(p)
                stats = input("Would you like to look at this player's stats? (y/n) ")
                if stats.lower() == 'y':
                    player_searcher.stat_query(search)


def searchTeam():
    pass


def searchGame():
    search = None
    while search != 'x':
        print("Usages: ")
        print("a. Look up all the GAMES for the current week")
        print("b. Look up all GAMES for a given TEAM for the current week")
        print("c. Look up all GAMES for a given TEAM for the given YEAR (regular season games only")
        print("d. Look up a specific GAME for a given TEAM for a given WEEK in a given YEAR")
        print("e. Look up all GAMES played in a given YEAR")
        print("f. Look up all GAMES played for a given WEEK in a given YEAR")

        search = input()
        if search != 'x':
            if search.lower() == 'a':
                pass
            elif search.lower() == 'b':
                pass
            elif search.lower() == 'c':
                pass
            elif search.lower() == 'd':
                printers.team_prompt()
                team = input()
                while team.lower() == 'help':
                    printers.team_help()
                    printers.team_prompt()
                    team = input()
                season = input("Please type what year the game was played in: ")
                week = input("Please type what week the game was played in: ")
                game_searcher.search_for_specific_game(team, season, week)
            elif search.lower() == 'e':
                pass
            elif search.lower() == 'f':
                pass



def searchMethod():
    query = None

    while query != 'x':

        print("Would you like to: ")
        print("a. Look up a NFL player")
        print("b. Look up a NFL Team")
        print("c. Look up a NFL game")
        print("\n or type 'x' to exit")

        query = input()

        if query.lower() == 'a':
            searchPlayers()
        elif query.lower() == 'b':
            searchTeam()
        elif query.lower() == 'c':
            searchGame()

    print("exiting...")


def main():
    searchMethod()


if __name__ == '__main__':
    main()
