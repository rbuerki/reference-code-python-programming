import concurrent.futures
import os
import shelve
import time


def double_the_price_slowly(x):
    print(f"Process {os.getpid()}: Fetching and processing item ...")
    time.sleep(1)
    result = {"album": x["album"], "d_price": x["preis"] * 2}
    print(f"Process {os.getpid()}: Finished processing of album {x['album']}")
    return result


if __name__ == "__main__":

    with shelve.open("data/record_shelf", "r") as shelf:
        records = shelf["records"]

    start = time.time()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # with concurrent.futures.ProcessPoolExecutor() as executor:
        _ = executor.map(double_the_price_slowly, records)

    end = time.time()

    print(f"\nTotal time: {end-start:.2f}")
