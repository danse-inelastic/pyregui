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
PACKAGE = guitoolkit/text

PROJ_TIDY += *.log
PROJ_CLEAN =


BUILD_DIRS = \


OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

#--------------------------------------------------------------------------
#

EXPORT_PYTHON_MODULES = \
	InputBoxFactory.py \
	InventoryDialog.py \
	MainFrame.py \
	SetButtonFactory.py \
	TraitLabelFactory.py \
	__init__.py \


export:: export-package-python-modules 



# version
# $Id: Make.mm,v 1.1 2006/08/09 23:09:22 linjiao Exp $

# End of file
