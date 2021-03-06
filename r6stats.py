import tkinter as tk
from datetime import datetime
import utilities as util
import calculate as calc
import dbhandler as db


'''TO DO
more info button
ALL info button
chances to win game (display math that goes with it. ie: % for map, % w/ teammates)
close button which saves all data
'''



# custom exceptions
class TeammateError(Exception):
    pass
    # print ('ERROR: too many teammates')
class RoundError(Exception):
    pass
    # print ('ERROR: round W/L results impossible')
class KDAError(Exception):
    pass
    # print ('ERROR: negative KDA')



def submit():
    # saves all data into a MatchData object
    date = datetime.today().strftime('%m-%d-%Y') # string
    map_name = map_listbox.get(map_listbox.curselection())
    teammates = []
    for teammate in team_dict: # adds all teammates to the teammate dict
        if team_dict[teammate].get():
            teammates.append(teammate)
    while(len(teammates) != 4):
        teammates.append('random')
    rwon = rounds_won.get()
    rlost = rounds_lost.get()
    gwon = 'true' if rounds_won.get() == 5 or rounds_won.get() >= rounds_lost.get() + 2 else 'false'
    k = kills.get()
    d = deaths.get()
    a = assists.get()


    try:
        if len(teammates) > 4:
            raise TeammateError
        if rwon == rlost:
            raise RoundError
        if k < 0 or d < 0 or a < 0:
            raise KDAError

        db.add_raw_data(date, map_name, teammates, rwon, rlost, gwon, k, d, a)
        db.add_general_data(gwon, rwon, rlost, k, d, a)
        db.add_map_data(map_name, gwon, rwon, rlost, k, d, a)
        for tmate in teammates:
            if tmate != 'random':
                db.add_teammate_data(tmate, gwon, rwon, rlost, k, d, a)
        db.add_random_data(teammates.count('random'), gwon, rwon, rlost, k, d, a)
        print('submitted')
        cleanup()

    except TeammateError:
        print('ERROR: CHECK TEAMMATE COUNT')
    except RoundError:
        print('ERROR: CHECK ROUND COUNT')
    except KDAError:
        print('ERROR: CHECK NEG KDA')
    except:
        print('ERROR: OTHER')



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
kills = tk.IntVar()
kills_entry = tk.Entry(kills_frame, textvariable=kills)

assists_frame = tk.Frame(main_window)
assists_label = tk.Label(assists_frame, text='assists:')
assists = tk.IntVar()
assists_entry = tk.Entry(assists_frame, textvariable=assists)

deaths_frame = tk.Frame(main_window)
deaths_label = tk.Label(deaths_frame, text='deaths:')
deaths = tk.IntVar()
deaths_entry = tk.Entry(deaths_frame, textvariable=deaths)


# submit button
submit_button = tk.Button(main_window, text='Submit', command=submit)



# pack
map_frame.pack()
teammate_frame.pack()
rwon_frame.pack()
rlost_frame.pack()
kills_frame.pack()
assists_frame.pack()
deaths_frame.pack()

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