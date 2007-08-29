#!/usr/bin/env python


# pyregui set up requires an "install_info.py" installed
# to  pyreg_gui python package directory.

def preparePackage( package, sourceRoot = "." ):
    package.changeRoot( sourceRoot )
    
    #--------------------------------------------------------
    # now add subdirs
    #
    #python modules
    package.addPurePython(
        sourceDir = 'pyregui',
        destModuleName = 'pyregui' )


    package.addScripts( sourceFiles = [
        "applications/text2pyreui.py",
        "applications/wxpyregui.py",
        "applications/pyreapphelp.py",
        ] )


    package.addEtc( "etc" )


    package.addData( 
        sourceDir = "resources",
        destDir = "pyregui/resources")

    
    return package



if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('nx5', '0.1.0a')

    preparePackage( package )

    package.setup()

