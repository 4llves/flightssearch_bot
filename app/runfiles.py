import multiprocessing
import subprocess

def run_script(script):
    subprocess.call(["python", script])

if __name__ == "__main__":
    scripts = ["./app/flightssearch_bot.py", "./app/server.py"]
    processes = []

    for script in scripts:
        process = multiprocessing.Process(target=run_script, args=(script,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()