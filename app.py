from constants import PLAYERS, TEAMS
import random


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
    exp_players = []
    inexp_players = []
    for player in PLAYERS:
        add_player_data = {}
        add_player_data["name"] = player["name"]
        if "and" in player["guardians"]:
            add_player_data["guardians"] = player["guardians"].split(' and ')
        else:
            add_player_data["guardians"] = [player["guardians"]]
        if player["experience"] == 'YES':
            add_player_data["experience"] = True
        else:
            add_player_data["experience"] = False
        add_player_data["height"] = int(player['height'].split(' ')[0])
        if add_player_data['experience'] is True:
            exp_players.append(add_player_data)
        else:
            inexp_players.append(add_player_data)
    return exp_players, inexp_players


def balance_teams():
    each_team_total = int(len(PLAYERS) / len(TEAMS))
    chosen_players = random.sample(PLAYERS, each_team_total)
    players = []
    for player in chosen_players:
        add_player_data = {}
        add_player_data = player["name"]
        players.append(add_player_data)
    return each_team_total, players


def display_stats(team_name):
    total_players, player_names = balance_teams()

    enter = input("""
    Team: {} Stats
    --------------
    Total players: {}
    Players:
      {}

    Press ENTER to continue... """.format(team_name, total_players, ', '.join(player_names)))
    if enter == "":
        exit()
    else:
        exit()


if __name__ == "__main__":
    menu()
