
import  wx
from pyre.components.Component import Component

class AtomLoader(wx.Dialog):#, Component):
    '''load atoms for various molecular modeling engines'''

    def __init__(self, parent = None,
                 size = (600,400), # wx.DefaultSize,
                 pos = wx.DefaultPosition,
                 style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
                 pyre_component = None, pyre_inventory = None,
                 verbosity = 1, toolkit = None
                 ):

        self.parent = parent

        self.toolkit = toolkit

        #self._registry = GuiElementRegistry()
        
        #self.inventory = InventoryProxy(pyre_inventory)
        self.pyre_component = pyre_component
        self.verbosity = verbosity

        #apptitle = "Component: %s" % pyre_component.name
        apptitle = "Settings of Loader"    
        
        wx.Dialog.__init__(self,parent = None)
        
        # Instead of calling wx.Dialog.__init__ we precreate the dialog
        # so we can set an extra style that must be set before
        # creation, and then we create the GUI object using the Create
        # method.
        
#        pre = wx.PreDialog()
#        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
#        pre.Create(parent, -1, apptitle, pos, size, style)
#        
#        # This next step is the most important, it turns this Python
#        # object into the real wrapper of the dialog (instead of pre)
#        # as far as the wxPython extension is concerned.
#        
#        self.PostCreate(pre)
        
        configure_panel, cpsize = self.get_action_window()

        # add ok and cancel buttons to sizer
        ok = wx.Button(self, wx.ID_OK, "OK")
        cancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        helpbutton = wx.Button(self, -1, "Help")

        if pyre_component.__class__.__doc__ is not None:
            docstr = pyre_component.__class__.__doc__
        else:
            docstr = "Please consider writing a docstring for %s" % pyre_component.__class__
        self.Bind(wx.EVT_BUTTON, self.OnHelpButton(docstr), helpbutton)


        okcancelSizer = wx.BoxSizer(wx.HORIZONTAL)
        okcancelSizer.Add(ok)
        okcancelSizer.AddSpacer( (7,7) )
        okcancelSizer.Add(cancel)

        topSizer = wx.BoxSizer( wx.HORIZONTAL )
        topSizer.Add( okcancelSizer )
        topSizer.AddSpacer( (50,40) )
        topSizer.Add( helpbutton )


        
        self.largeText = wx.TextCtrl(self, -1,
                        "Atom   x    y    z\n",
                       size=(200, 100), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        middleSizer = wx.BoxSizer(wx.VERTICAL)
        middleSizer.Add(self.largeText, 0, wx.ALL, 25)

        sizer = wx.BoxSizer( wx.VERTICAL )
        sizer.Add( topSizer )
        sizer.Add( configure_panel, 1, wx.GROW|wx.ALL, 5)#, 0, wx.FIXED_MINSIZE )
        sizer.Add(middleSizer)

        # now paint the screen
        border = wx.BoxSizer()
        border.Add(sizer, 1, wx.GROW|wx.ALL, 25)
        border.Fit(self)
        self.SetSizer(border)
        w, h = cpsize
        w+=150
        h+=200
        w = min(w, 800)
        h = min(h, 600)
        w = max(w, 300)
        h = max(h, 200)
        self.SetSize( (w,h) )
        self.SetAutoLayout( 1 )
        #self.Layout()
        
    def atoms(self):
        return self.largeText.GetValue()
    
    
if __name__ == "__main__":
#    demo_plotter(sample_graph())
    
    # Make a frame to show it
    app = wx.PySimpleApp()
    frame = AtomLoader()
    #frame = wx.Frame(None,-1,'Plottables')
    #plotter = Plotter(frame)
    frame.Show()
    app.MainLoop()
