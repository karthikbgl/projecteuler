from datetime import datetime                                                

def timeit(func):
    def inner_wrap(*args, **kw):
        t_start = datetime.now()
        result = func(*args, **kw)
        t_end = datetime.now()

        print '%r (%r, %r) %2.2f sec' % \
              (func.__name__, args, kw,
                  (t_end-t_start).total_seconds())
        return result

    return inner_wrap
