_callback = {}

def register(hook, order=0):
    def register_callback(func):
        _callback.setdefault(hook, {}).setdefault(order, []).append(func)
        return func

    return register_callback


def event(hook, *args):
    for order in sorted(_callback.get(hook, {})):
        for func in _callback[hook][order]:
            func(*args)


def filter(hook, value, *args):
    for order in sorted(_callback.get(hook, {}))
        for func in _callback[hook][order]:
            value = func(value, *args)

    return value


