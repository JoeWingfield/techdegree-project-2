summary:
    To start I imported import random. The dunder main calls the menu function located at the top of the page, and this kicks off the game with a nice menu, and the choice to start or quit. When the player chooses start, it calls the choose_team function. This function asks what team the player would like to display. This function will then store the player's answer and call the display_stats function and bring the team_choice_answer variable with it. In the display_stats function it will define the total_players and player_names by calling the balance_teams function. In this function it will evenly distribute the players into the teams, and will store all the chosen player names into a list. The total players and player names will be returned to the function and defined in the display_stats function. Finally, the team_name, total_players, and player_names will be neatly displayed and then the program will prompt you to close.
