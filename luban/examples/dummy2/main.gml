<gui name="test">

<mainapp name="Dummy">

  <mainframe name="Dummy" label="mainframe" >

    <menubar>

      <menu text="&amp;File">
	<menuitem text="&amp;Open" tip="Open dummy file" click-callback="OnOpenFile"/>
	<menuitem text="&amp;Hello" tip="Say Hello" click-callback="OnHello"/>
	<menuitem text="&amp;Exit" tip="Exit Dummy" click-callback="OnExit"/>
      </menu>

      <menu text="&amp;Help">
	<menuitem text="&amp;About" tip="About Dummy" click-callback="OnAbout"/>
      </menu>
    </menubar>


    <splitter direction="horizontal" minimumPanelSize="100" sliderPosition="400">
      
      <splitter direction="vertical" minimumPanelSize="250">
	<panel label="listpanel" borderStyle="sunken">
	  <sizer ratios="[0,1]" border="5" direction="vertical">
 A list of sth:
	    <listbox style="single choice" label="list" selectionChange-callback="OnListSelectChanged" keydown-callback="OnKeyDownInListWindow">
	    </listbox>
	  </sizer>
	</panel>
	<panel label="graph" borderStyle="default">
	  <sizer ratios="[1]" border="5" direction="vertical">
	Hi, there!
          </sizer>
	</panel>
      </splitter>
      
      <panel label="lower" borderStyle="sunken">
	<sizer ratios="[1]" border="5">
	  <pyshell keydown-callback="+OnKeyDownInShellWindow" locals="pyshell_locals" label="pythonshell">
	  </pyshell>
	</sizer>
      </panel>
      
    </splitter>    

  </mainframe>
</mainapp>

</gui>
