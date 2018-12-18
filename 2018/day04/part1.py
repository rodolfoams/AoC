import argparse

def main(args):
    logs = list()
    with open(args.infile,'r') as file:
        line = file.readline().strip()
        while len(line) > 0:
            logs.append(line)
            line = file.readline().strip()
    guard_id = 0
    sleep_begin = 0
    sleep_end = 0
    sleep_logs = {}
    for line in logs:
        if "guard" in line.lower():
            guard_id = int(line.split("#")[1].split(" ")[0].strip())
            if guard_id not in sleep_logs:
                sleep_logs[guard_id] = [0] * 60
        elif "asleep" in line:
            sleep_begin = int(line.split("]")[0].split(":")[1])
        elif "wakes" in line:
            sleep_end = int(line.split("]")[0].split(":")[1])
            for i in range(sleep_begin, sleep_end):
                sleep_logs[guard_id][i] += 1
    max_sleep = 0
    chosen_guard = 0
    minute = 0
    for guard_id, logs in sleep_logs.items():
        time_slept = sum(logs)
        if time_slept > max_sleep:
            chosen_guard = guard_id
            max_sleep = time_slept
            minute = logs.index(max(logs))
    print(chosen_guard * minute)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--infile', type=str, default='day4.in', help='Input file.')
    parser.add_argument('--outfile', type=str, default='day4.in', help='Output file.')
    main(parser.parse_args())