#!/usr/bin/env python


def findExecutable_unix( executable ):
    import popen2, os
    if os.path.exists( executable ): 
        return executable
    else:
        try:
            ret = popen2.popen4("which %s" % executable)[0].readlines()[0].strip()
            # crappy implementation
            if len(ret.split())>1 and ret.startswith( 'no' ):
                raise "not found"
            return ret
            pass
        except:
            raise RuntimeError , "Cannot find executable %s" % executable
    


def findExecutable_windows( exe ):
    import os
    path_env = os.environ["PATH"]
    paths = path_env.split(';')
    for path in paths: 
        try: items = os.listdir(path)
        except: continue
        if exe in items: return os.path.join( path, exe )
    raise RuntimeEeeror, "Cannot find %s" % exe


import os
if os.name == "nt":  nt = 1
else: nt = 0


def findExecutable( exe ):
    if nt: return findExecutable_windows( exe )
    return findExecutable_unix( exe )

