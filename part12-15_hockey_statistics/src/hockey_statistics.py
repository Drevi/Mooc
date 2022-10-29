# Write your solution here

import json

class HockeyStatisticApp:
    def __init__(self):
        self.__player_data = None

    def file_load(self, filename):
        with open(filename) as my_file:
            data = json.loads(my_file.read())
        print(f"read the data of {len(data)} players")
        return (data)

    def help(self):
        print("""
commands:
0 quit
1 search for player
2 teams
3 countries
4 players in team
5 players from country
6 most points
7 most goals
""")

    def execute(self):        
        self.__player_data = self.file_load(input("file name:"))
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                break
            if command == "1":
                self.search_player()
            if command == "2":
                self.sorted_list("team")
            if command == "3":
                self.sorted_list("nationality")
            if command == "4":
                self.players_in_team()
            if command == "5":
                self.players_from_country()
            if command == "6":
                self.most_points()
            if command == "7":
                self.most_goals()

    def print_player(self, player):
        print(f"{player['name']:21}{player['team']:3}{player['goals']:>4}{'+':>2}{player['assists']:>3}{'=':>2}{player['goals']+player['assists']:>4}")
    
    def search_player(self):
        player = input("name: ")
        player_data = list(filter(lambda x: x["name"] == player, self.__player_data))
        if len(player_data) == 0:
            print("player not found")
        else:
            self.print_player(player_data[0])

    def sorted_list(self, value):
        teams = sorted(set([player[value] for player in self.__player_data]))
        for team in teams:
            print(team)

    def points(self, player):
            return player["goals"] + player["assists"]

    def goals(self, player):
        return player["goals"]    

    def games(self, player):
        return player["games"]        

    def list_by_points(self, players: list):        
        return sorted(players, key=lambda i: (self.points(i), self.goals(i)), reverse=True )

    def list_by_goals(self, players: list):         
        return sorted(players, key=lambda i: (self.goals(i), -self.games(i)), reverse=True )

    def filter_team(self, players: list, team: str):
        return list(filter(lambda x: x["team"] == team, players))

    def filter_country(self, players: list, country: str):
        return list(filter(lambda x: x["nationality"] == country, players))
    
    def players_in_team(self):
        team = input("team: ")
        players = self.list_by_points(self.filter_team(self.__player_data, team))
        for player in players:
            self.print_player(player)

    def players_from_country(self):
        country = input("country: ")
        players = self.list_by_points(self.filter_country(self.__player_data, country))
        for player in players:
            self.print_player(player)

    def most_points(self):
        ammount = int(input("how many: "))
        players = self.list_by_points(self.__player_data)
        for player in players[0:ammount]:
            self.print_player(player) 

    def most_goals(self):
        ammount = int(input("how many: "))
        players = self.list_by_goals(self.__player_data)
        for player in players[0:ammount]:
            self.print_player(player)


program = HockeyStatisticApp()
program.execute()