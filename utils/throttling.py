from ratelimit import limits, sleep_and_retry
import threading
import time

# Constants
REQUESTS_PER_MINUTE = 10
TOKENS_PER_MINUTE = 250000

# Global token usage tracking
_token_lock = threading.Lock()
_token_window_start = time.time()
_token_usage = 0

@sleep_and_retry
@limits(calls=REQUESTS_PER_MINUTE, period=60)
def throttled_task(func, *args, tokens_used=0, **kwargs):
    """
    Decorator-style throttling wrapper.
    Applies both request rate-limiting and token usage limiting.
    
    Args:
        func: The function to wrap and call.
        tokens_used: Approximate tokens the task will consume.
    """
    global _token_usage, _token_window_start

    with _token_lock:
        current_time = time.time()

        # If more than a minute passed, reset the token counter
        if current_time - _token_window_start >= 60:
            _token_window_start = current_time
            _token_usage = 0

        # If token budget exceeded, wait
        while _token_usage + tokens_used > TOKENS_PER_MINUTE:
            sleep_time = 60 - (current_time - _token_window_start)
            if sleep_time > 0:
                print(f"⏳ Token limit reached. Sleeping for {sleep_time:.2f} seconds...")
                time.sleep(sleep_time)
                _token_window_start = time.time()
                _token_usage = 0
            else:
                break

        # Track token usage
        _token_usage += tokens_used

    # Call the wrapped function
    return func(*args, **kwargs)
