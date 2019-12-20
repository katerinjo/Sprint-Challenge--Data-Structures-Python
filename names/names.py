import time

class Fork:
    def __init__(self, val, smaller=None, bigger=None):
        self.val = val
        self.smaller = smaller
        self.bigger = bigger

class BinarySet:
    def __init__(self):
        self.store = None

    def has_seen(self, name):
        if self.store == None:
            self.store = Fork(name, None, None)
            return False
        runner = self.store
        while runner is not None:
            if name == runner.val:
                return True
            if name < runner.val:
                if runner.smaller is None:
                    runner.smaller = Fork(name)
                    return False
                else:
                    runner = runner.smaller
            else:
                if runner.bigger is None:
                    runner.bigger = Fork(name)
                    return False
                else:
                    runner = runner.bigger

start_time = time.time()

bin_set = BinarySet()
duplicates = []
f = open('names_1.txt', 'r')
for name in (name.strip() for name in f):
    if bin_set.has_seen(name):
        duplicates.append(name)
f.close()

f = open('names_2.txt', 'r')
for name in (name.strip() for name in f):
    if bin_set.has_seen(name):
        duplicates.append(name)
f.close()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
