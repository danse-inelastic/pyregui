#!/usr/bin/env python

def preparePackage( package, sourceRoot = "." ):
    package.changeRoot( sourceRoot )
    
    #--------------------------------------------------------
    # now add python package luban
    #
    #journal
    package.addPurePython(
        sourceDir = 'luban',
        destModuleName = 'luban' )

    return package


if __name__ == "__main__":
    #------------------------------------------------------------
    #init the package
    from distutils_adpt.Package import Package
    package = Package('luban', '0.001')

    preparePackage( package )

    package.setup()

