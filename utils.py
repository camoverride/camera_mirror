import time
from functools import wraps



def retry_on_failure(max_attempts=3, delay_seconds=1):
    """
    A decorator to retry a function if it fails.

    Args:
    max_attempts (int): Maximum number of attempts to run the function.
    delay_seconds (int): Delay between retries in seconds.

    Returns:
    function: A wrapper function that incorporates the retry logic.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Attempt {attempts}/{max_attempts} failed with error: {e}")
                    if attempts < max_attempts:
                        print(f"Retrying in {delay_seconds} seconds...")
                        time.sleep(delay_seconds)
                    else:
                        print("Max retry attempts reached, function failed.")
        return wrapper
    return decorator
