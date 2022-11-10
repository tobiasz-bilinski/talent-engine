import pytest
import time


@pytest.fixture(scope="session", autouse=True)
def time_elapsed_fixture():
    # Inspired by Kamil, it was just printing strings before and after yield but this is cooler :)
    time_start = time.time()
    yield
    time_elapsed = time.time() - time_start
    print(f"Time elapsed: {time_elapsed:.2f}s")
