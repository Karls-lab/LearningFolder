import subprocess
import time 
import multiprocessing
import fib

# Build the C extension if changed 
def build_fib():
    subprocess.run(["python3", "setup.py", "build_ext", "--inplace"])
build_fib()


def main(n):
    pool = multiprocessing.Pool()
    results = pool.map(fib.fib, range(n))

    #print(f"results: {results}")
    return results

print(f"\n\nStarting main.py\n")

start_time = time.perf_counter()
results = main(5000)
end_time = time.perf_counter()
print(f"Elapsed time: {end_time - start_time} seconds\n\n")

# num = 412986819712346493611195411383827409934884076105338432187865946722511205681167419748123598380002157658381536968436929608311101496272839009791376254928568258611725
# print(f"is the number in fib? {num in results}")

print(f"Last fib number: {results[-1]}")
