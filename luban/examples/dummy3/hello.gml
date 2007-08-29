<gui name="test">

<dialog title="hello" label='hellodialog'>

  <sizer ratios="[2,1]" border="5" direction="vertical">

    <panel label="form">
      <sizer ratios="[1,1]" border="2" direction="vertical">
	<sizer ratios="[1,2]" border="2" direction="horizontal">
	  name <textfield label="namefield" value="luban"/>
	</sizer>
	<sizer ratios="[1,2]" border="2" direction="horizontal">
	  greetings <textfield label="greetingsfield" value="hello"/>
	</sizer>
      </sizer>
    </panel>

    <panel label='buttons'>
      <sizer ratios="[1,1]" border="5" direction="horizontal">
	<button label='OK'/>
	<button label='Cancel'/>
      </sizer>
    </panel>

  </sizer>

</dialog>

</gui>
