import datetime

class PlayerRecord():
    # Use a class to represent a player as a record
    
    def __init__(self):
        self.player_number = None
        self.first_name = None
        self.last_name = None
        self.date_of_birth = None
        self.position = None
        self.injured = None
    
def main():
    # Create a player record and store the player details
    
    player1 = PlayerRecord()
    # Create a new player record
    
    player1.player_number = 1
    player1.first_name = 'Mpho'
    player1.last_name = 'Ramolefhe'
    player1.date_of_birth = datetime.datetime(2007, 7, 4)
    player1.position = 'Board 1'
    player1.injured = False
    
    print('### Player Record ###')
    print(f'Name: {player1.first_name} {player1.last_name}')
    print(f'Position {player1.position}')
    
main()