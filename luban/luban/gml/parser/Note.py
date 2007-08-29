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


from AbstractNode import AbstractNode, debug


class Note(AbstractNode):


    tag = "note"

    from luban.gml.elements.Note import Note as ElementFactory 

    onTable = onParagraph = onLink = onFigure = AbstractNode.onElement

    pass # end of Note
    

# version
__id__ = "$Id: Note.py,v 1.1.1.1 2005/03/08 16:13:43 linjiao Exp $"

# End of file 
