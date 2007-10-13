import wx.grid as gridlib

class TwoAtomPotentialTable(gridlib.PyGridTableBase):
    
    def __init__(self, parent):#, log, tableType):
        gridlib.PyGridTableBase.__init__(self)
        self.plotItems=parent.plotItems
        self.backend=parent.backend
        self.properties=None
        self.colLabels=['property','value']
#        self.dataTypes = [gridlib.GRID_VALUE_STRING]
        self.data = [[]]
        self.loadModel(PlotBrowser.currentItem)
        
    def loadModel(self,model):
        # first clear the gird
        self.Clear()
        # now load the new data
        if model.find('axes')!=-1:
            from graphics.MatplotlibPropertyModel import axesProps as properties
        elif model.find('line')!=-1:
            from graphics.MatplotlibPropertyModel import lineProps as properties
        elif model.find('plottables')!=-1:
            from graphics.MatplotlibPropertyModel import plottableProps as properties 
        elif model.find('figure')!=-1:
            from graphics.MatplotlibPropertyModel import figureProps as properties
        else:
            raise 'cannot find model properties'   

        self.properties = properties
        #process properties
        dataTypes=[None for p in self.properties]
        data=[None for p in self.properties]
        attributes=[None for p in self.properties]
        for i in range(len(self.properties)):
            val=self.getCurrentValue(i)
            data[i] = [self.properties[i][0], val]
            dataTypes[i] = self.properties[i][2]
            attributes[i] = self.properties[i][3]
        
        self.dataTypes = dataTypes
        self.data = data
        self.attributes = attributes
        
        # now insert the data--two columns for property value and
        # as many rows as it takes
        self.InsertCols(0,2)
        self.InsertRows(len(self.properties))
#        for i in range(len(properties)):
#            self.InsertRows()

    def getCurrentValue(self, row):
        objectReference = self.plotItems[PlotBrowser.currentItem]
        apiKeyword = self.properties[row][3]
        value=getp(objectReference, apiKeyword)
        #first take care of some special cases for formatting purposes:
        sequence2String=['xlim','ylim']
        array2String=['xticks','yticks','xdata','ydata']
        textBox2String=['xticklabels','yticklabels']
        if type(apiKeyword)==type(1.0) or type(apiKeyword)==type(1):
            value=self.roundNChopNString(value)
        elif apiKeyword in sequence2String:
            value=self.roundNChopNString(value)
        elif apiKeyword in array2String:
            value=value.tolist()
            value=self.roundNChopNString(value)
        elif apiKeyword in textBox2String:
            #from wx.text import Text
            strings=[]
            for textInstance in value:
                strings.append(textInstance.get_text())
            value=strings
        return value

    def roundNChopNString(self,num):
        '''This rounds everything to three decimal places and eventually chops off trailing stuff'''
        if type(num)==type(1.0):# or type(num)==type(1):
            return round(num,3)
        elif type(num)==type([1.0]):
            newNum=[]
            for i in range(len(num)):
                newNum.append(round(num[i],3))
            return num
        elif type(num)==type((1.0,)):
            newNum=[]
            for i in range(len(num)):
                newNum.append(round(num[i],3))
            return tuple(num)
                
        
        
    # required methods for the wxPyGridTableBase interface

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.data[0])

    def IsEmptyCell(self, row, col):
        try:
            return not self.data[row][col]
        except IndexError:
            return True

    # Get/Set values in the table.  The Python version of these
    # methods can handle any data-type, (as long as the Editor and
    # Renderer understands the type too,) not just strings as in the
    # C++ version.
    def GetValue(self, row, col):
        try:
            return self.data[row][col]
        except IndexError:
            return ''

    def SetValue(self, row, col, value):
        
        try:
            self.data[row][col] = value
        except IndexError:
            # add a new row
            self.data.append([''] * self.GetNumberCols())
            self.SetValue(row, col, value)

            # tell the grid we've added a row
            msg = gridlib.GridTableMessage(self,            # The table
                    gridlib.GRIDTABLE_NOTIFY_ROWS_APPENDED, # what we did to it
                    1                                       # how many
                    )

            self.GetView().ProcessTableMessage(msg)

    #--------------------------------------------------
    # Some optional methods

    # Called when the grid needs to display labels
    def GetColLabelValue(self, col):
        return self.colLabels[col]

    # Called to determine the kind of editor/renderer to use by
    # default, doesn't necessarily have to be the same type used
    # natively by the editor/renderer if they know how to convert.
    def GetTypeName(self, row, col):
        if col==0:
            return gridlib.GRID_VALUE_STRING
        else:
            return self.dataTypes[row]

    # Called to determine how the data can be fetched and stored by the
    # editor and renderer.  This allows you to enforce some type-safety
    # in the grid.
    def CanGetValueAs(self, row, col, typeName):
        #can't change the first column
        if col==0:
            return False
        # everything in second column depends on the row
        entryType = self.dataTypes[row].split(':')[0]
        if typeName == entryType:
            return True
        else:
            return False

    def CanSetValueAs(self, row, col, typeName):
        return self.CanGetValueAs(row, col, typeName)
    
#    def GetAttr(self,row,col):
#        if col
    
