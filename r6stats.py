import tkinter as tk
import utilities as util
import calculate as calc


'''TO DO
more info button
ALL info button
chances to win game (display math that goes with it. ie: % for map, % w/ teammates)
close button which saves all data
'''



# custom exceptions
class TeammateError(Exception):
    print ('ERROR: too many teammates')
class RoundError(Exception):
    print ('ERROR: round W/L results impossible')
class KDAError(Exception):
    print ('ERROR: negative KDA')



FILE_NAME = 'raw_data.json'
matches = util.load_file(FILE_NAME) if util.file_exists(FILE_NAME) else []


def submit():
    # saves all data into a MatchData object
    teammates = []
    for teammate in team_dict: # adds all teammates to the teammate dict
        if team_dict[teammate].get():
            teammates.append(teammate)

    gwon = False
    if rounds_won.get() == 5 or rounds_won.get() >= rounds_lost.get() + 2:
        gwon = True

    match_dict = {
        'map_name': map_listbox.get(map_listbox.curselection()) # string
        'teammates': teammates # [string]
        'randoms': 4 - len(teammates) # int
        'rwon': rounds_won.get() # int
        'rlost': rounds_lost.get() # int
        'gwon': gwon # bool
        'k': kills.get() # int
        'd': deaths.get() # int
        'a': assists.get() # int
    }

    try:
        if check(match_dict):
            matches.append(match_dict)
            util.write_file(FILE_NAME, matches)
            cleanup()
    except:
        pass


def check(match_dict) -> bool:    
    if len(match_dict['teammates']) > 4:
        raise TeammateError
    if match_dict['randoms'] > 4:
        raise TeammateError
    if match_dict['rwon'] == match_dict['rlost']:
        raise RoundError
    if match_dict['k'] < 0 or match_dict['d'] < 0 or match_dict['a'] < 0:
        raise KDAError
    return True


def cleanup():
    rwon1.deselect()
    rwon2.deselect()
    rwon3.deselect()
    rwon4.deselect()
    rwon5.deselect()

    rlost1.deselect()
    rlost2.deselect()
    rlost3.deselect()
    rlost4.deselect()
    rlost5.deselect()

    gwon_yes.deselect()
    gwon_no.deselect()

    kills_entry.delete(0, 'end')
    deaths_entry.delete(0, 'end')
    assists_entry.delete(0, 'end')









############################################################################
############################## GUI #########################################
############################################################################


# window
main_window = tk.Tk()

# map
map_frame = tk.Frame(main_window)
map_label = tk.Label(map_frame, text='Map:')
map_listbox = tk.Listbox(map_frame, selectmode='SINGLE', yscrollcommand=True)
map_listbox.insert(1, 'Bank')
map_listbox.insert(2, 'Border')
map_listbox.insert(3, 'Chalet')
map_listbox.insert(4, 'Club House')
map_listbox.insert(5, 'Coastline')
map_listbox.insert(6, 'Consulate')
map_listbox.insert(7, 'Hereford')
map_listbox.insert(8, 'House')
map_listbox.insert(9, 'Kafe Dostoyevsky')
map_listbox.insert(10, 'Oregon')
map_listbox.insert(11, 'Skyscraper')
map_listbox.insert(12, 'Theme Park')
map_listbox.insert(13, 'Villa')
map_listbox.insert(14, 'Fortress')

# teammate variables
team_dict = {
    'arnold': tk.BooleanVar(),
    'benji': tk.BooleanVar(),
    'charles': tk.BooleanVar(),
    'josh': tk.BooleanVar(),
    'juan': tk.BooleanVar(),
    'lloyd': tk.BooleanVar(),
    'lu': tk.BooleanVar(),
    'victor': tk.BooleanVar()
}

# teammate checkbuttons
teammate_frame = tk.Frame(main_window)
teammate_label = tk.Label(teammate_frame, text='Teammates:')
arnold_checkbutton = tk.Checkbutton(teammate_frame, text='arnold', variable=team_dict['arnold'], onvalue=True, offvalue=False)
benji_checkbutton = tk.Checkbutton(teammate_frame, text='benji', variable=team_dict['benji'], onvalue=True, offvalue=False)
charles_checkbutton = tk.Checkbutton(teammate_frame, text='charles', variable=team_dict['charles'], onvalue=True, offvalue=False)
josh_checkbutton = tk.Checkbutton(teammate_frame, text='josh', variable=team_dict['josh'], onvalue=True, offvalue=False)
juan_checkbutton = tk.Checkbutton(teammate_frame, text='juan', variable=team_dict['juan'], onvalue=True, offvalue=False)
lloyd_checkbutton = tk.Checkbutton(teammate_frame, text='lloyd', variable=team_dict['lloyd'], onvalue=True, offvalue=False)
lu_checkbutton = tk.Checkbutton(teammate_frame, text='lu', variable=team_dict['lu'], onvalue=True, offvalue=False)
victor_checkbutton = tk.Checkbutton(teammate_frame, text='victor', variable=team_dict['victor'], onvalue=True, offvalue=False)

# rounds won
rwon_frame = tk.Frame(main_window)
rwon_label = tk.Label(rwon_frame, text='Rounds Won?')
rounds_won = tk.IntVar()
rwon0 = tk.Radiobutton(rwon_frame, text='0', variable=rounds_won, value=0)
rwon1 = tk.Radiobutton(rwon_frame, text='1', variable=rounds_won, value=1)
rwon2 = tk.Radiobutton(rwon_frame, text='2', variable=rounds_won, value=2)
rwon3 = tk.Radiobutton(rwon_frame, text='3', variable=rounds_won, value=3)
rwon4 = tk.Radiobutton(rwon_frame, text='4', variable=rounds_won, value=4)
rwon5 = tk.Radiobutton(rwon_frame, text='5', variable=rounds_won, value=5)

# rounds lost
rlost_frame = tk.Frame(main_window)
rlost_label = tk.Label(rlost_frame, text='Rounds Lost?')
rounds_lost = tk.IntVar()
rlost0 = tk.Radiobutton(rlost_frame, text='0', variable=rounds_lost, value=0)
rlost1 = tk.Radiobutton(rlost_frame, text='1', variable=rounds_lost, value=1)
rlost2 = tk.Radiobutton(rlost_frame, text='2', variable=rounds_lost, value=2)
rlost3 = tk.Radiobutton(rlost_frame, text='3', variable=rounds_lost, value=3)
rlost4 = tk.Radiobutton(rlost_frame, text='4', variable=rounds_lost, value=4)
rlost5 = tk.Radiobutton(rlost_frame, text='5', variable=rounds_lost, value=5)

# KDA
kills_frame = tk.Frame(main_window)
kills_label = tk.Label(kills_frame, text='kills:')
kills = tk.StringVar()
kills_entry = tk.Entry(kills_frame, textvariable=kills)

deaths_frame = tk.Frame(main_window)
deaths_label = tk.Label(deaths_frame, text='deaths:')
deaths = tk.StringVar()
deaths_entry = tk.Entry(deaths_frame, textvariable=deaths)

assists_frame = tk.Frame(main_window)
assists_label = tk.Label(assists_frame, text='assists:')
assists = tk.StringVar()
assists_entry = tk.Entry(assists_frame, textvariable=assists)

# submit button
submit_button = tk.Button(main_window, text='Submit', command=submit)



# pack
map_frame.pack()
teammate_frame.pack()
rwon_frame.pack()
rlost_frame.pack()
gwon_frame.pack()
kills_frame.pack()
deaths_frame.pack()
assists_frame.pack()

map_label.pack()
map_listbox.pack()

teammate_label.pack()
arnold_checkbutton.pack(side='left')
benji_checkbutton.pack(side='left')
charles_checkbutton.pack(side='left')
josh_checkbutton.pack(side='left')
juan_checkbutton.pack(side='left')
lloyd_checkbutton.pack(side='left')
lu_checkbutton.pack(side='left')
victor_checkbutton.pack(side='left')
submit_button.pack(side='left')

rwon_label.pack(side='left')
rwon0.pack(side='left')
rwon1.pack(side='left')
rwon2.pack(side='left')
rwon3.pack(side='left')
rwon4.pack(side='left')
rwon5.pack(side='left')

rlost_label.pack(side='left')
rlost0.pack(side='left')
rlost1.pack(side='left')
rlost2.pack(side='left')
rlost3.pack(side='left')
rlost4.pack(side='left')
rlost5.pack(side='left')

kills_label.pack(side='left')
kills_entry.pack(side='left')
assists_label.pack(side='left')
assists_entry.pack(side='left')
deaths_label.pack(side='left')
deaths_entry.pack(side='left')

submit_button.pack(side='bottom')







main_window.mainloop()