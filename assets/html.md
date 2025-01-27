HTML Interview Questions and Answers
What is HTML?
Answer1:
HTML, or HyperText Markup Language, is a Universal language which allows an individual using special
code to create web pages to be viewed on the Internet.

Answer2:
HTML ( H yper T ext M arkup L anguage) is the language used to write Web pages. You are looking at a Web
page right now.
You can view HTML pages in two ways:

One view is their appearance on a Web browser, just like this page -- colors, different text sizes, graphics.
The other view is called "HTML Code" -- this is the code that tells the browser what to do.
What is a tag?
In HTML, a tag tells the browser what to do. When you write an HTML page, you enter tags for many reasons
-- to change the appearance of text, to show a graphic, or to make a link to another page.

What is the simplest HTML page?
HTML Code:




This is my message to the world!
Browser Display:
This is my message to the world!

How do I create frames? What is a frameset?
Frames allow an author to divide a browser window into multiple (rectangular) regions. Multiple documents
can be displayed in a single window, each within its own frame. Graphical browsers allow these frames to be
scrolled independently of each other, and links can update the document displayed in one frame without
affecting the others.
You can't just "add frames" to an existing document. Rather, you must create a frameset document that defines
a particular combination of frames, and then display your content documents inside those frames. The frameset
document should also include alternative non-framed content in a NOFRAMES element.
The HTML 4 frames model has significant design flaws that cause usability problems for web users. Frames
should be used only with great care.

How can I include comments in HTML?
Technically, since HTML is an SGML application, HTML uses SGML comment syntax. However, the full
syntax is complex, and browsers don't support it in its entirety anyway. Therefore, use the following simplified
rule to create HTML comments that both have valid syntax and work in browsers:

An HTML comment begins with "", and does not contain "--" or ">" anywhere in the
comment.
The following are examples of HTML comments:

*
* *
Do not put comments inside tags (i.e., between "<" and ">") in HTML markup.

What is a Hypertext link?
A hypertext link is a special tag that links one page to another page or resource. If you click the link, the
browser jumps to the link's destination.

How comfortable are you with writing HTML entirely by hand?

Very. I don’t usually use WYSIWYG. The only occasions when I do use Dreamweaver are when I want to
draw something to see what it looks like, and then I’ll usually either take that design and hand-modify it or
build it all over again from scratch in code. I have actually written my own desktop HTML IDE for Windows
(it’s called Less Than Slash) with the intention of deploying it for use in web development training. If has built-
in reference features, and will autocomplete code by parsing the DTD you specify in the file. That is to say, the
program doesn’t know anything about HTML until after it parses the HTML DTD you specified. This should
give you some idea of my skill level with HTML.

What is everyone using to write HTML?
Everyone has a different preference for which tool works best for them. Keep in mind that typically the less
HTML the tool requires you to know, the worse the output of the HTML. In other words, you can always do it
better by hand if you take the time to learn a little HTML.

What is a DOCTYPE? Which one do I use?
According to HTML standards, each HTML document begins with a DOCTYPE declaration that specifies
which version of HTML the document uses. Originally, the DOCTYPE declaration was used only by SGML-
based tools like HTML validators, which needed to determine which version of HTML a document used (or
claimed to use).
Today, many browsers use the document's DOCTYPE declaration to determine whether to use a stricter, more
standards-oriented layout mode, or to use a "quirks" layout mode that attempts to emulate older, buggy
browsers.

Can I nest tables within tables?
Yes, a table can be embedded inside a cell in another table. Here's a simple example:

this is the first cell of the outer table	this is the second cell of the outer table,
with the inner table embedded in it

this is the first cell of the inner table	this is the second cell of the inner table
The main caveat about nested tables is that older versions of Netscape Navigator have problems with them if

you don't explicitly close your TR, TD, and TH elements. To avoid problems, include every , , and

tag, even though the HTML specifications don't require them. Also, older versions of Netscape Navigator have problems with tables that are nested extremely deeply (e.g., tables nested ten deep). To avoid problems, avoid nesting tables more than a few deep. You may be able to use the ROWSPAN and COLSPAN attributes to minimize table nesting. Finally, be especially sure to validate your markup whenever you use nested tables.
How do I align a table to the right (or left)?
You can use

to float a table to the right. (Use ALIGN="left" to float it to the left.)
Any content that follows the closing tag will flow around the table. Use
or

to mark the end of the text that is to flow around the table, as shown in this example:
The table in this example will float to the right.

... This text will wrap to fill the available space to the left of (and if the text is long enough, below) the table.
This text will appear below the table, even if there is additional room to its left.
How can I use tables to structure forms?
Small forms are sometimes placed within a TD element within a table. This can be a useful for positioning a
form relative to other content, but it doesn't help position the form-related elements relative to each other.
To position form-related elements relative to each other, the entire table must be within the form. You cannot
start a form in one TH or TD element and end in another. You cannot place the form within the table without
placing it inside a TH or TD element. You can put the table inside the form, and then use the table to position
the INPUT, TEXTAREA, SELECT, and other form-related elements, as shown in the following example.

Account:	
Password:	
How do I center a table?
In your HTML, use

...
In your CSS, use

div.center {
text-align: center;
}

div.center table {
margin-left: auto;
margin-right: auto;
text-align: left;
}

How do I use forms?
The basic syntax for a form is:

...

When the form is submitted, the form data is sent to the URL specified in the ACTION attribute. This URL
should refer to a server-side (e.g., CGI) program that will process the form data. The form itself should contain
at least one submit button (i.e., an <INPUT TYPE="submit" ...> element),
form data elements (e.g., 
, 
, and <SELECT>) as needed, and</li>
<li>additional markup (e.g., identifying data elements, presenting instructions) as needed.</li>
</ul>
<p>How can I check for errors?<br>
HTML validators check HTML documents against a formal definition of HTML syntax and then output a list<br>
of errors. Validation is important to give the best chance of correctness on unknown browsers (both existing<br>
browsers that you haven't seen and future browsers that haven't been written yet).<br>
HTML checkers (linters) are also useful. These programs check documents for specific problems, including<br>
some caused by invalid markup and others caused by common browser bugs. Checkers may pass some invalid<br>
documents, and they may fail some valid ones.<br>
All validators are functionally equivalent; while their reporting styles may vary, they will find the same errors<br>
given identical input. Different checkers are programmed to look for different problems, so their reports will<br>
vary significantly from each other. Also, some programs that are called validators (e.g. the "CSE HTML<br>
Validator") are really linters/checkers. They are still useful, but they should not be confused with real HTML<br>
validators.<br>
When checking a site for errors for the first time, it is often useful to identify common problems that occur<br>
repeatedly in your markup. Fix these problems everywhere they occur (with an automated process if possible),<br>
and then go back to identify and fix the remaining problems.<br>
Link checkers follow all the links on a site and report which ones are no longer functioning. CSS checkers<br>
report problems with CSS style sheets.</p>
<p>Do I have to memorize a bunch of tags?<br>
No. Most programs that help you write HTML code already know most tags, and create them when you press a<br>
button. But you should understand what a tag is, and how it works. That way you can correct errors in your<br>
page more easily.</p>
<p>How do I make a form so it can be submitted by hitting ENTER?</p>
<p>The short answer is that the form should just have one <INPUT TYPE=TEXT> and no TEXTAREA, though it<br>
can have other form elements like checkboxes and radio buttons.</p>
<p>How do I set the focus to the first form field?<br>
You cannot do this with HTML. However, you can include a script after the form that sets the focus to the<br>
appropriate field, like this:</p>
<form id="myform" name="myform" action=...>
<input type="text" id="myinput" name="myinput" ...>
</form>
<script type="text/javascript">
document.myform.myinput.focus();
</script>
<p>A similar approach uses <body onload=...> to set the focus, but some browsers seem to process the ONLOAD<br>
event before the entire document (i.e., the part with the form) has been loaded.</p>
<p>How can I eliminate the extra space after a </form> tag?<br>
HTML has no mechanism to control this. However, with CSS, you can set the margin-bottom of the form to 0.<br>
For example:</p>
<form style="margin-bottom:0;" action=...>
<p>You can also use a CSS style sheet to affect all the forms on a page:<br>
form { margin-bottom: 0 ; }</p>
<p>How can I use tables to structure forms?<br>
Small forms are sometimes placed within a TD element within a table. This can be a useful for positioning a<br>
form relative to other content, but it doesn't help position the form-related elements relative to each other.<br>
To position form-related elements relative to each other, the entire table must be within the form. You cannot<br>
start a form in one TH or TD element and end in another. You cannot place the form within the table without<br>
placing it inside a TH or TD element. You can put the table inside the form, and then use the table to position<br>
the INPUT, TEXTAREA, SELECT, and other form-related elements, as shown in the following example.</p>
<form action="[URL]">
<table border="0">
<tr>
<th scope="row">
<label for="account">Account:</label>
</th>
<td>
<input type="text" name="account" id="account">
</td>
</tr>
<tr>
<th scope="row">
<label for="password">Password:
</th>
<td>
<input type="password" name="password" id="password">
</td>
</tr>
<tr>
<td> </td>
<td><input type="submit" name="Log On"></td>
</tr>
</table>
</form>
<p>Can I have two or more actions in the same form?<br>
No. A form must have exactly one action. However, the server-side (e.g., CGI) program that processes your<br>
form submissions can perform any number of tasks (e.g., updating a database, sending email, logging a<br>
transaction) in response to a single form submission.</p>
<p>How can I use forms for pull-down navigation menus?<br>
There is no way to do this in HTML only; something else must process the form. JavaScript processing will<br>
work only for readers with JavaScript-enabled browsers. CGI and other server-side processing is reliable for<br>
human readers, but search engines have problems following any form-based navigation.</p>
<p>How can I avoid using the whole URL?<br>
The URL structure defines a hierarchy (or relationship) that is similar to the hierarchy of subdirectories (or<br>
folders) in the filesystems used by most computer operating systems. The segments of a URL are separated by<br>
slash characters ("/"). When navigating the URL hierarchy, the final segment of the URL (i.e., everything after<br>
the final slash) is similar to a file in a filesystem. The other segments of the URL are similar to the<br>
subdirectories and folders in a filesystem.<br>
A relative URL omits some of the information needed to locate the referenced document. The omitted<br>
information is assumed to be the same as for the base document that contains the relative URL. This reduces<br>
the length of the URLs needed to refer to related documents, and allows document trees to be accessed via<br>
multiple access schemes (e.g., "file", "http", and "ftp") or to be moved without changing any of the embedded<br>
URLs in those documents.<br>
Before the browser can use a relative URL, it must resolve the relative URL to produce an absolute URL. If the<br>
relative URL begins with a double slash (e.g., //www.yoursite.com/faq/html/), then it will inherit only the base<br>
URL's scheme. If the relative URL begins with a single slash (e.g., /faq/html/), then it will inherit the base<br>
URL's scheme and network location.<br>
If the relative URL does not begin with a slash (e.g., all.html , ./all.html or ../html/), then it has a relative path<br>
and is resolved as follows.</p>
<ol>
<li>The browser strips everything after the last slash in the base document's URL and appends the relative URL<br>
to the result.</li>
<li>Each "." segment is deleted (e.g., ./all.html is the same as all.html, and ./ refers to the current "directory"<br>
level in the URL hierarchy).</li>
<li>Each ".." segment moves up one level in the URL hierarchy; the ".." segment is removed, along with the<br>
segment that precedes it (e.g., foo/../all.html is the same as all.html, and ../ refers to the parent "directory" level<br>
in the URL hierarchy).</li>
</ol>
<p>Some examples may help make this clear. If the base document is<br>
<URL:http://www.yoursite.com/faq/html/basics.html>, then</p>
<p>all.html and ./all.html<br>
refer to <URL:http://www.yoursite.com/faq/html/all.html><br>
./<br>
refers to <URL:http://www.yoursite.com/faq/html/><br>
../<br>
refers to <URL:http://www.yoursite.com/faq/><br>
../cgifaq.html<br>
refers to <URL:http://www.yoursite.com/faq/cgifaq.html><br>
../../reference/<br>
refers to <URL:http://www.yoursite.com/reference/></p>
<p>Please note that the browser resolves relative URLs, not the server. The server sees only the resulting absolute<br>
URL. Also, relative URLs navigate the URL hierarchy. The relationship (if any) between the URL hierarchy<br>
and the server's filesystem hierarchy is irrelevant.</p>
<p>Can I use percentage values for <TD WIDTH=...>?<br>
The HTML 3.2 and HTML 4.0 specifications allow only integer values (representing a number of pixels) for<br>
the WIDTH attribute of the TD element. However, the HTML 4.0 DTD allows percentage (and other non-<br>
integer) values, so an HTML validator will not complain about <TD WIDTH="xx%">.<br>
It should be noted that Netscape and Microsoft's browsers interpret percentage values for <TD WIDTH=...><br>
differently. However, their interpretations (and those of other table-aware browsers) happen to match when<br>
combined with <TABLE WIDTH="100%">. In such situations, percentage values can be used relatively<br>
safely, even though they are prohibited by the public specifications.</p>
<p>Why doesn't <TABLE WIDTH="100%"> use the full browser width?<br>
Graphical browsers leave a narrow margin between the edge of the display area and the content.<br>
Also note that Navigator always leaves room for a scrollbar on the right, but draws the scrollbar only when the<br>
document is long enough to require scrolling. If the document does not require scrolling, then this leaves a right<br>
"margin" that cannot be removed.</p>
<p>Why is there extra space before or after my table?<br>
This is often caused by invalid HTML syntax. Specifically, it is often caused by loose content within the table<br>
(i.e., content that is not inside a TD or TH element). There is no standard way to handle loose content within a<br>
table. Some browsers display all loose content before or after the table. When the loose content contains only<br>
multiple line breaks or empty paragraphs, then these browsers will display all this empty space before or after<br>
the table itself.<br>
The solution is to fix the HTML syntax errors. All content within a table must be within a TD or TH element.</p>
<p>How do I create a link that sends me email?<br>
Use a mailto link, for example</p>
<p>How can I have two sets of links with different colors?<br>
You can suggest this presentation in a style sheet. First, specify colors for normal links, like this:</p>
<p>a:link {color: blue; background: white}<br>
a:visited {color: purple; background: white}<br>
a:active {color: red; background: white}</p>
<p>Next, identify the links that you want to have different colors. You can use the CLASS attribute in your HTML,<br>
like this:</p>
<p><a class="example1" href="[URL]">[link text]</a><br>
Then, in your style sheet, use a selector for links with this CLASS attribute, like this:</p>
<p>a.example1:link {color: yellow; background: black}<br>
a.example1:visited {color: white; background: black}<br>
a.example1:active {color: red; background: black}</p>
<p>Alternatively, you can identify an element that contains the links that you want to have different colors, like<br>
this:</p>
<div class="example2">...
<a href="[URL]">[link text]</a>...
<a href="[URL]">[link text]</a>...
<a href="[URL]">[link text]</a>...
</div>
<p>Then, in your style sheet, use a selector for links in this containing element, like this:</p>
<p>.example2 a:link {color: yellow; background: black}<br>
.example2 a:visited {color: white; background: black}<br>
.example2 a:active {color: red; background: black}</p>
<p>How can I show HTML examples without them being interpreted as part of my document?<br>
Within the HTML example, first replace the "&" character with "&" everywhere it occurs. Then replace<br>
the "<" character with "<" and the ">" character with ">" in the same way.<br>
Note that it may be appropriate to use the CODE and/or PRE elements when displaying HTML examples.</p>
<p>How do I get special characters in my HTML?<br>
The special case of the less-than ('<'), greater-than ('>'), and ampersand ('&') characters. In general, the safest<br>
way to write HTML is in US-ASCII (ANSI X3.4, a 7-bit code), expressing characters from the upper half of<br>
the 8-bit code by using HTML entities.<br>
Working with 8-bit characters can also be successful in many practical situations: Unix and MS-Windows<br>
(using Latin-1), and also Macs (with some reservations).<br>
Latin-1 (ISO- 8859 - 1) is intended for English, French, German, Spanish, Portuguese, and various other western<br>
European languages. (It is inadequate for many languages of central and eastern Europe and elsewhere, let<br>
alone for languages not written in the Roman alphabet.) On the Web, these are the only characters reliably<br>
supported. In particular, characters 128 through 159 as used in MS-Windows are not part of the ISO- 8859 - 1<br>
code set and will not be displayed as Windows users expect. These characters include the em dash, en dash,<br>
curly quotes, bullet, and trademark symbol; neither the actual character (the single byte) nor its �nnn; decimal<br>
equivalent is correct in HTML. Also, ISO- 8859 - 1 does not include the Euro currency character. (See the last<br>
paragraph of this answer for more about such characters.)<br>
On platforms whose own character code isn't ISO- 8859 - 1, such as MS-DOS and Mac OS, there may be<br>
problems: you have to use text transfer methods that convert between the platform's own code and ISO- 8859 - 1<br>
(e.g., Fetch for the Mac), or convert separately (e.g., GNU recode). Using 7-bit ASCII with entities avoids<br>
those problems, but this FAQ is too small to cover other possibilities in detail.<br>
If you run a web server (httpd) on a platform whose own character code isn't ISO- 8859 - 1, such as a Mac or an<br>
IBM mainframe, then it's the job of the server to convert text documents into ISO- 8859 - 1 code when sending<br>
them to the network.<br>
If you want to use characters not in ISO- 8859 - 1, you must use HTML 4 or XHTML rather than HTML 3.2,<br>
choose an appropriate alternative character set (and for certain character sets, choose the encoding system too),<br>
and use one method or other of specifying this.</p>
<p>Should I put quotes around attribute values?<br>
It is never wrong to quote attribute values, and many people recommend quoting all attribute values even when<br>
the quotation marks are technically optional. XHTML 1.0 requires all attribute values to be quoted. Like<br>
previous HTML specifications, HTML 4 allows attribute values to remain unquoted in many circumstances<br>
(e.g., when the value contains only letters and digits).<br>
Be careful when your attribute value includes double quotes, for instance when you want ALT text like "the<br>
"King of Comedy" takes a bow" for an image. Humans can parse that to know where the quoted material ends,<br>
but browsers can't. You have to code the attribute value specially so that the first interior quote doesn't<br>
terminate the value prematurely. There are two main techniques:</p>
<ul>
<li>Escape any quotes inside the value with " so you don't terminate the value prematurely: ALT="the<br>
"King of Comedy" takes a bow".</li>
<li>Use single quotes to enclose the attribute value: ALT='the "King of Comedy" takes a bow'.</li>
</ul>
<p>Both these methods are correct according to the specification and are supported by current browsers, but both<br>
were poorly supported in some earlier browsers. The only truly safe advice is to rewrite the text so that the<br>
attribute value need not contain quotes, or to change the interior double quotes to single quotes, like this:<br>
ALT="the 'King of Comedy' takes a bow".</p>
<p>Posting Copy and Paste HTML<br>
For those wanting to post direct Copy and Paste HTML on screen without the use of spaces or *s etc. and the<br>
need to explain those substitutions: Use < to substitute for each opening tag < in each tagged set of HTML.<br>
Example, typing the following: <a href="http://www.yourname.com"><img<br>
src="http://pics.yourname.com/aw/pics/mask.gif"></a> Will show up on screen as: <a
href="http://www.yourname.com"><img src="http://pics.yourname.com/aw/pics/mask.gif"></a></p>
<p>HTML for Lists</p>
<ol>
<li>Bulleted Lists: <ul> begins a bulleted, indented list. Each item in the list is then prefaced with the <li> tag. It<br>
is not necessary to insert a break at the end of each line -- the <li> tag automatically creates a new line.</li>
</ol>
<ul>
<li>with <li type=disc></li>
<li>with <li type=square></li>
<li>with <li type=circle></li>
</ul>
<ol start="2">
<li>Numbered Lists: <ol> begins a numbered, indented list. Each item in the list is then prefaced with the <li><br>
tag. You need to close the list with the </ol> tag. Note: You can expand the <ol> to specify the TYPE of<br>
numbering:</li>
</ol>
<ol> 1 (decimal numbers: 1, 2, 3, 4, 5, ...)
<ol type="a"> a (lowercase alphabetic: a, b, c, d, e, ...)
<ol type="A"> A (uppercase alphabetic: A, B, C, D, E, ...)
<ol type="i"> i (lowercase Roman numerals: i, ii, iii, iv, v, ...)
<ol type="I"> I (uppercase Roman numerals: I, II, III, IV, V, ...)
<p>Are there any problems with using tables for layout?<br>
On current browsers, the entire table must be downloaded and the dimensions of everything in the table must to<br>
be known before the table can be rendered. That can delay the rendering of your content, especially if your<br>
table contains images without HEIGHT or WIDTH attributes.<br>
If any of your table's content is too wide for the available display area, then the table stretches to accomodate<br>
the oversized content. The rest of the content then adjusts to fit the oversized table rather than fitting the<br>
available display area. This can force your readers to scroll horizontally to read your content, or can cause<br>
printed versions to be cropped.<br>
For readers whose displays are narrower than the author anticipated, fixed-width tables cause the same<br>
problems as other oversized tables. For readers whose displays are wider than the author anticipated, fixed-<br>
width tables cause extremely wide margins, wasting much of the display area. For readers who need larger<br>
fonts, fixed-width tables can cause the content to be displayed in short choppy lines of only a few words each.<br>
Many browsers are especially sensitive to invalid syntax when tables are involved. Correct syntax is especially<br>
critical. Even with correct syntax, nested tables may not display correctly in older versions of Netscape<br>
Navigator.<br>
Some browsers ignore tables, or can be configured to ignore tables. These browsers will ignore any layout<br>
you've created with tables. Also, search engines ignore tables. Some search engines use the text at the<br>
beginning of a document to summarize it when it appears in search results, and some index only the first n<br>
bytes of a document. When tables are used for layout, the beginning of a document often contains many<br>
navigation links that appear before than actual content.<br>
Many versions of Navigator have problems linking to named anchors when they are inside a table that uses the<br>
ALIGN attribute. These browsers seem to associate the named anchor with the top of the table, rather than with<br>
the content of the anchor. You can avoid this problem by not using the ALIGN attribute on your tables.<br>
If you use tables for layout, you can still minimize the related problems with careful markup. Avoid placing<br>
wide images, PRE elements with long lines, long URLs, or other wide content inside tables. Rather than a<br>
single full-page layout table, use several independent tables. For example, you could use a table to lay out a<br>
navigation bar at the top/bottom of the page, and leave the main content completely outside any layout tables.</p>
<p>How do I eliminate the blue border around linked images?<br>
In your HTML, you can specify the BORDER attribute for the image:<br>
<a href=...><img src=... alt=... border="0"></a><br>
However, note that removing the border that indicates an image is a link makes it harder for users to distinguish<br>
quickly and easily which images on a web page are clickable.</p>
<p>How do I eliminate the space around/between my images?<br>
If your images are inside a table, be sure to set the BORDER, CELLSPACING, and CELLPADDING attributes<br>
to 0.<br>
Extra space between images is often created by whitespace around the <IMG> tag in the markup. It is safe to<br>
use newlines inside a tag (between attributes), but not between two tags. For example, replace this:</p>
<td ...>
<img src=... alt=...>
<img src=... alt=...>
</td>
<p>with this:</p>
<td ...><img src=... alt=...><img src=... alt=...></td>
<p>According to the latest specifications, the two should be equivalent. However, common browsers do not<br>
comply with the specifications in this situation.<br>
Finally, extra space between images can appear in documents that trigger the "standards" rendering mode of<br>
Gecko-based browsers like Mozilla and Firefox.</p>
<p>How can I specify colors?<br>
If you want others to view your web page with specific colors, the most appropriate way is to suggest the colors<br>
with a style sheet. Cascading Style Sheets use the color and background-color properties to specify text and<br>
background colors. To avoid conflicts between the reader's default colors and those suggested by the author,<br>
these two properties should always be used together.<br>
With HTML, you can suggest colors with the TEXT, LINK, VLINK (visited link), ALINK (active link), and<br>
BGCOLOR (background color) attributes of the BODY element.<br>
Note that these attributes are deprecated by HTML 4. Also, if one of these attributes is used, then all of them<br>
should be used to ensure that the reader's default colors do not interfere with those suggested by the author.<br>
Here is an example:</p>
<body bgcolor="#ffffff" text="#000000" link="#0000ff" vlink="#800080" alink="#000080">
Authors should not rely on the specified colors since browsers allow their users to override document-specified
colors.
<p>How do I get form data emailed to me?<br>
The only reliable mechanism for processing form submissions is with a server-side (e.g., CGI) program. To<br>
send form data to yourself via email, you should use a server-side program that processes the form submission<br>
and sends the data to your email address.<br>
Some web service providers make standard form-to-email programs available to their customers. Check with<br>
your service provider for details.<br>
If you can install CGI programs on your own server, see the answer to the previous question for a list of useful<br>
resources.<br>
If you can't run CGI programs on your own server, you can use a remotely hosted form-to-email services. Note<br>
that the provider of a remotely hosted service will have access to any data submitted via the service.<br>
Forms that use action="mailto:..." are unreliable. According to the HTML specifications, form behavior is<br>
explicitly undefined for mailto URIs (or anything else other than HTTP URIs). They may work one way with<br>
one software configuration, may work other ways in other software configurations, and may fail completely in<br>
other software configurations.</p>
<p>Can I prevent a form from being submitted again?<br>
No. The server-side (e.g., CGI) program that processes the form submission must handle duplicate submissions<br>
gracefully.<br>
You could generate the form with a server-side (e.g., CGI) program that adds a hidden field with a unique<br>
session ID. Then the server-side program that processes the form submission can check the session ID against a<br>
list of previously used session IDs. If the session ID has already been used, then an appropriate action can be<br>
taken (e.g., reject the submission, or update the previously submitted data).<br>
Ultimately, your server-side program must be smart enough to handle resubmitted data. But you can avoid<br>
getting resubmitted data by not expiring the confirmation page from form submissions. Since you want to</p>
<p>expire pages quickly when they have transient data, you might want to avoid putting transient data on the<br>
confirmation page. You could provide a link to a database query that returns transient data though.</p>
<p>How can I allow file uploads to my web site?<br>
These things are necessary for Web-based uploads:</p>
<ul>
<li>An HTTP server that accepts uploads.</li>
<li>Access to the /cgi-bin/ to put the receiving script. Prewritten CGI file-upload scripts are available.</li>
<li>A form implemented something like this:</li>
</ul>
<form method="post" enctype="multipart/form-data" action="fup.cgi">
File to upload: <input type=file name=upfile><br>
Notes about the file: <input type=text name=note><br>
<input type=submit value=Press> to upload the file!
</form>
<p>Not all browsers support form-based file upload, so try to give alternatives where possible.</p>
<p>The Perl CGI.pm module supports file upload. The most recent versions of the cgi-lib.pl library also support<br>
file upload. Also, if you need to do file upload in conjunction with form-to-email, the Perl package MIME::Lite<br>
handles email attachments.</p>
<p>How can I require that fields be filled in, or filled in correctly?<br>
Have the server-side (e.g., CGI) program that processes the form submission send an error message if the field<br>
is not filled in properly. Ideally, this error message should include a copy of the original form with the original<br>
(incomplete or incorrect) data filled in as the default values for the form fields. The Perl CGI.pm module<br>
provides helpful mechanisms for returning partially completed forms to the user.<br>
In addition, you could use JavaScript in the form's ONSUBMIT attribute to check the form data. If JavaScript<br>
support is enabled, then the ONSUBMIT event handler can inform the user of the problem and return false to<br>
prevent the form from being submitted.<br>
Note that the server-side program should not rely upon the checking done by the client-side script.</p>
<p>How do I change the title of a framed document?<br>
The title displayed is the title of the frameset document rather than the titles of any of the pages within frames.<br>
To change the title displayed, link to a new frameset document using TARGET="_top" (replacing the entire<br>
frameset).</p>
<p>How do I link an image to something?<br>
Just use the image as the link content, like this:</p>
<p><a href=...><img src=... alt=...></a></p>
<p>Should I end my URLs with a slash?<br>
The URL structure defines a hierarchy similar to a filesystem's hierarchy of subdirectories or folders. The<br>
segments of a URL are separated by slash characters ("/"). When navigating the URL hierarchy, the final<br>
segment of the URL (i.e., everything after the final slash) is similar to a file in a filesystem. The other segments<br>
of the URL are similar to the subdirectories and folders in a filesystem.<br>
When resolving relative URLs (see the answer to the previous question), the browser's first step is to strip<br>
everything after the last slash in the URL of the current document. If the current document's URL ends with a<br>
slash, then the final segment (the "file") of the URL is null. If you remove the final slash, then the final segment<br>
of the URL is no longer null; it is whatever follows the final remaining slash in the URL. Removing the slash<br>
changes the URL; the modified URL refers to a different document and relative URLs will resolve differently.<br>
For example, the final segment of the URL <a href="http://www.mysite.com/faq/html/">http://www.mysite.com/faq/html/</a> is empty; there is nothing after<br>
the final slash. In this document, the relative URL all.html resolves to <a href="http://www.mysite.com/faq/html/all.html">http://www.mysite.com/faq/html/all.html</a></p>
<p>(an existing document). If the final slash is omitted, then the final segment of the modified URL<br>
<a href="http://www.mysite.com/faq/html">http://www.mysite.com/faq/html</a> is "html". In this (nonexistent) document, the relative URL all.html would<br>
resolve to <a href="http://www.mysite.com/faq/all.html">http://www.mysite.com/faq/all.html</a> (another nonexistent document).<br>
When they receive a request that is missing its final slash, web servers cannot ignore the missing slash and just<br>
send the document anyway. Doing so would break any relative URLs in the document. Normally, servers are<br>
configured to send a redirection message when they receive such a request. In response to the redirection<br>
message, the browser requests the correct URL, and then the server sends the requested document. (By the way,<br>
the browser does not and cannot correct the URL on its own; only the server can determine whether the URL is<br>
missing its final slash.)<br>
This error-correction process means that URLs without their final slash will still work. However, this process<br>
wastes time and network resources. If you include the final slash when it is appropriate, then browsers won't<br>
need to send a second request to the server.<br>
The exception is when you refer to a URL with just a hostname (e.g., <a href="http://www.mysite.com">http://www.mysite.com).</a>.) In this case, the<br>
browser will assume that you want the main index ("/") from the server, and you do not have to include the<br>
final slash. However, many regard it as good style to include it anyway.</p>
<p>How do I specify a specific combination of frames instead of the default document?<br>
This is unfortunately not possible. When you navigate through a site using frames, the URL will not change as<br>
the documents in the individual frames change. This means that there is no way to indicate the combination of<br>
documents that make up the current state of the frameset.<br>
The author can provide multiple frameset documents, one for each combination of frame content. These<br>
frameset documents can be generated automatically, perhaps being created on the fly by a CGI program. Rather<br>
than linking to individual content documents, the author can link to these separate frameset documents using<br>
TARGET="_top". Thus, the URL of the current frameset document will always specify the combination of<br>
frames being displayed, which allows links, bookmarks, etc. to function normally.</p>
<p>How do I link to a location in the middle of an HTML document?<br>
First, label the destination of the link. The old way to label the destination of the link was with an anchor using<br>
the NAME attribute. For example:<br>
<h2><a name="section2">Section 2: Beyond Introductions</a></h2></p>
<p>The modern way to label the destination of the link is with an ID attribute. For example:<br>
<h2 id="section2">Section 2: Beyond Introductions</h2></p>
<p>Second, link to the labeled destination. The URL is the URL of the document, with "#" and the value of the<br>
NAME or ID attribute appended. Continuing the above examples, elsewhere in the same document you could<br>
use:<br>
<a href="#section2">go to Section 2</a></p>
<p>Similarly, in another document you could use:<br>
<a href="thesis.html#section2">go to Section 2 of my thesis</a></p>
<p>How do I create a link?<br>
Use an anchor element. The HREF attribute specifies the URL of the document that you want to link to. The<br>
following example links the text "Web Authoring FAQ" to <URL:http://www.htmlhelp.com/faq/html/>:<br>
<A HREF="http://www.yoursite.com/faq/html/">Web Authoring FAQ</A></p>
<p>How do I create a link that opens a new window?<br>
<a target="_blank" href=...> opens a new, unnamed window.<br>
<a target="example" href=...> opens a new window named "example", provided that a window or frame by that<br>
name does not already exist.<br>
Note that the TARGET attribute is not part of HTML 4 Strict. In HTML 4 Strict, new windows can be created<br>
only with JavaScript. links that open new windows can be annoying to your readers if there is not a good reason<br>
for them.</p>
<p>How do I let people download a file from my page?<br>
Once the file is uploaded to the server, you need only use an anchor reference tag to link to it. An example<br>
would be:<br>
<a href="../files/foo.zip">Download Foo Now! (100kb ZIP)</a></p>
<p>How do I create a button which acts like a link?<br>
This is best done with a small form:</p>
<FORM ACTION="[URL]" METHOD=GET>
<INPUT TYPE=submit VALUE="Text on button">
</FORM>
<p>If you want to line up buttons next to each other, you will have to put them in a one-row table, with each button<br>
in a separate cell.<br>
Note that search engines might not find the target document unless there is a normal link somewhere else on the<br>
page.<br>
A go-to-other-page button can also be coded in JavaScript, but the above is standard HTML and works for<br>
more readers.</p>
<p>How can I make a form with custom buttons?<br>
Rather than a normal submit button (<input type="submit" ...>), you can use the image input type (<input<br>
type="image" ...>). The image input type specifies a graphical submit button that functions like a server-side<br>
image map.<br>
Unlike normal submit buttons (which return a name=value pair), the image input type returns the x-y<br>
coordinates of the location where the user clicked on the image. The browser returns the x-y coordinates as<br>
name.x=000 and name.y=000 pairs.<br>
For compatability with various non-graphical browsing environments, the VALUE and ALT attributes should<br>
be set to the same value as the NAME attribute. For example:<br>
<input type="image" name="Send" alt="Send" value="Send" src="send-button.gif"><br>
For the reset button, one could use <button type="reset" ...>, JavaScript, and/or style sheets, although none of<br>
these mechanisms work universally.</p>
<p>How do I specify page breaks in HTML?<br>
There is no way in standard HTML to specify where page breaks will occur when printing a page. HTML was<br>
designed to be a device-independent structural definition language, and page breaks depend on things like the<br>
fonts and paper size that the person viewing the page is using.</p>
<p>How do I remove the border around frames?<br>
Removing the border around frames involves both not drawing the frame borders and eliminating the space<br>
between the frames. The most widely supported way to display borderless frames is <FRAMESET ...<br>
BORDER=0 FRAMEBORDER=0 FRAMESPACING=0>.<br>
Note that these attributes are proprietary and not part of the HTML 4.01 specifications. (HTML 4.01 does<br>
define the FRAMEBORDER attribute for the FRAME element, but not for the FRAMESET element.) Also,<br>
removing the border around a frame makes it difficult to resize it, as this border is also used in most GUIs to<br>
change the size of the frame.</p>
<p>Which should I use, &entityname; or &#number;?<br>
In HTML, characters can be represented in three ways:</p>
<ol>
<li>a properly coded character, in the encoding specified by the "charset" attribute of the "Content-type:" header;</li>
<li>a character entity (&entityname;), from the appropriate HTML specification (HTML 2.0/3.2, HTML 4, etc.);</li>
<li>a numeric character reference (&#number;) that specifies the Unicode reference of the desired character. We<br>
recommend using decimal references; hexadecimal references are less widely supported.</li>
</ol>
<p>In theory these representations are equally valid. In practice, authoring convenience and limited support by<br>
browsers complicate the issue.</p>
<p>HTTP being a guaranteed "8-bit clean" protocol, you can safely send out 8-bit or multibyte coded characters, in<br>
the various codings that are supported by browsers.<br>
A. HTML 2.0/3.2 (Latin-1)</p>
<p>By now there seems no convincing reason to choose &entityname; versus &#number;, so use whichever is<br>
convenient.<br>
If you can confidently handle 8-bit-coded characters this is fine too, probably preferred for writing heavily-<br>
accented languages. Take care if authoring on non-ISO- 8859 - based platforms such as Mac, Psion, IBM<br>
mainframes etc., that your upload technique delivers a correctly coded document to the server. Using &-<br>
representations avoids such problems.<br>
B. A single repertoire other than Latin- 1</p>
<p>In such codings as ISO- 8859 - 7 Greek, koi8-r Russian Cyrillic, and Chinese, Japanese and Korean (CJK)<br>
codings, use of coded characters is the most widely supported and used technique.</p>
<p>Although not covered by HTML 3.2, browsers have supported this quite widely for some time now; it is a valid<br>
option within the HTML 4 specifications--use a validator such as the WDG HTML Validator or the W3C<br>
HTML Validation Service which supports HTML 4 and understands different character encodings.</p>
<p>Browser support for coded characters may depend on configuration and font resources. In some cases,<br>
additional programs called "helpers" or "add-ins" supply virtual fonts to browsers.</p>
<p>"Add-in" programs have in the past been used to support numeric references to 15-bit or 16-bit code protocols<br>
such as Chinese Big5 or Chinese GB2312.</p>
<p>In theory you should be able to include not only coded characters but also Unicode numeric character<br>
references, but browser support is generally poor. Numeric references to the "charset-specified" encoding may<br>
appear to produce the desired characters on some browsers, but this is wrong behavior and should not be used.<br>
Character entities are also problematical, aside from the HTML-significant characters <, & etc.</p>
<p>C. Internationalization per HTML 4</p>
<p>Recent versions of the popular browsers have support for some of these features, but at time of writing it seems<br>
unwise to rely on this when authoring for a general audience.</p>
<p>Is there a way to prevent getting framed?<br>
"Getting framed" refers to having your documents displayed within someone else's frameset without your<br>
permission. This can happen accidentally (the frameset author forgot to use TARGET="_top" when linking to<br>
your document) or intentionally (the frameset author wanted to display your content with his/her own<br>
navigation or banner frames).</p>
<p>To avoid "framing" other people's documents, you must add TARGET="_top" to all links that lead to<br>
documents outside your intended scope.<br>
Unfortunately, there is no reliable way to specify that a particular document should be displayed in the full<br>
browser window, rather than in the current frame. One workaround is to use <BASE TARGET="_top"> in the<br>
document, but this only specifies the default target frame for links in the current document, not for the<br>
document itself.</p>
<p>If the reader's browser has JavaScript enabled, the following script will automatically remove any existing<br>
framesets:</p>
<script type="text/javascript">
<p>if (top.frames.length!=0) {<br>
if (window.location.href.replace)<br>
top.location.replace(self.location.href);<br>
else<br>
top.location.href=self.document.href;<br>
}</p>
</script>
<p>An alternative script is</p>
<script type="text/javascript">
function breakOut() {
if (self != top)
window.open("my URL","_top","");
}
</script>
</HEAD>
<BODY onLoad="breakOut()">
<p>Why aren't my frames the exact size I specified?<br>
Older versions of Netscape Navigator seems to convert pixel-based frame dimensions to whole percentages,<br>
and to use those percentage-based dimensions when laying out the frames. Thus, frames with pixel-based<br>
dimensions will be rendered with a slightly different size than that specified in the frameset document. The<br>
rounding error will vary depending on the exact size of the browser window.<br>
Furthermore, Navigator seems to store the percentage-based dimensions internally, rather than the original<br>
pixel-based dimensions. Thus, when a window is resized, the frames are redrawn based on the new window<br>
size and the old percentage-based dimensions.<br>
There is no way to prevent this behavior. To accommodate it, you should design your site to adapt to variations<br>
in the frame dimensions. This is another situation where it is a good idea to accommodate variations in the<br>
browser's presentation.</p>
<p>How can I specify background images?<br>
With HTML, you can suggest a background image with the BACKGROUND attribute of the BODY element.<br>
Here is an example:</p>
<body background="imagefile.gif" bgcolor="#ffffff" text="#000000" link="#0000ff" vlink="#800080"
alink="#000080">
If you specify a background image, you should also specify text, link, and background colors since the reader's
default colors may not provide adequate contrast against your background image. The background color may
be used by those not using your background image. Authors should not rely on the specified background image
since browsers allow their users to disable image loading or to override document-specified backgrounds.
<p>How can I copy something from a webpage to my webpage?<br>
1: Plaintext or any text information viewable from your browser can be easily copied like any other text from<br>
any other file.<br>
2; HTML and web scripts - you will need to view the web page's source code. In the page's source code,<br>
copying the <script> and </script> tags as well as all the information in-between these tags will usually enable<br>
the script to work on your web page.<br>
3: Images, sounds, or movies - Almost all images, sounds, and movies can be copied to your computer and then<br>
viewed on your webpage. Images can be easily copied from a webpage by right-clicking an image and selecting<br>
"Save Picture as" or "Save Image as". Unless the sound or movies file has a direct link to download and save<br>
the file to a specified location on your hard disk drive or to view your Internet browser's cache and locate the<br>
sound or movie file saved in the cache.</p>
<ol start="4">
<li>Embedded objects - Looking at the source code of the object to determine the name of the file and how it is<br>
loaded, and copy both the code and the file.</li>
</ol>
<p>Is it possible to make the HTML source not viewable?<br>
In short, there is no real method or script for making standard HTML source code not viewable. You may<br>
consider doing any of the below if they are concerned about your source code.</p>
<ol>
<li>Create the web page in Macromedia Flash or a similar program. The visitor would need to download the<br>
Macromedia Flash plug-in and would be unable to view the source code for the flash applet.</li>
<li>There are various scripts that will disable the right click feature, preventing the user from saving images or<br>
viewing the source. However, this will not protect the source code of your page. For example, Internet Explorer<br>
users may still click "View" and "Source" to view the source code of the page, or a user could disable scripts<br>
and images can be saved by simply saving the web page to the hard drive.</li>
<li>There are several programs that will help scramble your code, making it difficult (not impossible) to read.<br>
Again, this is not going to prevent someone from viewing your code.</li>
</ol>
<p>Why doesn't my title show up when I click "check it out"?<br>
You're probably looking at the wrong part of the screen. The Title usually shows up in the Title Bar on the<br>
Window, to the left of the minimize/maximize buttons on graphical browsers.</p>
<p>How do I make a thumbnail for my image(s)?<br>
Thumbnails are very useful, but they take a little bit of time to make. All you need is a graphics editing<br>
program that has functions to resize an image (sometimes it's under a function called image attributes). Be<br>
advised--when you have made a thumbnail, you will need to save it as something different than the original.<br>
Also, you will generally want to link to the larger graphic when you are done.</p>
<p>Here are the steps:</p>
<ol>
<li>Load a copy of the image into your graphics editing program.</li>
<li>Determine the ratio the thumbnail to be. (Do you want it to be half the size? One third of the size? One<br>
quarter of the size? One tenth of the size?)</li>
<li>Find the resize (or change attributes) function of your program. Most programs will recogize a percentage,<br>
for example you can type in 25% for height and width if you want the thumbnail to be a quarter of the size. (It<br>
it doesn't do percentages, you can calculate it by multiplying the pixels by the percentage. If you have a graphic<br>
that is 400 by 100, and you want it 25% of the size, multiple each measurement by .25. In this case, you'll get<br>
100 and 25.)</li>
<li>Once you are satisfied with the thumbnail, think of a name for the image. Choose Save As and enter that<br>
name. (Tip: I like to just add t after the image name. For taco.jpg I'd use tacot.jpg)</li>
<li>Upload the image to your site, and edit your HTML to load the new image name with the new, smaller size.<br>
If you wish, you can link to the larger image around the image.</li>
</ol>
<p>Example: You have taco.jpg which is 400 pixels wide and 100 pixels high. You made a thumbnail of it called<br>
tacot.jpg, which is now 100 pixels wide and 25 pixels high. After you have both images uploaded, here's the<br>
code:</p>
<p><a href="taco.jpg"><img src="tacot.jpg" width=100 height=25 border=0 alt="click for larger taco"></a><br>
You'll find border=0 to be helpful in eliminating a link-colored box around your thumbnail.</p>
<p>What is the difference between the HTML form methods GET and POST?<br>
The method parameter specifies which method the client is using to send information to the WEB server. The<br>
method determines which parameter you will find the CGI request data in:</p>
<ul>
<li>POST - post_args</li>
<li>GET - httpargs</li>
</ul>
<p>How do I rename all the files from .htm to .html after copying them from a PC to a UNIX machine?<br>
UNIX's mv (<code>move') command won't handle wildcard filenames. However, there's a program called htmaddl (for</code>HTM-add-"L"'), so you can login and type htmaddl. This will rename all .htm files to .html</p>
<p>If you haven't got this program on your UNIX machine, you can type it into a file called htmaddl:</p>
<p>#! /bin/sh</p>
<p>for f in *.htm; do<br>
base=<code>basename $f .htm</code><br>
mv $f $base.html<br>
done</p>
<p>After saving it and exiting your editor, make it executable by typing the command<br>
chmod ugo+x htmaddl<br>
Best of all, move it into your ~/bin directory, or ask your WebMeister to put it in /usr/local/bin so everyone can<br>
use it.</p>
<p>How do I put sounds for older versions of Internet Explorer?<br>
For older versions of Internet Explorer, this technique was used <BG SOUND="sound.ext">.</p>
<p>Can I use any HTML in the box?<br>
Yes. Any HTML tag that your browser supports will work in the box. So you can carry tags from chapters to<br>
chapters and mix and match...</p>
<p>How to transferring user to new web page automatically?<br>
You will need to use the below meta tag.<br>
<META HTTP-EQUIV="Refresh" CONTENT="2"; URL="http://www.yourname.com"><br>
Placing the above tag in your <HEAD></HEAD> will load yousite.com in 2 seconds.<br>
Changing the 2 value on CONTENT="2" to another value will increase or decrease the delay until loading the<br>
new page.</p>
<p>I'm trying to <code>include' a HTML document in another document...Is there a way to do this? Yes, there are several ways to do this. But remember, HTML is not a programming language - it doesn't have</code>directives': it's a markup language, so trying to compare it to C or Pascal is not going to be very meaningful.</p>
<p>SGML already provides the standard way to do this, using an entry in the DocType Declaration for a file:</p>
<!doctype html public "-//IETF//DTD HTML 3.0//EN" [
<!entity foo system "bar.html">
]>
...
and then later when you want to include the file
...
&foo;
<p>This is the General Entity mechanism used universally in normal SGML work and does exactly what is wanted,<br>
with the added benefit that you can have multiple occurrences of &foo; if you need to include some text at<br>
more than one place. Unfortunately none of the browsers except Panorama support it, basically because very<br>
few of the programmers who write browsers bothered to read up on what can be done.</p>
<ul>
<li>The second way is to use the facilities of your server. This has to be enabled by someone with access to the<br>
server configuration files (ask your WebMeister). For example, the NCSA server lets you embed a command<br>
inside an SGML comment:</li>
</ul>
<!--#exec cmd="cat myfile.html"-->
Provided this occurs in a file with a special file type (eg .shtml, and this is what has to be specified in the server
configuration), the server will parse the file and send out the result of the command embedded in the document.
<ul>
<li>There is in fact a vastly easier way to do this. SGML provides a PI mechanism (Processing Instruction) in the<br>
form:</li>
</ul>
<?cat myfile>
SGML/HTML couldn't care what you put inside (except it must not, for obvious reasons, contain the `>'
character!). This would be a great way to specify a page break, for example: suppose you were processing an
SGML file using PostScript, you could say <?showpage>...but again, none of the browsers except Panorama
support this, again because they guys who write them have never bothered to actually read up on how SGML
works.
<p>How do I keep people from stealing my source code and/or images?<br>
Because copies of your HTML files and images are stored in cache, it is impossible to prevent someone from<br>
being able to save them onto their hard drive. If you are concerned about your images, you may wish to embed<br>
a watermark with your information into the image. Consult your image editing program's help file for more<br>
details.</p>
<p>The colors on my page look different when viewed on a Mac and a PC.<br>
The Mac and the PC use slightly different color palettes. There is a 216 "browser safe" color palette that both<br>
platforms support; the Microsoft color picker page has some good information and links to other resources<br>
about this. In addition, the two platforms use different gamma (brightness) values, so a graphic that looks fine<br>
on the Mac may look too dark on the PC. The only way to address this problem is to tweak the brightness of<br>
your image so that it looks acceptable on both platforms.</p>
<p>How do you create tabs or indents in Web pages?<br>
There was a tag proposed for HTML 3.0, but it was never adopted by any major browser and the draft<br>
specification has now expired. You can simulate a tab or indent in various ways, including using a transparent<br>
GIF, but none are quite as satisfactory or widely supported as an official tag would be.</p>
<p>My page looks good on one browser, but not on another.<br>
There are slight differences between browsers, such as Netscape Navigator and Microsoft Internet Explorer, in<br>
areas such as page margins. The only real answer is to use standard HTML tags whenever possible, and view<br>
your pages in multiple browsers to see how they look.</p>
<p>How do I make sure my framed documents are displayed inside their frameset?<br>
When the sub-documents of a frameset state are accessed directly, they appear without the context of the<br>
surrounding frameset.<br>
If the reader's browser has JavaScript support enabled, the following script will restore the frameset:</p>
<SCRIPT TYPE="text/javascript">
if (parent.location.href == self.location.href) {
if (window.location.href.replace)
window.location.replace('frameset.html');
else
// causes problems with back button, but works
window.location.href = 'frameset.html';
}
</SCRIPT>
A more universal approach is a "restore frames" link:
<p><A HREF="frameset.html" TARGET="_top">Restore Frames<br>
Note that in either case, you must have a separate frameset document for every content document. If you link to<br>
the default frameset document, then your reader will get the default content document, rather than the content<br>
document he/she was trying to access. These frameset documents should be generated automatically, to avoid<br>
the tedium and inaccuracy of creating them by hand.</p>
<p>Note that you can work around the problem with bookmarking frameset states by linking to these separate<br>
frameset documents using TARGET="_top", rather than linking to the individual content documents.</p>
<p>How do I update two frames at once?<br>
There are two basic techniques for updating multiple frames with a single link: The HTML-based technique<br>
links to a new frameset document that specifies the new combination of frames. The JavaScript-based solution<br>
uses the onClick attribute of the link to update the additional frame (or frames).</p>
<p>The HTML-based technique can link to a new frameset document with the TARGET="_top" attribute<br>
(replacing the entire frameset). However, there is an alternative if the frames to be updated are part of a nested<br>
frameset. In the initial frameset document, use a secondary frameset document to define the nested frameset.<br>
For example:</p>
<p><frameset cols="*,3*"><br>
<frame src="contents.html" name="Contents"><br>
<frame src="frameset2.html" name="Display"><br>
<noframes></p>
<!-- Alternative non-framed version -->
</body></noframes>
</frameset>
<p>A link can now use the TARGET="Display" attribute to replace simultaneously all the frames defined by the<br>
frameset2.html document.<br>
The JavaScript-based solution uses the onClick attribute of the link to perform the secondary update. For<br>
example:<br>
<a href="URL1" target="Frame1" onClick="top.Frame2.location='URL2';">Update frames<br>
The link will update Frame1 with URL1 normally. If the reader's browser supports JavaScript (and has it<br>
enabled), then Frame2 will also be updated (with URL2).</p>
<p>Can I have two or more Submit buttons in the same form?<br>
Yes. This is part of HTML 2.0 Forms support (some early browsers did not support it, but browser coverage is<br>
now excellent).<br>
The submit buttons must have a NAME attribute. The optional VALUE attribute can be used to specify<br>
different text for the different submit buttons.<br>
To determine which submit button was used, you need to use different values for the NAME and/or VALUE<br>
attributes. Browsers will send to the server the name=value pair of the submit button that was used. Here is an<br>
example:</p>
<p><input type="submit" name="join" value="I want to join now"><br>
<input type="submit" name="info" value="Please send full details"></p>
<p>Note that if you are using image submit buttons, you need to provide different NAME attributes for them too.<br>
Also, browser behavior can be inconsistent when the form is submitted without a submit button (e.g., by hitting<br>
ENTER).<br>
If you're unsure what results you're going to get when you submit your form, TipJar has a standard script which<br>
you can use. Code this, for example (assuming method "post"):</p>
<form method="post" action="http://www.yoursite.com/cgi-bin/test">
and then go through the motions of submitting your form. The TipJar server decodes the form input, and
displays the result to you.
<p>How do I make a link or form in one frame update another frame?<br>
In the frameset document (the HTML document containing the <frameset> <frame> tags), make sure to name<br>
the individual frames using the NAME attribute. The following example creates a top frame named</p>
<p>"navigation" and a bottom frame named "content":<br>
<frameset rows="*,3*"><br>
<frame name="navigation" src="navigation.html"><br>
<frame name="content" src="content.html"><br>
<noframes><body></p>
<!-- Alternative non-framed version -->
</body></noframes>
</frameset>
<p>Then, in the document with the link, use the TARGET attribute to specify which frame should be used to<br>
display the link. (The value of the TARGET attribute should match the value of the target frame's NAME<br>
attribute.) For example:</p>
<p><a target="content" href=...><br>
To target a form submission, use the TARGET attribute of the FORM element, like this:</p>
<form target="content" action=...>
Note that when forms are processed entirely by JavaScript, the target frame must be specified in the JavaScript.
The value of the TARGET attribute is irrelevant.
Normally, the default target frame is the current frame ("_self"). To change the default target for every
link/form on the page, use the TARGET attribute of the BASE element, like this:
<p><base target="content"></p>
<p>When I try to upload my site, all my images are X's. How do I get them to load correctly?<br>
They are a few reasons that this could happen. The most common are:</p>
<ol>
<li>You're attempting to use a .bmp or .tif or other non-supported file format. You can only use .gif and .jpg on<br>
the web. You must convert files that are not .gif or .jpg into a .gif or .jpg with your image/graphics program.</li>
<li>You've forgotten to upload the graphic files. Double-Check.</li>
<li>You've incorrectly linked to the images. When you are starting out, try just using the file name in the <img><br>
tag. If you have cat.jpg, use<br>
img src="cat.jpg">.</li>
<li>Image file names are case-sensitive. If your file is called CaT.JpG, you cannot type cat.jpg, you must type<br>
CaT.JpG exactly in the src.</li>
<li>If all of the above fail, re-upload the image in BINARY mode. You may have accidentally uploaded the<br>
image in ASCII mode.</li>
</ol>
<p>Is there a site that shows which tags work on which browsers?<br>
There have been several attempts to do this, but I'm not aware of any really good source of comparisons<br>
between the browsers. The trouble is that there are many different versions of each browser, and many different<br>
tags. All current browsers should support the tags in the official HTML 3.2 specification, but the major ones<br>
also support nonstandard tags and sometimes have slightly different implementations. One place that has fairly<br>
good compatibility info is Browsercaps.</p>
<p>Why does the browser show my plain HTML source?<br>
If Microsoft Internet Explorer displays your document normally, but other browsers display your plain HTML<br>
source, then most likely your web server is sending the document with the MIME type "text/plain". Your web<br>
server needs to be configured to send that filename with the MIME type "text/html". Often, using the filename<br>
extension ".html" or ".htm" is all that is necessary. If you are seeing this behavior while viewing your HTML<br>
documents on your local Windows filesystem, then your text editor may have added a ".txt" filename extension<br>
automatically. You should rename filename.html.txt to filename.html so that Windows will treat the file as an<br>
HTML document.</p>
<p>How can I display an image on my page?<br>
Use an IMG element. The SRC attribute specifies the location of the image. The ALT attribute provides<br>
alternate text for those not loading images. For example:</p>
<p><img src="logo.gif" alt="ACME Products"></p>
<p>Why do my links open new windows rather than update an existing frame?<br>
If there is no existing frame with the name you used for the TARGET attribute, then a new browser window<br>
will be opened, and this window will be assigned the name you used. Furthermore, TARGET="_blank" will<br>
open a new, unnamed browser window.<br>
In HTML 4, the TARGET attribute value is case-insensitive, so that abc and ABC both refer to the same<br>
frame/window, and _top and _TOP both have the same meaning. However, most browsers treat the TARGET<br>
attribute value as case-sensitive and do not recognize ABC as being the same as abc, or _TOP as having the<br>
special meaning of _top.<br>
Also, some browsers include a security feature that prevents documents from being hijacked by third-party<br>
framesets. In these browsers, if a document's link targets a frame defined by a frameset document that is located<br>
on a different server than the document itself, then the link opens in a new window instead.</p>
<p>How do I get out of a frameset?<br>
If you are the author, this is easy. You only have to add the TARGET attribute to the link that takes readers to<br>
the intended 'outside' document. Give it the value of _top.<br>
In many current browsers, it is not possible to display a frame in the full browser window, at least not very<br>
easily. The reader would need to copy the URL of the desired frame and then request that URL manually.<br>
I would recommend that authors who want to offer readers this option add a link to the document itself in the<br>
document, with the TARGET attribute set to _top so the document displays in the full window if the link is<br>
followed.</p>
<p>How do I make a frame with a vertical scrollbar but without a horizontal scrollbar?<br>
The only way to have a frame with a vertical scrollbar but without a horizontal scrollbar is to define the frame<br>
with SCROLLING="auto" (the default), and to have content that does not require horizontal scrolling. There is<br>
no way to specify that a frame should have one scrollbar but not the other. Using SCROLLING="yes" will<br>
force scrollbars in both directions (even when they aren't needed), and using SCROLLING="no" will inhibit all<br>
scrollbars (even when scrolling is necessary to access the frame's content). There are no other values for the<br>
SCROLLING attribute.</p>
<p>Are there any problems with using frames?<br>
The fundamental problem with the design of frames is that framesets create states in the browser that are not<br>
addressable. Once any of the frames within a frameset changes from its default content, there is no longer a<br>
way to address the current state of the frameset. It is difficult to bookmark - and impossible to link or index -<br>
such a frameset state. It is impossible to reference such a frameset state in other media. When the sub-<br>
documents of such a frameset state are accessed directly, they appear without the context of the surrounding<br>
frameset. Basic browser functions (e.g., printing, moving forwards/backwards in the browser's history) behave<br>
differently with framesets. Also, browsers cannot identify which frame should have focus, which affects<br>
scrolling, searching, and the use of keyboard shortcuts in general.<br>
Furthermore, frames focus on layout rather than on information structure, and many authors of framed sites<br>
neglect to provide useful alternative content in the NOFRAMES element. Both of these factors cause<br>
accessibility problems for browsers that differ significantly from the author's expectations and for search<br>
engines.</p>
<p>Do search engines dislike frames?<br>
Search engines can link directly to framed content documents, but they cannot link to the combinations of<br>
frames for which those content documents were designed. This is the result of a fundamental flaw in the design<br>
of frames.<br>
Search engines try to provide their users with links to useful documents. Many framed content documents are</p>
<p>difficult to use when accessed directly (outside their intended frameset), so there is little benefit if search<br>
engines offer links to them. Therefore, many search engines ignore frames completely and go about indexing<br>
more useful (non-framed) documents.<br>
Search engines will index your <NOFRAMES> content, and any content that is accessible via your</p>