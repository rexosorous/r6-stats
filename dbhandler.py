import sqlite3

conn = sqlite3.connect('r6stats.db')
c = conn.cursor()



def add_raw_data (date, map_name, teammate_list, rwon, rlost, gwon, k, d, a):
    c.execute(f"""INSERT INTO raw_data VALUES(
        '{date}', 
        '{map_name}', 
        '{teammate_list[0]}',
        '{teammate_list[1]}',
        '{teammate_list[2]}',
        '{teammate_list[3]}', 
        {rwon}, 
        {rlost}, 
        '{gwon}', 
        {k}, 
        {d}, 
        {a})""")



def add_general_data(gwon, rwon, rlost, k, d, a):
    games_won = 1 if gwon == 'true' else 0
    games_lost = 1 if gwon == 'false' else 0
    c.execute(f"""UPDATE general_data SET
        total_games = total_games + 1,
        games_won = games_won + {games_won},
        games_lost = games_lost + {games_lost},
        rounds_won = rounds_won + {rwon},
        rounds_lost = rounds_lost + {rlost},
        kills = kills + {k},
        deaths = deaths + {d},
        assists = assists + {a}
        """)



def add_map_data(map_name, gwon, rwon, rlost, k, d, a):
    games_won = 1 if gwon == 'true' else 0
    games_lost = 1 if gwon == 'false' else 0
    c.execute(f"""UPDATE map_data SET
        total_games = total_games + 1,
        games_won = games_won + {games_won},
        games_lost = games_lost + {games_lost},
        rounds_won = rounds_won + {rwon},
        rounds_lost = rounds_lost + {rlost},
        kills = kills + {k},
        deaths = deaths + {d},
        assists = assists + {a}
        WHERE map_name = '{map_name}'
        """)



def add_teammate_data(teammate, gwon, rwon, rlost, k, d, a):
    games_won = 1 if gwon == 'true' else 0
    games_lost = 1 if gwon == 'false' else 0
    c.execute(f"""UPDATE teammate_data SET
        total_games = total_games + 1,
        games_won = games_won + {games_won},
        games_lost = games_lost + {games_lost},
        rounds_won = rounds_won + {rwon},
        rounds_lost = rounds_lost + {rlost},
        kills = kills + {k},
        deaths = deaths + {d},
        assists = assists + {a}
        WHERE teammate = '{teammate}'
        """)



def add_random_data(random_count, gwon, rwon, rlost, k, d, a):
    games_won = 1 if gwon == 'true' else 0
    games_lost = 1 if gwon == 'false' else 0
    c.execute(f"""UPDATE random_data SET
        total_games = total_games + 1,
        games_won = games_won + {games_won},
        games_lost = games_lost + {games_lost},
        rounds_won = rounds_won + {rwon},
        rounds_lost = rounds_lost + {rlost},
        kills = kills + {k},
        deaths = deaths + {d},
        assists = assists + {a}
        WHERE random_count = {random_count}
        """)