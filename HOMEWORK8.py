import time

def measure_time(func, *args, **kwargs):
    """
    A function to measure the execution time of another function.

    Parameters:
    - func: The function whose execution time we want to measure.
    - *args: Positional arguments to pass to the function.
    - **kwargs: Key arguments to pass to a function.

    Returns:
    - elapsed_time: Function execution time in seconds.
    """
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time
def example_function():
    time.sleep(2)
    if __name__ == "__main__":
        measured_time = measure_time(example_function)
        print(f"Function execution time: {measured_time} seconds")