

class Decorator:

    def __init__(self, tag, attributes={}):
        attrs_str = ' '.join( [ ("%s=%r" % (k,v)) for k,v in attributes.iteritems()] ) 
        self._start = "<%s " % tag + attrs_str + '>'
        self._end = "</%s>"  % tag
        return


    def start(self): return self._start

    def end(self): return self._end

    def decorations(self): return self._start, self._end

    def decorate(self, text): return self._start + text + self._end
