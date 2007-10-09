import wx


class LargeTextLoader(wx.Dialog):
    '''loads a large amount of text'''

    def registerInputBox( self, trait, box ):
        self._registry.register( "inputBox", trait, box )
        return

    def getUserInput( self, trait ):
        inputBox = self._registry.get( "inputBox", trait )
        return inputBox.GetValue().strip()

    def setUserInput( self, trait, value):
        inputBox = self._registry.get( "inputBox", trait )
        inputBox.SetValue( value )
        return

    def getGuiElement( self, category, trait):
        return self._registry.get(category, trait )


    def registerGuiElement(self, category, trait, element):
        self._registry.register( category, trait, element)
        return


    def __init__(self, parent = None,
                 size = (600,400), # wx.DefaultSize,
                 pos = wx.DefaultPosition,
                 style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER,
                 pyre_component = None, pyre_inventory = None,
                 verbosity = 1, toolkit = None
                 ):

        self.parent = parent

        self.toolkit = toolkit

#        self._registry = GuiElementRegistry()
        
#        self.inventory = InventoryProxy(pyre_inventory)
        self.pyre_component = pyre_component
        self.verbosity = verbosity

        #apptitle = "Component: %s" % pyre_component.name
        apptitle = "Settings"

        pre = wx.PreDialog()
        pre.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        pre.Create(parent, -1, apptitle, pos, size, style)
        self.PostCreate(pre)

        # dialog created. get the main view 
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

        sizer = wx.BoxSizer( wx.VERTICAL )
        sizer.Add( topSizer )
        sizer.Add( configure_panel, 1, wx.GROW|wx.ALL, 5)#, 0, wx.FIXED_MINSIZE )

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

        #print "%s.__init__ done" % self.__class__.__name__
        return
    
    def getText(self):
        return self.largeText.GetValue()


    def get_action_window(self):

        #traits = self.inventory.traits( verbosity = self.verbosity )

        #import wx.lib.scrolledpanel as scrolled

        width = 600
        height = 400 
        
        
        self.largeText = wx.TextCtrl(self, -1,
                        "Atom   x    y    z\n",
                       size=(600, 400), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER)
        
        return self.largeText, (width,height)

#        dialog = self
#        
#        class Panel( scrolled.ScrolledPanel ):
#
#            def __getattribute__(self, name):
#                try: return object.__getattribute__(self, name)
#                except:
#                    return getattr( dialog, name )
#                
#        panel = Panel(
#            self, -1, #size=(width,height ),
#            style = wx.TAB_TRAVERSAL, #|wx.SUNKEN_BORDER,
#            name = "configuration" )
#
###         panel.registerInputBox = self.registerInputBox
###         panel.registerGuiElement = self.registerGuiElement
###         panel.getUserInput = self.getUserInput
###         panel.getGuiElement = self.getGuiElement
###         panel.setUserInput = self.setUserInput
###         panel.inventory = self.inventory
#
#        inputBoxFactory = self.toolkit.InputBoxFactory(panel)
#        setButtonFactory = self.toolkit.SetButtonFactory(panel)
#        labelFactory = self.toolkit.TraitLabelFactory(panel)
#
#        sizer = wx.GridBagSizer(vgap = 10, hgap = 5)
#
#        row = 0
#        for trait in traits:
#            l = labelFactory( trait ); sizer.Add( l, pos=(row,0), flag = wx.ALIGN_RIGHT|wx.GROW|wx.ALL)
#            t = inputBoxFactory( trait ); sizer.Add( t, pos=(row, 1), flag = wx.GROW)
#            b = setButtonFactory( trait )
#            if b: sizer.Add( b ,  pos = (row, 2), flag = wx.GROW|wx.ALL)
#            row = row+1
#            continue
#
#        boxSizer = wx.BoxSizer( wx.VERTICAL )
#        boxSizer.Add( sizer, 1, wx.GROW|wx.ALL, 5 )
#        panel.SetSizer( boxSizer )
#        w, h = panel.GetBestVirtualSize()
#        #boxSizer.SetSizeHints( panel.GetParent() )
#        panel.SetAutoLayout(1)
#        panel.SetupScrolling()
#
#        return panel, (w,h)


    def OnHelpButton(self, docstr, title="Pyre Docstring"):
        def _(event): 
            dlg = wx.lib.dialogs.ScrolledMessageDialog(self, docstr, title)
            dlg.ShowModal()
        return _
    
if __name__ == "__main__":
#    demo_plotter(sample_graph())
    
    # Make a frame to show it
    app = wx.PySimpleApp()
    dlg = LargeTextLoader()
    #frame = wx.Frame(None,-1,'Plottables')
    #plotter = Plotter(frame)
    dlg.Show()
    app.MainLoop()