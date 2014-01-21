import inspect

def is_subclass(self, cls, target_class_name="", level=0):
    """Check whether the cls is the same sort of class wiht 'target_class_name'
    """

    # TODO: inspect.getmro(cls)
    # = type(obj).mro()
    #
    queue = list(cls.__bases__)
    while len(queue)>0:
        c = queue.pop()
        if c.__name__ == "object":
            continue
        elif c.__module__ + "." + c.__name__ == target_class_name:
            return True
        [ queue.append(x) for x in c.__bases__ ]

    return False

def get_classes(self, path="", target_name="", gls=None):
    """Get classes of current loaded modules that are matched with 'target_name'
    """

    if gls is None:
        # Get caller's globals()
        gls = inspect.currentframe().f_back.f_globals
        # gls = sys._getframe(1).f_globals

    imported = gls.items()
    for d in imported:
        if inspect.ismodule(d[1]):
            try:
                d[1].__file__
            except:
                continue
            if d[1].__file__.startswith(path):
                print d[0], d[1]
                print "FOUND:", d[1].__file__
                for x in inspect.getmembers(d[1]):
                    if inspect.isclass(x[1]):
                        if is_subclass(x[1], target_class_name=target_name):
                            print "\t", x

    return None

# decorator for a tornado request class
def route_url(self, url):
    def _route_url(cls):
        orig_init = cls.__init__
        def __init__(self, *args, **kws):
            print "before", url
            self.xurl = url
            orig_init(self, *args, **kws)
            print "after", url
        cls.__init__ = __init__
        return cls

    return _route_url

# make a class on the fly
Panatomy = type("Panatomy", (object,), 
        {   "is_subclass":is_subclass, 
            "get_classes":get_classes, 
            "route_url":route_url })
