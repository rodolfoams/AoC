def read_int_arr():
    return map(int, raw_input().strip().split())

def process(arr):
    idx = arr.index(max(arr))
    ammount = arr[idx]
    arr[idx] = 0
    idx += 1
    for i in xrange(ammount):
        arr[idx%len(arr)] += 1
        idx += 1

def verify(tries, trie):
    curr = tries
    for v in trie:
        if v not in curr:
            return False
        curr = curr[v]
    return True

def save(tries, trie, n):
    curr = tries
    for v in trie:
        if v not in curr:
            curr[v] = dict()
        curr = curr[v]
    curr["begin"] = n

def get_cycle_begin(tries, trie):
    curr = tries
    for v in trie:
        curr = curr[v]
    return curr["begin"]

if __name__ == "__main__":
    sequences = list()
    tries = dict()
    steps = 0
    arr = read_int_arr()
    while not verify(tries, arr):
        steps += 1
        save(tries, arr, steps)
        process(arr)
    print steps - get_cycle_begin(tries, arr) + 1