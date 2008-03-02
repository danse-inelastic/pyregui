#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Brandon Keith
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
from pyre.components.Component import Component

class MolDynamics(Component):
    '''This class serves as an API/interface for md engines.'''
    class Inventory(Component.Inventory):
        import pyre.inventory as inv  
        barostatParameter = inv.float('Barostat Parameter', default = 0.005)
        barostatParameter.meta['tip'] = '''barostat parameter to keep 
fluctuations relatively small'''
        coordinateFormat = inv.str('Coordinate Format', default = 'cartesian')
        coordinateFormat.meta['tip'] = 'what format the coordinates are in'
        coordinateFormat.validator = inv.choice(['cartesian','fractional'])
        constantPressureFit = inv.bool('Constant Pressure Fit', default = False)
        constantPressureFit.meta['tip'] = '''keep pressure constant during fitting (fit 
to irreducible cell coordinates and lattice lengths)'''
        constantPressureOptimize = inv.bool('Constant Pressure Optimize', default = False)
        constantPressureOptimize.meta['tip'] = '''keep pressure constant during optimization'''
        constantVolumeFit = inv.bool('Constant Volume Fit', default = False)
        constantVolumeFit.meta['tip'] = '''keep volume constant during fitting (fit 
to irreducible cell coordinates)'''
        constantVolumeOptimize = inv.bool('Constant Volume Optimize', default = False)
        constantVolumeOptimize.meta['tip'] = '''keep volume constant during optimization'''
        dispersionInRecipSpace = inv.bool('Calculate Dispersion in Reciprocal Space', default = False)
        dispersionInRecipSpace.meta['tip'] = '''whether to calculate dispersion forces 
partly in reciprocal space'''
        dumpFrequency = inv.float('Dump Frequency', default=1.0)
        dumpFrequency.meta['tip'] = '''frequency at which a restart file is written'''
        engineExecutablePath = inv.str('Engine Executable Path', default = 
                                '/home/brandon/gulp3.0/Src/gulp')
        engineExecutablePath.meta['tip'] = '''path to the engine\'s executable'''
        ensemble= inv.str('Thermodynamic Ensemble', default='nve', validator=inv.choice(["nve","nvt","npt"]))
        ensemble.meta['tip'] = 'thermodynamic ensemble (nve, nvt, npt, ...)'
        equilibrationTime = inv.float('Equilibration Time (ps)', default=0.1)
        equilibrationTime.meta['tip'] = 'equilibration time of the simulation (ps)'
        identifyMolecules = inv.bool('Indentify Molecules', default=False)
        identifyMolecules.meta['tip'] = '''identify molecules based on covalent radii 
and remove intramolecular coloumb interactions'''
        integrator = inv.str('Integrator', default='velocity-verlet')
        integrator.meta['tip'] = 'type of integrator'
        inputDeckName = inv.str('Input Filename', default = 'gulp.gin')
        inputDeckName.meta['tip'] = '''input file for executable'''
        logFilename = inv.str('Log Filename', default='molDynamics.log')
        logFilename.meta['tip'] = 'name of log file for md run'
        optimizeCell = inv.bool('Optimize Cell', default = False)
        optimizeCell.meta['tip'] = 'whether to optimize the unit cell'
        optimizeCoordinates = inv.bool('Optimize Coordinates', default = False)
        optimizeCoordinates.meta['tip'] = 'whether to optimize the coordinate positions'
        productionTime = inv.float('Production Time (ps)', default=5.0)
        productionTime.meta['tip'] = 'production time of the simulation'
        computeMaterialProperties = inv.bool('Compute Material Properties', default = False)
        computeMaterialProperties.meta['tip'] = 'whether to print material properties'
        restartFilename = inv.str('Restart Filename', default = 'molDynamics.res')
        restartFilename.meta['tip'] = '''restart file for md executable'''
        runType = inv.str('Run Type',default='md',\
                validator=inv.choice(['md', 'restart md', 'optimize', 'fit']))
        runType.meta['tip'] = 'type of run'
        sample = inv.facility('Sample', default=Component('sample', 'sample'))
        sample.meta['importance']=10
        sample.meta['tip'] = 'piece of material being measured/simulated'
        sampleFrequency = inv.float('Sample Properties Frequency', default=5.0)
        sampleFrequency.meta['tip'] = '''frequency at which sampled properties are 
written to trajectory and log file'''
        spaceGroup = inv.str('Space Group', default = None)
        spaceGroup.meta['tip'] = 'specify space group symmetry'
        thermostatParameter = inv.float('Thermostat Parameter', default = 0.005)
        thermostatParameter.meta['tip'] = '''thermostat parameter to keep 
fluctuations relatively small'''
        timeStep = inv.float('Time step (ps)', default=0.5)
        timeStep.meta['tip'] = 'integration time step (ps)'
        trajectoryFilename = inv.str('Trajectory Filename', default='molDynamics.xyz')
        trajectoryFilename.meta['tip'] = 'name of trajectory file'
        #trajectoryType = inv.facility('Trajectory Type', default = TrajectoryType())
        trajectoryType = inv.str('Trajectory Type', default = 'xyz (Gulp)')
        trajectoryType.meta['tip'] = '''type of trajectory file'''
        trajectoryType.validator = inv.choice(['xyz (Gulp)','netcdf (Mmtk)',
            'trajectory (Gulp)','history (Gulp)','phonon (Gulp)','arc (Gulp)'])
        workingDirectory = inv.str('Working Directory',default='$HOME')
        workingDirectory.meta['tip'] = '''working directory where computation will
take place and all files will be written'''
                        
    def __init__(self, name=None):
        if name is None:
            name = 'MolDynamics'
        Component.__init__(self, name, facility=None)
        self.i=self.inventory
    
#    def _configure(self):
#        Component._configure(self)
#        #self.sample = self.i.sample
    
# version
__id__ = "$Id$"

# Generated automatically by PythonMill on Mon Apr 16 12:44:30 2007

# End of file 
