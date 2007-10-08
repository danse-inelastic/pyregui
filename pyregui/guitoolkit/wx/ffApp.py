#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import ffFrame

modules ={u'addEditDialog': [0, '', u'addEditDialog.py'],
 u'ffFrame': [1, 'Main frame of Application', u'ffFrame.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = ffFrame.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
