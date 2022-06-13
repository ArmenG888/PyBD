# PyBD
<h1>Work in Progress</h1>
<h1>DO IT ON YOUR OWN RISK AND WITH CONSENT</h1>
<h4>We are not responsible for any damage you do</h4>
Backdoor made with python, django, sqlite (WIP)

<h1>What is a backdoor?</h1>
Basically you can gain access to another persons computer.



<h1>Usage:</h1>
<h4>First install all the libraries you need for this</h4>
<pre>pip install -r requirments.txt</pre>
<h4>Than, you need to start the server</h4>
<pre>cd server</pre>
<pre>python manage.py runserver</pre>
<h4>Run the main.py on the target machine</h4>
<pre>cd client</pre>
<pre>python main.py</pre>


<h1>Language</h1>


Will type hello and bye on the victims computer
<pre>
keyboard:"
Hello
bye
";
</pre>

<h4>Read files</h4>
<pre>read: "test.txt"</pre>
<h4>Read multiple files (infinite amount)</h4>
<pre>read: "file_name", "filename_2"</pre>

<h4>Running python scripts</h4>
<pre>python: "
print("hello world")
";
</pre>

<h4>Anything other will be interpurted as a cmd command</h4>
<pre>
cd ..
dir
</pre>
