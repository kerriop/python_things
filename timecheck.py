import time
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))

def checkio(data):
    x = []
    for i in data:
        if data.count(i) > 1:
            x.append(i)
    return x

print(list(checkio([1, 2, 3, 1, 3])))

with Profiler() as p:
    for x in range(10**4):
        list(checkio([1, 2, 3, 1, 3]))