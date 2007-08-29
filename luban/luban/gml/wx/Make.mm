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
PACKAGE = gml/wx

# directory structure

BUILD_DIRS = \
    wxmpl \

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse


#--------------------------------------------------------------------------
#
# export

EXPORT_PYTHON_MODULES = \
	Button.py \
	Dialog.py \
	HistogramPlotPanel.py \
	ListBox.py \
	MainFrame.py \
	MainView.py \
	MainWinApp.py \
	Menu.py \
	MenuBar.py \
	MenuItem.py \
	Notebook.py \
	Panel.py \
	PyShell.py \
	RadioBox.py \
	Sizer.py \
	Splitter.py \
	TextField.py \
	__init__.py \
	ext.py \
	globalID.py \



include doxygen/default.def

export:: export-package-python-modules 

# version
# $Id: Make.mm 1205 2006-11-15 16:23:10Z linjiao $

# End of file
