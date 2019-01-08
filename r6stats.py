import tkinter as tk
import utilities as util


'''TO DO
error messages in check()
try and catch block to catch common errors
save and load data
stats
'''


class MatchData:
    def __init__(self, map_name: str, teammates: [str], randoms: int, rwon: int, rlost: int, gwin: bool, kills: int, deaths: int, assists: int):
        self.map_name = map_name
        self.teammates = teammates
        self.randoms = randoms
        self.rwon = rwon
        self.rlost = rlost
        self.gwin = gwin
        self.kills = kills
        self.deaths = deaths
        self.assists = assists


matches = [] # list of MatchData objects


def submit():
    # saves all data into a MatchData object
    map_name = map_listbox.get(map_listbox.curselection())
    teammates = []
    for teammate in team_dict: # adds all teammates to the teammate dict
        if team_dict[teammate].get():
            teammates.append(teammate)
    randoms = 4 - len(teammates)
    rwon = rounds_won.get()
    rlost = rounds_lost.get()
    gwin = win.get()
    k = kills.get()
    d = deaths.get()
    a = assists.get()

    if check(map_name, teammates, randoms, rwon, rlost, gwin, k, d, a):
        matches.append(MatchData(map_name, teammates, randoms, rwon, rlost, gwin, k, d, a))
        cleanup()
        print(matches[0].map_name)
        print(matches[0].teammates)
        print(matches[0].randoms)
        print(matches[0].rwon)
        print(matches[0].rlost)
        print(matches[0].gwin)
        print(matches[0].kills)
        print(matches[0].deaths)
        print(matches[0].assists)


def check(map_name, teammates, randoms, rwon, rlost, gwin, k, d, a):
    if len(teammates) > 4:
        return False
    if randoms > 4:
        return False
    if rwon == rlost:
        return False
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

    gwin_yes.deselect()
    gwin_no.deselect()

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
rwon1 = tk.Radiobutton(rwon_frame, text='1', variable=rounds_won, value=1)
rwon2 = tk.Radiobutton(rwon_frame, text='2', variable=rounds_won, value=2)
rwon3 = tk.Radiobutton(rwon_frame, text='3', variable=rounds_won, value=3)
rwon4 = tk.Radiobutton(rwon_frame, text='4', variable=rounds_won, value=4)
rwon5 = tk.Radiobutton(rwon_frame, text='5', variable=rounds_won, value=5)

# rounds lost
rlost_frame = tk.Frame(main_window)
rlost_label = tk.Label(rlost_frame, text='Rounds Lost?')
rounds_lost = tk.IntVar()
rlost1 = tk.Radiobutton(rlost_frame, text='1', variable=rounds_lost, value=1)
rlost2 = tk.Radiobutton(rlost_frame, text='2', variable=rounds_lost, value=2)
rlost3 = tk.Radiobutton(rlost_frame, text='3', variable=rounds_lost, value=3)
rlost4 = tk.Radiobutton(rlost_frame, text='4', variable=rounds_lost, value=4)
rlost5 = tk.Radiobutton(rlost_frame, text='5', variable=rounds_lost, value=5)

# W/L?
gwin_frame = tk.Frame(main_window)
gwin_label = tk.Label(gwin_frame, text='Overall Win or Loss?')
win = tk.BooleanVar()
gwin_yes = tk.Radiobutton(gwin_frame, text='win', variable=win, value=True)
gwin_no = tk.Radiobutton(gwin_frame, text='loss', variable=win, value=False)

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
gwin_frame.pack()
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
rwon1.pack(side='left')
rwon2.pack(side='left')
rwon3.pack(side='left')
rwon4.pack(side='left')
rwon5.pack(side='left')

rlost_label.pack(side='left')
rlost1.pack(side='left')
rlost2.pack(side='left')
rlost3.pack(side='left')
rlost4.pack(side='left')
rlost5.pack(side='left')

gwin_label.pack(side='left')
gwin_yes.pack(side='left')
gwin_no.pack(side='left')

kills_label.pack(side='left')
kills_entry.pack(side='left')
deaths_label.pack(side='left')
deaths_entry.pack(side='left')
assists_label.pack(side='left')
assists_entry.pack(side='left')

submit_button.pack(side='bottom')







main_window.mainloop()