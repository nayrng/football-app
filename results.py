# movies = []
# for md in movie_list:
#     m = MovieResult(
#         imdb_code=md.get("imdb_code"),
#         title=md.get("title"),
#         duration=md.get("duration"),
#         director=md.get("director"),
#         year=md.get("year", 0),
#         rating=md.get("rating", 0),
#         imdb_score=md.get("imdb_score", 0.0),
#         keywords=md.get("keywords"),
#         genres=md.get("genres")
#     )
#     movies.append(m)

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

def gameList(namedTuple, gameList):
    game = []
    for g in gameList:
        ga = namedTuple(
            seasonYear=g.get("seasonYear"),
            homeTeam=g.get("homeTeam"),
            awayTeam=g.get("awayTeam"),
            week=g.get("week"),
            seasonType=g.get("seasonType")
        )
    game.append(g)
    return game

def passingStats(namedTuple, gameList):
    stats = []
    for s in gameList:
        st = namedTuple(
            sack=s.get("sacks"),
            cmp=s.get("cmp"),
            passingTwoPointAttemptMade=s.get("passingTwoPointAttemptMade"),
            #cmpAirYds=s.get("cmpAirYds"),
            passingTwoPointAttempt=s.get("passingTwoPointAttempt"),
            passingInt=s.get("passingInt"),
            passingTds=s.get("passingTds"),
            att=s.get("att"),
            sackYds=s.get("sackYds"),
            #inCmpAirYds=s.get("inCmpAirYds"),
            #passingTwoPointAttemptMissed=s.get("passingTwoPointAttemptMissed"),
            inCmp=s.get("inCmp"),
            passingYds=s.get("passingYds")
        )
    stats.append(s)
    return stats

def rushingStats(namedTuple, gameList):
    stats = []
    for s in gameList:
        st = namedTuple(
            fumblesLost=s.get("fumblesLost"),
            rushingTwoPointAttemptMade=s.get("rushingTwoPointAttemptMade"),
            rushingYds=s.get("rushingYds"),
            # cmpAirYds=s.get("cmpAirYds"),
            tds=s.get("tds"),
            rushingTwoPointAttempt=s.get("rushingTwoPointAttempt"),
            loss=s.get("loss"),
            attempt=s.get("attempt"),
            lossYds=s.get("lossYds"),
        )
    stats.append(s)
    return stats

def receivingStats(namedTuple, gameList):
    stats = []
    for s in gameList:
        st = namedTuple(
            receivingTwoPointAttemptMade=s.get("receivingTwoPointAttemptMade"),
            fumblesLost=s.get("fumblesLost"),
            yacYds=s.get("yacYds"),
            tds=s.get("tds"),
            rec=s.get("rec"),
            target=s.get("target"),
            receivingYds=s.get("receivingYds"),
            receivingTwoPointAttempt=s.get("receivingTwoPointAttempt")

        )
    stats.append(s)
    return stats