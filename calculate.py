''' TO DO
for map data, track W/L ratio with randoms for all amounts of randoms
perhaps keep persistent statistics and edit them with each submit instead of looping everytime
'''





'''ALL STATS TO TRACK

maps:
average KDA
W/L ratio
W/L ratio with randoms
round W/L ratio
round W/L ratio with randoms
games played

teammates:
W/L ratio
round W/L ratio
games played

randoms:
W/L ratio
round W/L ratio
games played
varied for each amount of randoms

overall:
KDA
W/L
round W/L
games played


% chance to win a particular game
'''


def init(matches: [object]):
    matches = matches


    #### MAP DATA ####
    class MapData:
        gwon = 0
        glost = 0
        gwon_random = 0
        glost_random =0
        rwon = 0
        rlost = 0
        rwon_random = 0
        rlost_random = 0
        total_games = 0
        kills = 0
        deaths = 0
        assists = 0

    map_dict = {
        'Bank': MapData(),
        'Border': MapData(),
        'Chalet': MapData(),
        'Club House': MapData(),
        'Coastline': MapData(),
        'Consulate': MapData(),
        'Hereford': MapData(),
        'House': MapData(),
        'Kafe Dostoyevsky': MapData(),
        'Oregon': MapData(),
        'Skyscraper': MapData(),
        'Theme Park': MapData(),
        'Villa': MapData(),
        'Fortress': MapData()
    }

    for match in matches:
        if match['gwon']:
            map_dict[match['map_name']].gwon += 1
        else:
            map_dict[match['map_name']].glost += 1
        map_dict[match['map_name']].rwon += match['rwon']
        map_dict[match['map_name']].rlost += match['rlost']
        if match['randoms'] > 0: # FIX THIS CONDITIONAL
                if match['gwon']:
                    map_dict[match['map_name']].gwon_random += 1
                else:
                    map_dict[match['map_name']].glost_random += 1
                map_dict[match['map_name']].rwon_random += match['rwon_random']
                map_dict[match['map_name']].rlost_random += match['rlost_random']
        map_dict[match['map_name']].total_games += 1
        map_dict[match['map_name']].kills += match['kills']
        map_dict[match['map_name']].deaths += match['deaths']
        map_dict[match['map_name']].assists += match['assists']





    #### TEAMMATE DATA ####
    class TeammateData:
        gwon = 0
        glost = 0
        rwon = 0
        rlost = 0
        total_games = 0

    teammate_dict = {
        'arnold': TeammateData(),
        'benji': TeammateData(),
        'charles': TeammateData(),
        'josh': TeammateData(),
        'juan': TeammateData(),
        'lloyd': TeammateData(),
        'lu': TeammateData(),
        'victor': TeammateData()
    }

    for match in matches:
        for tmate in match['teammates']:
            if match['gwon']:
                teammate_dict[tmate].gwon += 1
            else:
                teammate_dict[tmate].glost += 1
            teammate_dict[tmate].rwon += match['rwon']
            teammate_dict[tmate].rlost += match['rlost']
            teammate_dict[tmate].total_games += 1



    #### RANDOM DATA ####
    class RandomData:
        gwin = 0
        glost = 0
        rwon = 0
        rlost = 0
        total_games = 0

    random_dict =  {
        0: RandomData(),
        1: RandomData(),
        2: RandomData(),
        3: RandomData(),
        4: RandomData()
    }

    for match in matches:
        if match['gwin']:
            randoms_dict[match['randoms']].gwon += 1
        else:
            randoms_dict[match['randoms']].glost += 1
        randoms_dict[match['randoms']].rwon += match['rwon']
        randoms_dict[match['randoms']].rlost += match['rlost']
        randoms_dict[match['randoms']].total_games += 1



    #### OVERALL DATA ####
    overall_dict = {
        'gwon': 0,
        'glost': 0,
        'rwon': 0,
        'rlost': 0,
        'total_games': 0,
        'kills': 0,
        'deaths': 0,
        'assists': 0
    }

    for match in matches:
        if match['gwin']:
            overall_dict['gwon'] += 1
        else:
            overall_dict['glost'] += 1
        overall_dict['rwon'] += match['rwon']
        overall_dict['rlost'] += match['rlost']
        overall_dict['total_games'] += 1
        overall_dict['kills'] += match['kills']
        overall_dict['deaths'] += match['deaths']
        overall_dict['assists'] += match['assists']




    #### % CHANCES ####

    # how to do the math???