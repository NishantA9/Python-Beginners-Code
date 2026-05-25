"""Functions used in preparing Guido's gorgeous lasagna."""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    Parameters: elapsed_bake_time (int): The baking time already elapsed.
    Returns: int: The remaining bake time in minutes.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    Parameters: number_of_layers (int): The number of lasagna layers.
    Returns: int: The preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    Parameters:
        number_of_layers (int): The number of lasagna layers.
        elapsed_bake_time (int): The baking time already elapsed.
    Returns: int: The total elapsed cooking time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time