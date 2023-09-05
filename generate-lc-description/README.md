<h2>Generate LC Description</h2>
<hr>
This script will fetch description from leetcode and writes it to a file, maintaining source formatting.

Used Selenium since Leetcode is build using react where content is rendered using JS, lightweight libraries like
requests cannot be used.

<br>

**To run -**
<pre>
install python3
</pre>

<pre>
pip3 install BeautifulSoup
pip3 install selenium
</pre>

<pre>
python3 generate_lc_description.py "$question"
</pre>

_Example:_
<pre>
python3 generate_lc_description.py "Two Sum"
</pre>
<br>

<hr>

_References_ -
<ul>
    <li>To fetch element in absence of ID:<br>
    (Here, xpath is used)<br>
    <a>https://stackoverflow.com/questions/57262217/how-do-you-use-ec-presence-of-element-locatedby-id-mydynamicelement-excep</a>
    </li>
    <li>
    To fetch element by attributes:<br>
    <a>https://stackoverflow.com/questions/2136267/beautiful-soup-and-extracting-a-div-and-its-contents-by-id</a>
    </li>
</ul>

<br>


