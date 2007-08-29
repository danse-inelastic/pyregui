
context = {}
cache = []

def write( t ):
    cache.append( t )
    return

def exec_( lines, d ):
    global cache, write, context
    d['write'] = write
    d['cache'] = cache
    d.update( context )
    context = {}
    newlines = []
    codes = []
    iscode = False
    for line in lines:
        if line.startswith( '% ' ):
            codes.append( line[2:] )
            if not iscode: iscode = True
            pass
        else:
            if iscode:
                exec '\n'.join(codes) in d
                newlines += cache
                cache = []
                pass
            newlines.append( line )
            iscode = False
            pass
        continue
    return newlines


def parse( instream, d={} ):
    lines = instream.read().splitlines()
    import tempfile
    h, path = tempfile.mkstemp( )
    stream = open(path, 'w')
    print >>stream, '\n'.join(exec_(lines, d ))
    stream.close()
    newstream = open(path, 'r')
    import os
    os.remove( path )
    return newstream


def test():
    t  = """
line1
line2
template begin
% write( "hello" )
template end
"""
    print exec_( t.splitlines(), {} )

    import tempfile
    h, path = tempfile.mkstemp()
    stream = open( path, 'w' )
    print >>stream, t
    stream.close()
    
    print parse( open(path), {} ).read()

    import os
    os.remove( path )
    return


if __name__ == "__main__" : test()
