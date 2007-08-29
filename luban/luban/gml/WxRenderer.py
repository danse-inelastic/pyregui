#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin
#                      California Institute of Technology
#                         (C) 2007  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import journal
jname = "gml-wx-renderer"
debug = journal.debug( jname )
warning = journal.warning( jname )
info = journal.info( jname )


from luban.controller import eval_


import wx


class Renderer:

    def render(self, gui, controller):
        """
        gui: gui xml tree
        controller: controller of the model-contoller-view paradigm
        """
        info.log( "start rendering" )
        self.controller = controller
        self.view = controller.view
        self._cur_sec_level = 0
        self._current_widget = None
        document = gui.identify(self)
        info.log( "rendering done." )
        return document


    # handlers

    def onGui(self, gui):
        self.expand( gui )
        return self.view


    def onMainApp(self, mainApp):

        name = mainApp.attributes.get('name')
        
        self._current_widget = app = wx.app( name )

        self.view.app = app # so that main wx view can initialize

        self.expand( mainApp )
        return


    def onMainFrame(self, mainFrame):
        name = mainFrame.attributes.get('name')
        label = mainFrame.attributes.get('label')
        app = self._current_widget 
        frame = wx.mainFrame( name )
        self.view.setSubview( label, frame )
        self.mainframe = frame # remember this so that menu can refer to it as parent
        self._current_widget = app.frame = frame
        self.expand( mainFrame )
        self._current_widget = app
        return


    def onPanel(self, panel):
        parent = self._current_widget
        
        attrs = panel.attributes
        
        wxpanel = wx.panel( parent, borderStyle=attrs.get("borderStyle") )
        
        label = attrs.get('label')
        if label: self.view.setSubview( label, wxpanel )
        
        self._current_widget = wxpanel
        self.expand( panel )
        self._current_widget = parent
        return wxpanel


    def onSplitter(self, splitter):
        parent = self._current_widget
        children = splitter.children
        if len(children) != 2: raise RuntimeError, "splitter needs two children"

        attrs = splitter.attributes

        direction = attrs.get("direction")
        sliderPosition = attrs.get("sliderPosition")

        wxsplitter = wx.splitter( parent , minimumPanelSize = attrs.get('minimumPanelSize') )

        self._current_widget = wxsplitter
        window0 = children[0].identify(self)
        window1 = children[1].identify(self)
        self._current_widget = parent
        wxsplitter.add(window0, window1, direction, sliderPosition)
        return wxsplitter


    def onNotebook(self, notebook):
        parent = self._current_widget
        children = notebook.children

        attrs = notebook.attributes

        borderStyle = attrs.get("borderStyle")
        titles = attrs.get('titles')

        wxnotebook = wx.notebook( parent, borderStyle = borderStyle )

        self._current_widget = wxnotebook
        
        for title, child in zip(titles, children):
            page = child.identify(self)
            wxnotebook.add( title, page )
            continue
        
        self._current_widget = parent
        return wxnotebook


    def onSizer(self, sizer):
        
        import wx
        parent = self._current_widget
        
        children = sizer.children
        ratios = sizer.attributes.get("ratios")
        if len(ratios) != len(children):
            msg = "Number of elements and number of ratios do not match: %s != %s" %(
                len(ratios), len(children) )
            raise ValueError, msg
        direction = sizer.attributes.get('direction')
        wxsizer = wx.sizer( direction = direction )
        border = sizer.attributes.get("border")

        for ratio, child in zip(ratios, children):
            debug.log( "prepare to descend to %s" % child )
            if isElement(child): 
                child.parentIsSizer = 1
                wxelement = child.identify(self)
                wxsizer.add( wxelement, float(ratio), border )
            elif isStr(child):
                text = self._write( child )
                wxsizer.add( text, float(ratio), border )
                wxelement = text
            else: raise ValueError
            
            continue

        #we need to remember how deep we are in the sizer hierarchy
        #if we don't remember, all sizers will try to fit
        #to the parent window. In wx, sizer is not a window,
        #it is not a widget. 

        if not sizer.__dict__.get( 'parentIsSizer' ) :
            parent.SetSizer(wxsizer)
            parent.SetAutoLayout(1)
            wxsizer.Fit(parent)
            pass
        
        return wxsizer


    def onListBox(self, listbox):
        attrs = listbox.attributes
        
        style = attrs.get('style')
        callbacks = self._eval_callbacks( _get_callbacks(attrs), locals() )
        parent = self._current_widget
        wxlistbox = wx.listbox( parent, style=style, callbacks=callbacks )
        
        label = attrs.get('label')
        if label: self.view.setSubview( label, wxlistbox )

        return wxlistbox


    def onButton(self, button):
        attrs = button.attributes
        
        callbacks = self._eval_callbacks( _get_callbacks(attrs), locals() )
        kwds = attrs.asDict()
        debug.log( "attributes = %s" % kwds )
        _remove_callbacks( kwds )
        
        parent = self._current_widget
        wxbutton = wx.button( parent, callbacks=callbacks, **kwds )
        
        label = attrs.get('label')
        if label: self.view.setSubview( label, wxbutton )

        return wxbutton


    def onTextField(self, textField):
        attrs = textField.attributes
        kwds = attrs.asDict()
        label = kwds.get('label')
        del kwds['label']
        
        parent = self._current_widget
        wxtextField = wx.textfield( parent, **kwds )
        
        if label: self.view.setSubview( label, wxtextField )

        return wxtextField


    def onMenuBar(self, menubar):
        parent = self._current_widget
        wxmenubar = wx.menubar()
        for child in menubar.children:
            wxmenu = child.identify(self)
            wxmenubar.append( wxmenu )
            continue
        parent.SetMenuBar( wxmenubar )
        return wxmenubar


    def onMenu(self, menu):
        attrs = menu.attributes
        text = attrs.get('text')
        label = attrs.get('label')
        mainframe = self.mainframe
        wxmenu = wx.menu( mainframe, text )
        for child in menu.children:
            wxmenuitem = child.identify(self)
            wxmenu.append( wxmenuitem )
            continue
        if label: self.view.setSubview( label, wxmenu )
        return wxmenu


    def onMenuItem(self, menuitem):
        attrs = menuitem.attributes
        #frame = self._current_widget
        text = attrs.get( 'text' )
        tip = attrs.get( 'tip' )
        callbacks = self._eval_callbacks( _get_callbacks(attrs), locals() )
        #wxmenuitem = wx.menuitem( frame, text, tip = tip, callbacks = callbacks)
        wxmenuitem = wx.menuitem( text, tip = tip, callbacks = callbacks)
        return wxmenuitem


    def onHistogramFigure(self, histogramFigure):
        attrs = histogramFigure.attributes
        parent = self._current_widget
        size = attrs.get( 'size' )
        dpi = attrs.get( 'dpi' )
        wxHistogramFigure = wx.histogramFigure( parent, size = size, dpi = dpi )

        label = attrs.get('label')
        if label: self.view.setSubview( label, wxHistogramFigure )
        
        return wxHistogramFigure


    def onPyShell(self, pyshell):
        attrs = pyshell.attributes
        parent = self._current_widget

        envs = eval_( attrs.get('locals'), locals() )
        callbacks = self._eval_callbacks( _get_callbacks(attrs), locals() )
        wxpyshell = wx.pyshell( parent, callbacks=callbacks, locals = envs )
        
        label = attrs.get('label')
        if label: self.view.setSubview( label, wxpyshell )

        return wxpyshell


    def onDialog(self, dialog):
        attrs = dialog.attributes
        parent = self._current_widget

        kwds = attrs.asDict()
        if kwds.has_key( 'label' ): del kwds['label']
        wxdialog = wx.dialog( parent, **kwds )

        label = attrs.get('label')
        if label: self.view.setSubview( label, wxdialog )

        self._current_widget = wxdialog
        self.expand( dialog )
        self._current_widget = parent

        return wxdialog
        

    def expand(self, element):
        debug.log( "expand element %s" % element )
        for child in element.children:
            debug.log( "descend to %s" % child )
            if isElement(child): child.identify(self)
            elif isStr(child):
                self._write( child )
            else: raise ValueError
            continue
        return


    def _write(self, txt):
        return wx.text( self._current_widget, txt )


    def _eval_callbacks(self, callbacks, locals):
        """helper function to evaluate pointer to callback functions
        """
        rt = {}
        for name, value in callbacks.iteritems():
            if value.endswith('+') :
                name = '+' + name
                value = value[:-1]
            elif value.startswith('+'):
                name = name + '+'
                value = value[1:]
                pass
            rt[name] = eval_( value, locals )
            continue
        return rt


    pass # end of Renderer




signature = "-callback"
def _get_callbacks( attrs):
    '''helper function to extract callback-specifications

    attrs is a dictionary like object that holds attributes of a
    xml tag. loop through this dictionary and find out all callbacks.
    '''
    rt = {}
    for attrName in attrs:
        if attrName.endswith( signature ):
            rt[ attrName[:-len(signature)] ] = attrs.get( attrName )
            pass
        continue
    return rt
def _remove_callbacks( attrdict ):
    for attrName in attrdict:
        if attrName.endswith( signature ):
            del attrdict[ attrName ]
            pass
        continue
    return


from elements.Element import isStr, isElement


# version
__id__ = "$Id$"

# End of file 

