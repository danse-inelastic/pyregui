#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from pyre.xml.Document import Document as DocumentNode


class Document(DocumentNode):


    tags = [
        "Gui", "MainApp", "MainFrame",
        'MenuBar', 'Menu', 'MenuItem',
        "Panel", "Splitter", "Notebook",
        "Sizer",
        "ListBox",
        'HistogramFigure', 'PyShell',
        "Section", "Note", "Paragraph", "Link",
        'Button', 'TextField', 
        "Table", "Row", "Cell",
        'Emphasis',
        "List", 'ListItem',
        'Code',
        'Figure',
        'Dialog',
        ]


    def onGui(self, gui):
        self.document = gui
        return


# version
__id__ = "$Id: Document.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
