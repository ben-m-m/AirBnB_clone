<main>
        <div id="layout-bars">        
<h1 class="d-flex flex-column gap-2">
  <span>AirBnB clone</span>
</h1>

<div>
  
</div>

<div class="gap formatted-content">
    <p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6fb2f5cd2372b3f233420753e882720c45f4a7767407ee5c56b8d9c02ea043a5" alt="" loading='lazy' style="" /></p>


<p>The AirBnB clone project starts now until&hellip; the end of the first year. The goal of the project is to deploy on our server a simple copy of the <a href="/rltoken/m8g02HcD2ovrl_K-zulYBw" title="AirBnB website" target="_blank">AirBnB website</a>.</p>

<p>We won&rsquo;t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.</p>

<p>After 4 months, We will have a complete web application composed by:</p>

<ul>
<li>A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)</li>
<li>A website (the front-end) that shows the final product to everybody: static and dynamic</li>
<li>A database or files that store data (data = objects)</li>
<li>An API that provides a communication interface between the front-end and our data (retrieve, create, delete, update them)</li>
</ul>

<h2>Final product</h2>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e8531350dc4c1cef82f6d6e6c43e408895281f110aee569c8e2a6cce615326d3" alt="" loading='lazy' style="" />
<img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/da2584da58f1d99a72f0a4d8d22c1e485468f941.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=4f63fd64414cbebddedb0dd2165c2ed116f3fd117216dc0cd48285a8c8ab6bb1" alt="" loading='lazy' style="" /></p>

<h2>Concepts to learn</h2>

<ul>
<li><a href="/rltoken/87ml5W9WzLbH7yAJuGk_mA" title="Unittest" target="_blank">Unittest</a> - and we should work all together on tests cases</li>
<li><strong>Python packages</strong> concept page</li>
<li>Serialization/Deserialization</li>
<li><code>*args, **kwargs</code></li>
<li><code>datetime</code></li>
<li>More coming soon!</li>
</ul>

<h2>Steps</h2>

<p>We won&rsquo;t build this application all at once, but step by step.</p>

<p>Each step will link to a concept:</p>

<h3>The console</h3>

<ul>
<li>create our data model</li>
<li>manage (create, update, destroy, etc) objects via a console / command interpreter</li>
<li>store and persist objects to a file (JSON file)</li>
</ul>

<p>The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between &ldquo;My object&rdquo; and &ldquo;How they are stored and persisted&rdquo;. This means:
from our console code (the command interpreter itself) and from the front-end and RestAPI we will build later, we won&rsquo;t have to pay attention (take care) of how our objects are stored. </p>

<p>This abstraction will also allow us to change the type of storage easily without updating all of our codebase.</p>

<p>The console will be a tool to validate this storage engine</p>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=7190fbbe4911441a48740447cf34041ec5a4550432c4aea0fcce300b309a69e1" alt="" loading='lazy' style="" /></p>

<h3>Web static</h3>

<ul>
<li>learn HTML/CSS</li>
<li>create the HTML of our application</li>
<li>create template of each object</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/87c01524ada6080f40fc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e50aa7d138693f6c89a5180c1e21b6c7f8dc41d632fffb95fa0e2e182ef16bd8" alt="" loading='lazy' style="" /></p>

<h3>MySQL storage</h3>

<ul>
<li>replace the file storage by a Database storage</li>
<li>map our models to a table in database by using an O.R.M.</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/5284383714459fa68841.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=12127580b88a42cb133772def5a4a95fa7bf30af9a44cf5f05c3d37a8563e9a0" alt="" loading='lazy' style="" /></p>

<h3>Web framework - templating</h3>

<ul>
<li>create our first web server in Python</li>
<li>make our static HTML file dynamic by using objects stored in a file or database</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/cb778ec8a13acecb53ef.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=20bf440923d2d4afd141bb09882448c9464fe515dbe0b1609db5bb8b1b7a6556" alt="" loading='lazy' style="" /></p>

<h3>RESTful API</h3>

<ul>
<li>expose all our objects stored via a JSON web interface</li>
<li>manipulate our objects via a RESTful API</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/06fccc41df40ab8f9d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d119b0cbf154a744ce569304901592b163f468b6d47b41baa549fd4e642a420f" alt="" loading='lazy' style="" /></p>

<h3>Web dynamic</h3>

<ul>
<li>learn JQuery</li>
<li>load objects from the client side by using our own RESTful API</li>
</ul>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/d2d06462824fab5846f3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=cd340aa69505aefd10e389b27a4567fd8e652f4a2e545989310a02dd50bb94ae" alt="" loading='lazy' style="" /></p>

<h2>Files and Directories</h2>

<ul>
<li><code>models</code> directory will contain all classes used for the entire project. A class, called &ldquo;model&rdquo; in a OOP project is the representation of an object/instance.</li>
<li><code>tests</code> directory will contain all unit tests.</li>
<li><code>console.py</code> file is the entry point of our command interpreter.</li>
<li><code>models/base_model.py</code> file is the base class of all our models. It contains common elements:

<ul>
<li>attributes: <code>id</code>, <code>created_at</code> and <code>updated_at</code></li>
<li>methods: <code>save()</code> and <code>to_json()</code></li>
</ul></li>
<li><code>models/engine</code> directory will contain all storage classes (using the same prototype). For the moment we will have only one: <code>file_storage.py</code>.</li>
</ul>

<h2>Storage</h2>

<p>Persistency is really important for a web application. It means: every time our program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won&rsquo;t be saved and will be gone.</p>

<p>In this project, we will manipulate 2 types of storage: file and database. For the moment, we will focus on file. </p>

<p>Why separate &ldquo;storage management&rdquo; from &ldquo;model&rdquo;? It&rsquo;s to make our models modular and independent. With this architecture, we can easily replace our storage system without re-coding everything everywhere.</p>

<p>We will always use class attributes for any object. Why not instance attributes? For 3 reasons:</p>

<ul>
<li>Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc&hellip;)</li>
<li>Provide default value of any attribute</li>
<li>In the future, provide the same model behavior for file storage or database storage</li>
</ul>

<h3>How can I store my instances?</h3>

<p>That&rsquo;s a good question. So let&rsquo;s take a look at this code:</p>

<pre><code>class Student():
    def __init__(self, name):
        self.name = name

students = []
s = Student(&quot;John&quot;)
students.append(s)
</code></pre>

<p>Here, I&rsquo;m creating a student and store it in a list. But after this program execution, my Student instance doesn&rsquo;t exist anymore.</p>

<pre><code>class Student():
    def __init__(self, name):
        self.name = name

students = reload() # recreate the list of Student objects from a file
s = Student(&quot;John&quot;)
students.append(s)
save(students) # save all Student objects to a file
</code></pre>

<p>Nice!</p>

<p>But how it works?</p>

<p>First, let&rsquo;s look at <code>save(students)</code>:</p>

<ul>
<li>Can I write each <code>Student</code> object to a file =&gt; <em>NO</em>, it will be the memory representation of the object. For another program execution, this memory representation can&rsquo;t be reloaded.</li>
<li>Can I write each <code>Student.name</code> to a file =&gt; <em>YES</em>, but imagine you have other attributes to describe <code>Student</code>? It would start to be become too complex.</li>
</ul>

<p>The best solution is to convert this list of <code>Student</code> objects to a JSON representation.</p>

<p>Why JSON? Because it&rsquo;s a standard representation of object. It allows us to share this data with other developers, be human readable, but mainly to be understood by another language/program.</p>

<p>Example:</p>

<ul>
<li>My Python program creates <code>Student</code> objects and saves them to a JSON file</li>
<li>Another Javascript program can read this JSON file and manipulate its own <code>Student</code> class/representation</li>
</ul>

<p>And the <code>reload()</code>? now you know the file is a JSON file representing all <code>Student</code> objects. So <code>reload()</code> has to read the file, parse the JSON string, and re-create <code>Student</code> objects based on this data-structure.</p>

<h3>File storage == JSON serialization</h3>

<p>For this first step, we have to write in a file all our objects/instances created/updated in our command interpreter and restore them when we start it.
We can&rsquo;t store and restore a Python instance of a class as &ldquo;Bytes&rdquo;, the only way is to convert it to a serializable data structure:</p>

<ul>
<li>convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method <code>my_instance.to_json()</code> to retrieve a dictionary</li>
<li>convert this data structure to a string (JSON format, but it can be YAML, XML, CSV&hellip;) - for us it will be a <code>my_string = JSON.dumps(my_dict)</code></li>
<li>write this string to a file on disk</li>
</ul>

<p>And the process of deserialization?</p>

<p>The same but in the other way:</p>

<ul>
<li>read a string from a file on disk</li>
<li>convert this string to a data structure. This string is a JSON representation, so it&rsquo;s easy to convert - for us it will be a <code>my_dict = JSON.loads(my_string)</code></li>
<li>convert this data structure to instance - for us it will be a <code>my_instance = MyObject(my_dict)</code></li>
</ul>

<h2><code>*args, **kwargs</code></h2>

<p><a href="/rltoken/seHCY0Sq6m_-PBetEnBACg" title="How To Use them" target="_blank">How To Use them</a></p>

<p>How do you pass arguments to a function?</p>

<pre><code>def my_fct(param_1, param_2):
    ...

my_fct(&quot;Best&quot;, &quot;School&quot;)
</code></pre>

<p>But with this function definition, you must call <code>my_fct</code> with 2 parameters, no more, no less.</p>

<p>Can it be dynamic? Yes we can:</p>

<pre><code>def my_fct(*args, **kwargs):
    ...

my_fct(&quot;Best&quot;, &quot;School&quot;)
</code></pre>

<p>What? What&rsquo;s <code>*args</code> and <code>**kwargs</code>?</p>

<ul>
<li><code>*args</code> is a Tuple that contains all arguments </li>
<li><code>*kwargs</code> is a dictionary that contains all arguments by key/value</li>
</ul>

<p>A dictionary? But why?</p>

<p>So, to make it clear, <code>*args</code> is the list of anonymous arguments, no name, just an order. <code>**kwargs</code> is the dictionary with all named arguments.</p>

<p>Examples:</p>

<pre><code>def my_fct(*args, **kwargs):
    print(&quot;{} - {}&quot;.format(args, kwargs))

my_fct() # () - {}
my_fct(&quot;Best&quot;) # (&#39;Best&#39;,) - {}
my_fct(&quot;Best&quot;, 89) # (&#39;Best&#39;, 89) - {}
my_fct(name=&quot;Best&quot;) # () - {&#39;name&#39;: &#39;Best&#39;}
my_fct(name=&quot;Best&quot;, number=89) # () - {&#39;name&#39;: &#39;Best&#39;, &#39;number&#39;: 89}
my_fct(&quot;School&quot;, 12, name=&quot;Best&quot;, number=89) # (&#39;School&#39;, 12) - {&#39;name&#39;: &#39;Best&#39;, &#39;number&#39;: 89}
</code></pre>

<p>Perfect? Of course we can mix both, but the order should be first all anonymous arguments, and after named arguments.</p>

<p>Last example:</p>

<pre><code>def my_fct(*args, **kwargs):
    print(&quot;{} - {}&quot;.format(args, kwargs))

a_dict = { &#39;name&#39;: &quot;Best&quot;, &#39;age&#39;: 89 }

my_fct(a_dict) # ({&#39;age&#39;: 89, &#39;name&#39;: &#39;Best&#39;},) - {}
my_fct(*a_dict) # (&#39;age&#39;, &#39;name&#39;) - {}
my_fct(**a_dict) # () - {&#39;age&#39;: 89, &#39;name&#39;: &#39;Best&#39;}
</code></pre>

<p>We can play with these 2 arguments to clearly understand where and how our variables are stored.</p>

<h2><code>datetime</code></h2>

<p><code>datetime</code> is a Python module to manipulate date, time etc&hellip;</p>

<p>In this example, we create an instance of <code>datetime</code> with the current date and time:</p>

<pre><code>from datetime import datetime

date_now = datetime.now()
print(type(date_now)) # &lt;class &#39;datetime.datetime&#39;&gt;
print(date_now) # 2017-06-08 20:42:42.170922
</code></pre>

<p><code>date_now</code> is an object, so we can manipulate it:</p>

<pre><code>from datetime import timedelta

date_tomorrow = date_now + timedelta(days=1)
print(date_tomorrow) # 2017-06-09 20:42:42.170922
</code></pre>

<p>&hellip; we can also store it:</p>

<pre><code>a_dict = { &#39;my_date&#39;: date_now }
print(type(a_dict[&#39;my_date&#39;])) # &lt;class &#39;datetime.datetime&#39;&gt;
print(a_dict) # {&#39;my_date&#39;: datetime.datetime(2017, 6, 8, 20, 42, 42, 170922)}
</code></pre>

<p>What? What&rsquo;s this format when a <code>datetime</code> instance is in a datastructure??? It&rsquo;s unreadable.</p>

<p>How to make it readable: <a href="/rltoken/mLLWq3qIJc396KdHxI7sBw" title="strftime" target="_blank">strftime</a></p>

<pre><code>print(date_now.strftime(&quot;%A&quot;)) # Thursday
print(date_now.strftime(&quot;%A %d %B %Y at %H:%M:%S&quot;)) # Thursday 08 June 2017 at 20:42:42
</code></pre>

<h2>Data diagram</h2>

<p><img src="https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230510%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230510T122348Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=e7ed4977b6e8f085a0addc3c0421e2ce57d5203913f2badc423da5f250ab991a" alt="" loading='lazy' style="" /></p>

</div>
<i aria-hidden="true" class="fa fa-search "></i>
<i aria-hidden="true" class="fa fa-window-minimize "></i>
</button>
</div>
</div>
</div>