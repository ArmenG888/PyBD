# The language 
<ul>
<li><h3>Keyboard</h3>
  <h4>You can click or type things on victims computer</h4>
Will type hello and bye on the victims computer
<pre>keyboard:"
Hello
bye
";</pre>
  <h4>Pressing buttons or hotkeys, need to be placed inside `button_name`</h4>
<pre>
keyboard:"
`ctrl + n`
`enter`
`alt + f4`
";
</li>
  
<li><h3>Read</h3>
<h4>Read files and takes infinite amount of arguments separted by a commma</h4>
<pre>read("test.txt")</pre>
<h4>Read multiple files (infinite amount)</h4>
<pre>read("file_name", "filename_2")</pre>
</li>
  
<li><h3>Delay</h3>
<h4>Takes on argument in seconds</h4>
<h4>This example will delay for one second</h4>
<pre>delay(1)</pre>
</li>
  
<li><h3>Python</h3>
<h4>Running python scripts</h4>
<pre>python: "
print("hello world")
";
</pre>
</li>
  
<li><h3>CMD</h3>
<h4>Anything other will be interpurted as a cmd command</h4>
<pre>
cd ..
dir
</pre>
</li>
</ul>

