import random

# Card values used in a standard Blackjack deck.
CARDS = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a random card from the deck."""
    return random.choice(CARDS)


def calculate_score(cards):
    """Calculate and return the score for a hand."""
    score = sum(cards)

    # A two-card score of 21 is Blackjack.
    if score == 21 and len(cards) == 2:
        return 0

    # Change an Ace from 11 to 1 if the hand goes over 21.
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score


def compare(user_score, computer_score):
    """Compare the scores and return the game result."""
    if user_score > 21:
        return "You went over. You lose."
    if computer_score > 21:
        return "Computer went over. You win."
    if user_score == computer_score:
        return "Draw."
    if user_score == 0:
        return "Blackjack! You win."
    if computer_score == 0:
        return "Computer has blackjack. You lose."
    if user_score > computer_score:
        return "You win!"
    return "You lose."


def play_game():
    """Run one complete Blackjack game."""
    # Deal two cards to the player and the computer.
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # Allow the player to draw cards until they stop or go bust.
    while True:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Stop if either player has Blackjack or the user goes over 21.
        if user_score == 0 or computer_score == 0 or user_score > 21:
            break

        choice = input("Type 'y' to draw another card or 'n' to pass: ").lower()

        if choice == "y":
            user_cards.append(deal_card())
        else:
            break

    # The computer draws until its score is at least 17.
    while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    # Calculate final scores and display the result.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))


# Start a new game whenever the player chooses "y".
while input("\nPlay Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()