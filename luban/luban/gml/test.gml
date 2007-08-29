<gui name="test">

<mainapp name="hello">
  <mainframe name="hello">
    <menubar>
      <menu text="&amp;File">
	<menuitem text="&amp;Open histogram" tip="Open saved histogram data file" callback="OnOpenHistogramFile">
	</menuitem>
      </menu>
    </menubar>
    <splitter direction="horizontal" minimumPanelSize="100" sliderPosition="400">
      
      <splitter direction="vertical" minimumPanelSize="250">
	<panel label="listpanel" borderStyle="sunken">
	  <sizer ratios="[1]" border="5">
	    <listbox style="single choice" label="histogramList">
	    </listbox>
	  </sizer>
	</panel>
	<panel label="graph" borderStyle="sunken">
	  <sizer ratios="[1]" border="5">
	    <histogramfigure size="(4,3)" dpi="75" label="histogramfigure">
	    </histogramfigure>
	  </sizer>
	</panel>
      </splitter>
      
      <panel label="lower" borderStyle="sunken">
      </panel>
      
    </splitter>    
  </mainframe>
</mainapp>

</gui>
