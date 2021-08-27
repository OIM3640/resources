# Python Style

## Related links: 
- PEP 0008 – Style Guide for Python Code (<https://www.python.org/dev/peps/pep-0008/>)
- PEP 257 -- Docstring Conventions (<https://www.python.org/dev/peps/pep-0257/>)

Program Python like a pro! Code in the right-hand column better to employers and other places you might send your code. It also helps avoid some common pitfalls. Finally, most of the code you see will use the patterns in the right-column; practice writing code this way will help you understand code that you read, when you work on a team or with code from cookbooks and other projects.

<table>
  <tr>
    <th ></th>
    <th >Anti-Patterns</th>
    <th >Patterns</th>
  </tr>
  <tr>
    <td  rowspan="3">Conditions</td>
    <td ><code>if condition is True:</code></td>
    <td ><code>if condition:</code></td>
  </tr>
  <tr>
    <td ><code>if condition is False:</code></td>
    <td ><code>if not condition:</code></td>
  </tr>
  <tr>
    <td >
    	<code>if condition:</code>
    	<br><code>&nbsp;&nbsp;&nbsp;&nbsp;return True</code>
		<br><code>else:</code>
  		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;return False</code>
  	</td>
    <td ><code>return condition</code></td>
  </tr>
  <tr>
    <td  rowspan="3">Parentheses and Whitespace</td>
    <td >
    	<code>a =1</code>
    	<br><code>a= 1</code>
		<br><code>a=1</code>
	</td>
    <td ><code>a = 1</code></td>
  </tr>
  <tr>
    <td ><code>f (a, b)</code></td>
    <td ><code>f(a, b)</code></td>
  </tr>
  <tr>
    <td ><code>if(a == 1)</code></td>
    <td ><code>if a == 1</code></td>
  </tr>
  <tr>
    <td >Indexing</td>
    <td ><code>s[len(s) - 1]</code></td>
    <td ><code>s[-1]</code></td>
  </tr>
  <tr>
    <td  rowspan="6">Iteration</td>
    <td >
    	<code>i = 0</code>
    	<br><code>while i < n:</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
  		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;i += 1</code>
  	</td>
    <td >
    	<code>for i in range(n):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
	</td>
  </tr>
  <tr>
    <td >
    	<code>i = start</code>
    	<br><code>while i <= stop:</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
  		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;i += 1</code>
  	</td>
    <td >
    	<code>for i in range(start, stop + 1):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
	</td>
  </tr>
  <tr>
    <td >
    	<code>i = 0</code>
    	<br><code>while i < n:</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
  		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;i += 2</code>
  	</td>
    <td >
    	<code>for i in range(0, n, 2):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;…</code>
	</td>
  </tr>
  <tr>
    <td >
    	<code>for i in range(len(s)):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;do something with s[i]</code>
	</td>
    <td >
    	<code>for c in s:</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;do something with c</code>
	</td>
  </tr>
  <tr>
    <td >
    	<code>for i in range(len(s)):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;do something with i and s[i]</code>
	</td>
    <td >
    	<code>for i, c in enumerate(s):</code>
		<br><code>&nbsp;&nbsp;&nbsp;&nbsp;do something with i and s[i]</code>
	</td>
  </tr>
</table>


