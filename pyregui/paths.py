import os

package = __import__( "pyregui" )
name = package.__name__


class Paths:
  scheme = {
    'bin': 'bin',
    'python': 'python',
    'lib': 'lib',
    'include': 'include',
    'data': 'share',
    }
  def __init__(
      self, root, bin = None, python = None, lib = None, 
      include = None, data = None):
    self.root = root
    scheme = self.scheme
    from os.path import join

    if bin is None:
      bin = join( root, scheme['bin'] )
    self.bin = bin

    if python is None:
      python = join( root, scheme['python'] )
    self.python = python

    if lib is None:
      lib = join( root, scheme['lib'] )
    self.lib = lib

    if include is None:
      include = join( root, scheme['include'] )
    self.include = include

    if data is None:
      data = join( root, scheme['data'] )
    self.data = data
    return



try: 
  import install_info as i
  paths = Paths( 
    None, bin = i.bin, python = i.python, lib = i.lib,
    include = i.include, data = i.share )
except ImportError:
  # assume that path_of_pyregui/../.. is the installation root
  root = os.path.abspath( os.path.join( package.__path__[0], '..', '..' ) )
  paths = Paths(root)
  pass


def find_resources():
    '''find the installation directory of 'resouces'
    
If the file 'alternateDirectory.txt' is found in the same directory
as paths.py, a different path for resources will be used.    
'''    
    try:
        f=file('alternateDirectory.txt','r')
        newpath=f.readline()
        f.close()
        return newpath
    except:
        return os.path.join( paths.data, name, "resources" )
#    home = os.path.expanduser( '~' )
#    return os.path.join(home, 'DANSE' , 'pyregui', 'resources' )

resources = find_resources()

