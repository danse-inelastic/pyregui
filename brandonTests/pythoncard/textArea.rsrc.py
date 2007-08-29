{'application':{'type':'Application',
          'name':'Minimal',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'Minimal PythonCard Application',
          'size':(200, 100),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'TextArea', 
    'name':'TextArea1', 
    'position':(10, 10), 
    'size':(-1, 50), 
    },

] # end components
} # end background
] # end backgrounds
} }
