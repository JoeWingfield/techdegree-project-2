import constants
import random
import copy


replay = []
replayed = 1
my_teams = copy.deepcopy(constants.TEAMS)
my_players = copy.deepcopy(constants.PLAYERS)
store_cleaned_players = []


def menu():
    game_running = True
    while game_running:
        try:
            menu_choice = int(input("""
            BASKETBALL TEAM STATS TOOL
            -----------MENU-----------
             Here are your choices:
              1) Display Team Stats
              2) Quit
            Enter an option > """))
            if menu_choice == 1:
                choose_team()
                game_running = False
            if menu_choice == 2:
                print("Goodbye")
                exit()
            if menu_choice > 2:
                raise ValueError
            if menu_choice < 1:
                raise ValueError
        except ValueError:
            print("Please choose a valid option")
        
        
def choose_team():
    game_running = True
    while game_running:
        try:
            team_choice = int(input("""
            1) Panthers
            2) Bandits
            3) Warriors
            
            Enter an option > """))
            if team_choice == 1:
                team_choice_answer = "Panthers"
                display_stats(team_choice_answer)
                game_running = False
            if team_choice == 2:
                team_choice_answer = "Bandits"
                display_stats(team_choice_answer)
                game_running = False
            if team_choice == 3:
                team_choice_answer = "Warriors"
                display_stats(team_choice_answer)
                game_running = False
            if team_choice > 3:
                raise ValueError
            if team_choice < 1:
                raise ValueError
        except ValueError:
            print("Please choose a valid option")
            
            
def clean_data():
    if len(replay) == 0:
        cleaned_players = []
        for data in my_players:
            add_player_data = {}
            add_player_data['name'] = data['name']
            if data['experience'] == 'YES':
                add_player_data['experience'] = True
            else:
                add_player_data['experience'] = False
            add_player_data["height"] = int(data['height'].split(' ')[0])
            cleaned_players.append(add_player_data)
    else:
        cleaned_players = store_cleaned_players[0].copy()
    return cleaned_players
    
    
def balance_teams():
    cleaned_players = clean_data()
    each_team_total = int(len(cleaned_players) / len(my_teams))
    if len(replay) == 0:
        shuffled_players = random.shuffle(cleaned_players)
        store_cleaned_players.append(cleaned_players.copy())
    player_names = []
    for player in cleaned_players:
        add_player_data = {}
        add_player_data = player["name"]
        player_names.append(add_player_data)
    panthers = []
    panthers.append(player_names[0:each_team_total])
    bandits = []
    bandits.append(player_names[each_team_total:each_team_total * 2])
    warriors = []
    warriors.append(player_names[each_team_total * 2:each_team_total * 3])
    return panthers, bandits, warriors, each_team_total
    
            
def display_stats(team_name):
    panthers, bandits, warriors, total_players = balance_teams()
    if team_name == "Panthers":
        player_names = ', '.join(panthers[0][0:total_players])
    if team_name == "Bandits":
        player_names = ', '.join(bandits[0][0:total_players])
    if team_name == "Warriors":
        player_names = ', '.join(warriors[0][0:total_players])
    choice = input("""
    Team {} Stats:
    --------------
    Total players: {}
    Players:
      {}
    
    Press ENTER to continue... """.format(team_name, total_players, player_names))
    if choice == "":
        replay.append(replayed)
        menu()
    else:
        exit()

        
if __name__ == "__main__":
    menu()
    
    
    
    
    
    
