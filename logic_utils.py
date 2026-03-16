def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # #FIX: Refactored logic to fix Hard mode range using Copilot Agent mode
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 500  # Fixed: Hard should be a wider range, not smaller
    return 1, 100

def parse_guess(raw: str, low: int, high: int):
    """
    Parse user input into an int guess within specific bounds.
    """
    # FIXME: Logic breaks here 
    # Original code didn't take low/high arguments, making range-checking impossible here.
    
    if not raw or raw.strip() == "":
        return False, None, "Enter a guess."

    try:
        # #FIX: Added float-to-int handling and boundary validation using Copilot Agent mode
        value = int(float(raw))
    except (ValueError, TypeError):
        return False, None, "That is not a number."

    if value < low or value > high:
        return False, None, f"Out of range! Guess between {low} and {high}."

    return True, value, None

def check_guess(guess, secret):
    # #FIX: Flipped the 'Too High'/'Too Low' logic which was inverted using Copilot Agent mode
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Too High! Go LOWER!"
    return "Too Low", "📉 Too Low! Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    # #FIX: Simplified scoring logic to prevent negative scores using Copilot Agent mode
    if outcome == "Win":
        points = max(10, 100 - (10 * attempt_number))
        return current_score + points
    return current_score # Penalties can be added here if desired