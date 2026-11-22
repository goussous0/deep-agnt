import time
def call_with_retry(fn, max_attempts=3, base_delay=1.0):
    """Call fn(), retrying transient failures with exponential backoff.

    Re-raise the last exception once max_attempts is exhausted.
    """
    exc = None    
    for i in range(max_attempts):
        try:
            result = fn()
            return result
        except (RateLimitError, TimeoutError, ServerError) as e:
             if i == max_attempts - 1:
                raise e
        sleep(base_delay * ( 2 ** i))
