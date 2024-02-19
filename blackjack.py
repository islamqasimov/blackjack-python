import random 

class Player:
    def __init__(self) -> None:
        self.hand = [] # A list to represent the player's hand

    def add_card(self, card): 
        # Function to adding new cards to hand
        self.hand.append(card)

    def calculate_hand_value(self): 
        # Logic to calculate hand's value
        value = 0
        for card in self.hand: # changing ranks to integer 
            if card['rank'] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card['rank'] == 'Ace' and value + 11 <= 21:
                value += 11
            elif card['rank'] == 'Ace' and value + 11 > 21:
                value += 1
            else:
                value += int(card['rank'])

        return value

    def display_hand(self): 
        # Displaying hand
        for card in self.hand:
            print(f"{card['rank']} of {card['suit']}") 

class Dealer:
    def __init__(self) -> None:
            self.hand = [] # A list to represent the dealer's hand

    def add_card(self, card): 
        # Function to adding new cards to hand
        self.hand.append(card)

    def calculate_hand_value(self): 
        # Logic to calculate hand's value
        value = 0
        for card in self.hand: # changing ranks to integer 
            if card['rank'] in ['Jack', 'Queen', 'King']:
                value += 10
            elif card['rank'] == 'Ace' and value + 11 <= 21:
                value += 11
            elif card['rank'] == 'Ace' and value + 11 > 21:
                value += 1
            else:
                value += int(card['rank'])

        return value

    def display_hand(self): 
        # Displaying hand
        for card in self.hand:
            print(f"{card['rank']} of {card['suit']}") 

class Deck:
    def __init__(self):
        # Create a standart deck of cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [{'rank': rank, 'suit' : suit} for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards) 

    def print_card(self):
        card = random.choice(self.cards)
        print(f"{card['rank']} of {card['suit']}")


class BlackjackGame:
    def __init__(self, playersNum):
        # Initialize game with the number of players
        self.deck = Deck() # a list to represent a deck of cards 
        self.players = [Player() for _ in range(playersNum)] # create player object
        self.dealer = Dealer() # create the dealer object 

    def start_game(self):
        # Method to start the game

        print("Shuffeling cards ...")
        self.deck.shuffle()

        print("Game started")

        print("Dealers first card is: ")
        self.deal_card(self.dealer)

        for i, player in enumerate(self.players, start=1):
            print("\n--------------------------------------------")
            print(f"Now playing \"Player {i}\"\n")

            self.deal_card(player) # \
                                    #   dealing first 2 cards to player
            self.deal_card(player) # / 

            if player.calculate_hand_value() == 21: # identify player future play capability
                play = False  
            else:
                play = True

            while play == True:
                play = input("\nDo you want to continue? (y/n): ") # Asking player if he wants to continue

                if play == 'y' and player.calculate_hand_value() < 21:
                    play = True
                    self.deal_card(player)
                else:
                    play = False

            print("\nPlayer's hand is:")
            player.display_hand()
            print(f"Hand's value: {player.calculate_hand_value()} ")

        print("\n--------------------------------------------\n Now THE DEALER comes")

        print("The DEALER'S second card is: ")
        self.deal_card(self.dealer)
        play = True
        while play == True:
            if self.dealer.calculate_hand_value() == 21:
                print("The DEALER got 21")
                play = False
            elif 21 > self.dealer.calculate_hand_value() > 16:
                print("The DEALER has to stop")
                play = False
            elif self.dealer.calculate_hand_value() <= 16:
                print("The DEALER has to grab a card")
                self.deal_card(self.dealer)
            else:
                print("The DEALER LOST")
                play = False

        print("\n================================================================")
        print("Dealer hand is:")

        self.dealer.display_hand()
        print(f"Dealer hand's value: {self.dealer.calculate_hand_value()} ")

        print("\n================================================================\n\nGAME STOPPED\n")

        print("The win/loss table:")

        for i, player in enumerate(self.players, start=1): 
            if self.dealer.calculate_hand_value() > player.calculate_hand_value() and self.dealer.calculate_hand_value() <= 21:
                print(f"\"Player {i}\" LOST\n")
            elif self.dealer.calculate_hand_value() < player.calculate_hand_value() and player.calculate_hand_value() <= 21:
                print(f"\"Player {i}\" WIN\n")
            else:
                print(f"\"Player {i}\" HAS A DRAW\n")

    def deal_card(self, player):
        # Method to deal a card to a player
        card = self.deck.cards.pop()
        print(f"{card['rank']} of {card['suit']}")
        player.add_card(card)

if __name__ == "__main__":
    game = BlackjackGame(int(input("How many players will play?: ")))
    game.start_game()
    