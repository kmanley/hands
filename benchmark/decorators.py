import time
import atexit

_timedfuncs = {} # func.__name__ -> (min, max, total, numcalls)

def dumpTimings(printfunc=None):
    funcs = _timedfuncs.keys()
    funcs.sort()
    for func in funcs:
        info = _timedfuncs[func]
        msg = ("%s: min=%3.5f msec, max=%3.5f msec, avg=%3.5f msec, numcalls=%d, calls/sec=%.5f" % (func, 
                                info[0], info[1], info[2]/float(info[3]), info[3], 1.0/(info[2]/float(info[3]))*1000.))
        if printfunc:
            printfunc(msg)
        else:
            print msg

atexit.register(dumpTimings)

def timed(func):
    def timed_wrapper(*args, **kw):
        start = time.clock()
        try:
            return func(*args, **kw)
        finally:
            elapsed = (time.clock() - start) * 1000.0
            info = _timedfuncs.setdefault(func.__name__, [999999, 0, 0, 0])
            if elapsed < info[0]:
                info[0] = elapsed
            if elapsed > info[1]:
                info[1] = elapsed
            info[2] = info[2] + elapsed
            info[3] = info[3] + 1
            _timedfuncs[func.__name__] = info
    try:
        timed_wrapper.__name__ = func.__name__
    except TypeError:
        pass # python 2.3 doesn't allow assigning to __name__
    return timed_wrapper

