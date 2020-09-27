import multiprocessing
import os
import shelve
import time


with shelve.open("record_shelf.shelf", "r") as shelf:
    records = shelf["records"]


def double_the_price_slowly(x):
    print(f"Process {os.getpid()}: Fetching and processing item ...")
    time.sleep(1)
    result = {"album": x["album"], "d_price": x["preis"] * 2}
    print(f"Process {os.getpid()}: Finished processing of album {x['album']}")
    return result


if __name__ == "__main__":
    multiprocessing.freeze_support()

    start = time.time()

    pool = multiprocessing.Pool(processes=len(records))
    _ = pool.map(double_the_price_slowly, records)

    end = time.time()

    print(f"\nTotal time: {end-start:.2f}")
