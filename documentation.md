# The language 
<ul>
<li><h3>Keyboard</h3>
  <h4>You can click or type things on victims computer</h4>
Will type hello and bye on the victims computer
<pre>
1. keyboard:"
2. Hello
3. bye
4. ";
</pre>
<h4>Pressing buttons or hotkeys, need to be placed inside `button_name`</h4>
<pre>
1. keyboard:"
2. `ctrl + n`
3. `enter`
4. `alt + f4`
5. ";
</li>
  
<li><h3>Read</h3>
<h4>Read files and takes infinite amount of arguments separted by a commma</h4>
<pre>
1. read("test.txt")
[Output]:
test.txt content
</pre>
<h4>Read multiple files (infinite amount)</h4>
<pre>
1. read("file_name", "filename_2")
[Output]:
:file_name:
file content
:filename_2:
file 2 content
</pre>
</li>
  
<li><h3>Delay</h3>
<h4>Takes on argument in seconds</h4>
<h4>This example will delay for one second</h4>
<pre>1. delay(1)</pre>
</li>

<li><h3>CD</h3>
<h4>Changes directory optional one argument which is directory name .. is going back</h4>
  <h4>If not arguments argument will be the current directory</h4>
<pre>
1. cd documents
[Output]:
C:/users/User/documents/
2. cd ..
[Output]:
C:/users/User/
3. cd 
[Output]:
C:/users/User/
</li>  
  
<li><h3>Power</h3>
<h4>Controling the computers power, restarting, shutting down, and logging out the user (sleep)</h4>
<pre>
1. power("shutdown")
[Output]:
Shutting down the pc
2. power("sleep")
[Output]:
Computer is going on sleep
3. power("restart")
[Output]:
Restarting the pc
4. power(0)
[Output]:
0 is a invalid argument, (shutdown, restart, sleep)
</pre>
</li>
  
<li><h3>Python</h3>
<h4>Running python scripts</h4>
<pre>
1. python: "
2. print("hello world")
3. ";
[Output]:
hello world
</pre>
</li>
 
<li><h3>Mouse</h3>
<h4>Control the mouse, click, move, both</h4>
  <ul>
    <li><h4>click()</h4>
      <h4>Left clicks the mouse. Has two arguments, if not argument provided will click on the point where the cursor is located</h4>
      <h4>First argument is the x value and the second is y value of where to click</h4>
      <pre>
mouse.click()
mouse.click(100,100)</pre>
    <li><h4>right_click()</h4>
      <h4>Same as click() only it right click's. Has two optional arguments of x and y</h4>
      <pre>
mouse.right_click()
mouse.right_click(100,100)</pre>     
    <li><h4>move()</h4>
      <h4>Moves the cursor to the given points. Needs two arguments</h4>
      <pre>mouse.move(100,100)</pre>
     <li><h4>spam_click()</h4>
      <h4>clicks the mouse multiple times based on how much the user has assigned. Takse one or three arguments. If only one argument, its the number of times click,You can also had x,y</h4>
      <pre>mouse.spam_click(100,100,5) # Will click the mouse 5 times at x=100, y=100    
      mouse.spam_click(5) # Will click 5 times at the cursor location</pre>
  </ul>
</li>  
  
<li><h3>CMD</h3>
<h4>Anything other will be interpurted as a cmd command</h4>
<pre>
dir
</pre>
</li>
</ul>

