# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = luban
PACKAGE = gml/elements

#--------------------------------------------------------------------------
#

all: export


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	AbstractAttributeContainer.py \
	AttributeDictionary.py \
	AttributeInventory.py \
	Button.py \
	Cell.py \
	Code.py \
	Dialog.py \
	Element.py \
	Emphasis.py \
	Figure.py \
	Gui.py \
	HistogramFigure.py \
	Link.py \
	List.py \
	ListBox.py \
	ListItem.py \
	MainApp.py \
	MainFrame.py \
	Menu.py \
	MenuBar.py \
	MenuItem.py \
	Note.py \
	Notebook.py \
	Panel.py \
	Paragraph.py \
	PyShell.py \
	RadioBox.py \
	Row.py \
	Section.py \
	Sizer.py \
	Splitter.py \
	Table.py \
	TextField.py \
	__init__.py \
	traits.py \



include doxygen/default.def

export:: export-package-python-modules 

# version
# $Id: Make.mm 1205 2006-11-15 16:23:10Z linjiao $

# End of file
