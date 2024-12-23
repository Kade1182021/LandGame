import random

class Player:
    def __init__(self, name):
        self.name = name
        self.deck = {"R": 10, "G": 10, "B": 10}
        self.hand = {"R": 0, "G": 0, "B": 0}
        self.tableau = {"R": 0, "G": 0, "B": 0}
        self.graveyard = {"R": 0, "G": 0, "B": 0}
        self.shuffle_deck()

    def shuffle_deck(self):
        deck_cards = []
        for card, count in self.deck.items():
            deck_cards.extend([card] * count)
        random.shuffle(deck_cards)
        self.deck = {"R": 0, "G": 0, "B": 0}
        for card in deck_cards:
            self.deck[card] += 1

    def draw_card(self):
        # Calculate the total number of cards left in the deck
        total_cards = sum(self.deck.values())
        
        # If the deck is empty, do nothing
        if total_cards == 0:
            return

        # Create a list of card types and their corresponding probabilities
        card_types = list(self.deck.keys())
        probabilities = [self.deck[card_type] / total_cards for card_type in card_types]

        # Randomly choose a card type based on the probabilities
        chosen_card = random.choices(card_types, weights=probabilities, k=1)[0]

        # Update the deck and hand
        self.deck[chosen_card] -= 1
        self.hand[chosen_card] += 1

    def play_card(self, card_type):
        card_type = card_type.upper()
        if self.hand.get(card_type, 0) > 0:
            self.hand[card_type] -= 1
            return card_type
        return None

    def check_win(self):
        return (
            all(count > 0 for count in self.tableau.values())  # One card of each type
            or max(self.tableau.values()) >= 5  # Five of one type
        )

    def format_cards(self, cards):
        return ", ".join([f"{card}x{count}" for card, count in cards.items() if count > 0])

class Game:
    def __init__(self):
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.current_player = self.player1
        self.opponent = self.player2
        self.turn = 1

    def start_game(self):
        for _ in range(5):
            self.player1.draw_card()
            self.player2.draw_card()
        self.play_game()

    def play_game(self):
        while True:
            self.show_game_state()
            
            # Handle draw step (skipped on Player 1's first turn)
            if not (self.turn == 1 and self.current_player == self.player1):
                self.current_player.draw_card()
            
            # Show hand and prompt action
            print(f"{self.current_player.name}'s turn.")
            self.show_hand()
            
            card = input("Choose a card to play (R, G, or B): ").strip().upper()
            if card not in ["R", "G", "B"]:
                print("Invalid input. Please choose R, G, or B.")
                continue
            
            played_card = self.current_player.play_card(card)
            if not played_card:
                print("You don't have that card in your hand.")
                continue

            self.resolve_card_effect(played_card)
            self.current_player.tableau[played_card] += 1
            
            if self.current_player.check_win():
                print(f"{self.current_player.name} wins!")
                break
            
            self.current_player, self.opponent = self.opponent, self.current_player
            self.turn += 1

    def resolve_card_effect(self, card):
        if card == "R":
            for card_type in ["R", "G", "B"]:
                if self.opponent.tableau[card_type] > 0:
                    print(f"{self.current_player.name} removes a card from {self.opponent.name}'s tableau.")
                    self.opponent.tableau[card_type] -= 1
                    self.opponent.graveyard[card_type] += 1
                    break
        elif card == "G":
            for card_type in ["R", "G", "B"]:
                if self.current_player.graveyard[card_type] > 0:
                    print(f"{self.current_player.name} brings a card back from their graveyard to their hand.")
                    self.current_player.graveyard[card_type] -= 1
                    self.current_player.hand[card_type] += 1
                    break
        elif card == "B":
            print(f"{self.current_player.name} forces {self.opponent.name} to discard a card.")
            while True:
                self.show_opponent_hand()
                card_to_discard = input(f"Choose a card for {self.opponent.name} to discard (R, G, or B): ").strip().upper()
                if card_to_discard in ["R", "G", "B"] and self.opponent.hand[card_to_discard] > 0:
                    self.opponent.hand[card_to_discard] -= 1
                    self.opponent.graveyard[card_to_discard] += 1
                    break
                print("Invalid choice. Please choose a valid card type from the opponent's hand.")
    
    def show_game_state(self):
        print("\nGame State:")
        for player in [self.player1, self.player2]:
            print(f"{player.name}:")
            print(f"  Tableau: {player.format_cards(player.tableau)}")
            print(f"  Graveyard: {player.format_cards(player.graveyard)}")
            print(f"  Hand: {player.format_cards(player.hand)}")  # Display each player's hand
        print("-" * 20)
    
    def show_opponent_hand(self):
        print(f"{self.opponent.name}'s Hand: {self.opponent.format_cards(self.opponent.hand)}")

    def show_hand(self):
        print(f"{self.current_player.name}'s Hand: {self.current_player.format_cards(self.current_player.hand)}")

# Start the game
if __name__ == "__main__":
    game = Game()
    game.start_game()
