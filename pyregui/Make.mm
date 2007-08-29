# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005 All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = pyregui
PACKAGE = pyregui

PROJ_TIDY += *.log *.pyc
PROJ_CLEAN =


BUILD_DIRS = \
	guitoolkit \
	inventory \
	launchers \


OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

#--------------------------------------------------------------------------
#

EXPORT_PYTHON_MODULES = \
	LauncherApp.py \
	WindowAppFactory.py \
	pyreapp_ext.py \
	pyreui.py \
	paths.py \
	utils.py \
	__init__.py \



EXPORT_BINS = \
	wxpyregui.py \
	textpyreui.py \
	text2pyreui.py \
	LauncherApp.py \


export:: export-binaries release-binaries export-python-modules 



# version
# $Id: Make.mm,v 1.5 2006/08/09 23:09:22 linjiao Exp $

# End of file
