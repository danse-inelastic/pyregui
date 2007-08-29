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
PACKAGE = launchers

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
	Launcher.py \
	__init__.py \
	lsf_launcher.py \
	mpich_launcher.py \
	mpich2_launcher.py \
	serial_launcher.py \
	spawn.py \




export:: export-package-python-modules 



# version
# $Id: Make.mm,v 1.1 2006/08/03 23:42:43 linjiao Exp $

# End of file
