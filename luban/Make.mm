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

PROJECT = luban
PACKAGE = luban

PROJ_TIDY += *.log *.pyc
PROJ_CLEAN =


BUILD_DIRS = \
	luban \


OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)


#--------------------------------------------------------------------------
#

all: export
	BLD_ACTION="all" $(MM) recurse

docs::
	BLD_ACTION="docs" $(MM) recurse

tidy:: 
	BLD_ACTION="tidy" $(MM) recurse

clean:: 
	BLD_ACTION="clean" $(MM) recurse


#--------------------------------------------------------------------------
#



export:: #export-binaries release-binaries export-python-modules 



# version
# $Id: Make.mm,v 1.5 2006/08/09 23:09:22 linjiao Exp $

# End of file
