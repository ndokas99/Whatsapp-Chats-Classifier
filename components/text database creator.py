import sqlite3

conn = sqlite3.connect("../databases/textData.db")

conn.execute("create table Labels(html text)")

conn.execute("create table Help(html text);")

conn.execute("create table About(html text);")

conn.execute("create table Display(html text)")

conn.execute("create table Saves(html text)")

save = "<html><head/><body><p><span style=\"font-size:10pt; font-weight:600;\">ENTER SAVE NAME</span></p></body></html>"
ogLabel = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
           PREPROCESSING CHAT LOG</span></p></body></html>"""
nextText = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
           CLASSIFYING CHATS </span></p></body></html>"""
tab0 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "School Information" Chats</span></p></body></html>"""
tab1 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "Advertising" Chats</span></p></body></html>"""
tab2 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "Computers and Tech" Chats</span></p></body></html>"""
tab3 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing 'Politics' Chats</span></p></body></html>"""
tab4 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "Religion" Chats</span></p></body></html>"""
tab5 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "Science" Chats</span></p></body></html>"""
tab6 = """<html><head/><body><p align="center"><span style="font-size:12pt; font-weight:600; font-style:italic;">
       Writing "Sports" Chats</span></p></body></html>"""


text0 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt;; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">OPEN</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Opens a new Whatsapp chat log.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Opening a  text file which does not contain the format of the exported chat log will cause processing to not \
occur which will result either in no output or undesired results.</span></p></body></html>"""

text1 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">SAVE</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Save the results of classification to a local database.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Can be reviewed later by opening 'Manage Saved'.</span></p></body></html>"""

text2 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">MANAGE SAVED</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Allows management of past results through:</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>1. Open past results for reviewing.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>2. Deleting of previously saved results.</span></p></body></html>"""

text3 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">POSITION TABS AT TOP</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Move the category tabs to the upper part of the interface.</span></p></body></html>"""

text4 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">POSITION TABS AT BOTTOM</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>Move the category tabs to the lower part of the interface.</span></p></body></html>"""

text5 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">FUNCTIONALITY HELP</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>View help of:</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>1. How the application works.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>2. Known bugs</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>3. Limitations</span></p></body></html>"""

text6 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">INTERFACE HELP</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>View this help about how to use this application's interface.</span></p></body></html>"""

text7 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">ABOUT WHATSAPP FILTER</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>View information about the application. </span></p></body></html>"""

text8 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style></head><body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;">
<p><span style="font-size:11pt; font-weight:600;">ABOUT CREATORS</span></p>
<hr />
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>View information about the people who created the application.</span></p>
</body></html>"""

text9 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin:0px;-qt-block-indent:0; text-indent:0px;}
</style>
</head>
<body style="font-family:'Tahoma'; font-size:10pt; font-weight:400; font-style:normal;" bgcolor="#efefef">
<p align="center"><span style="font-size:11pt; font-weight:600; color:#0055ff;">OPENING</span></p>
<hr />
<p><span>Opening a new chat log will lead to progressbar being opened which the user should wait for until it finishes.
</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span style="font-weight:600;">N.B: The interface may not respond for a time when the user chooses a log to be \
processed. This is not an error , so user should wait until progressbar loads.</span></p>
<p style="-qt-paragraph-type:empty; font-weight:600;"><br /></p>
<p style="-qt-paragraph-type:empty; font-weight:600;"><br /></p>
<p align="center"><span style="font-size:11pt; font-weight:600; color:#0055ff;">SAVING</span></p>
<hr />
<p><span>Results can be saved to a local database. They can then be viewed or deleted using the </span>
<span style="font-weight:600;">Manage Saved </span><span>section.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p align="center"><span style="font-size:11pt; font-weight:600; color:#0055ff;">CATEGORIZATION</span></p>
<hr />
<p><span>Results are classified into 7 categories namely:</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span>1. </span><span style="font-weight:600;">Learning</span><span> i.e. student-associated messages which refer \
to things like assignments, lectures, internship or timetables.</span></p>
<p><span>2. </span><span style="font-weight:600;">Computers and Tech </span><span>i.e. messages which cover \
aspects like computer systems, electronics and other technologies.</span></p>
<p><span>3. </span><span style="font-weight:600;">Advertisements</span><span> i.e. messages which appear to be \
advertising products.</span></p>
<p><span>4. </span><span style="font-weight:600;">Science</span><span> i.e. messages which cover scientific subjects \
like medicine and cosmology</span></p>
<p><span>5. </span><span style="font-weight:600;">Religion</span><span> i.e. messages which address issues to do with \
religious beliefs.</span></p>
<p><span>6. </span><span style="font-weight:600;">Politics </span><span>i.e. messages which address issues associated \
with government politics.</span></p>
<p><span>7. </span><span style="font-weight:600;">Sports </span><span>i.e. messages which talk about sporting \
activities like athletics, cricket, football, rugby and tennis.</span></p>
<p style="-qt-paragraph-type:empty;"><br /></p>
<p><span style="font-weight:600;">Note:</span></p>
<p><span>Categorization of unclear messages or of those not in these categories will result in the application making a\
 best-fit approximation.</span></p></body></html>"""

text10 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<meta name="qrichtext" content="1" />
<style type="text/css">
p {white-space: pre-wrap; margin: 0px; -qt-block-indent:0; text-indent:0px; text-align: center;}
span {font-size: 12pt;}
</style>
</head>
<body style="font-family:'Tahoma'; font-weight:400; font-style:normal;" bgcolor="#f0f0f0">
<p><img src="media/logo.png" width="375" height="85" /></p>
<hr />
<p><span>This is an AI-powered application</span></p>
<p><span>which groups Whatsapp messages into</span></p>
<p><span>different categories.</span></p>
<hr />
<p>
<span style="font-family:'Algerian'; font-weight:600; text-decoration: underline; font-size:14pt">PURPOSE</span>
</p>
<p><span>To combat the problem of information-overload on </span></p>
<p><span>Whatsapp so as to identify messages which one </span></p>
<p><span>deems relevant at a given moment.</span></p>
</body>
</html>"""

text11 = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html>
<head>
<meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
p {margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;}
</style>
</head>
<body style="font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;" bgcolor="#f0f0f0">
<p align="center" style="-qt-paragraph-type:empty;"><br /></p>
<p align="center"><span style="font-size:12pt;">This application was created by a University of </span></p>
<p align="center"><span style="font-size:12pt;">Zimbabwe student as part of their degree's</span></p>
<p align="center"><span style="font-size:12pt; font-weight:600;">Practical Project</span><span style=" font-size:12pt;">.</span></p>
<hr />
<p align="center" style="-qt-paragraph-type:empty;"><br /></p>
<p><span style=" font-size:12pt;">  Name:                               </span><span style=" font-size:11pt;">Kudakwashe Ndokanga</span></p>
<p><span style=" font-size:12pt;">  Degree:       </span><span style=" font-size:11pt;">Business Studies and Computing Science</span></p>
<p><span style=" font-size:12pt;">  Contact number:                      </span><span style=" font-size:11pt;">+263 787 814 090</span></p>
<p><span style=" font-size:12pt;">  Email:                        </span><span style="font-size:11pt; text-decoration: underline; color:#0000ff;">ndokaskuda1999@gmail.com</span></p>
<p><span style=" font-size:12pt;">  LinkedIn:            </span><span style=" font-size:11pt; text-decoration: underline; color:#0000ff;">kudakwashe-ndokanga-96b116205</span></p>
<p><span style=" font-size:12pt;">  Github handle:                                     </span><span style=" font-size:11pt; text-decoration: underline; color:#0000ff;">ndokas99</span></p>
</body>
</html>"""

tabHtml = """<!doctype html><html><head><meta charset="utf-8"><title>Testing</title><style>
body{ font-family: Times New Roman; margin: 0px; height: 100vh;
background: linear-gradient(to bottom right, #80011F, darkgreen, #37235B); background-attachment: fixed;}
div{ width: 90%; margin-left: 5%; border: 1px solid black; border-radius: 30px; background: white; margin-bottom: 5px}
.span1{ color: darkblue;}
.span2{ float: right; padding-right: 20px; color: purple;}
div p { margin-top: 2px; margin-right: 0; margin-bottom: 2px; margin-left: 20px;}
</style></head><body><br>"""

tabEnd = """</body></html>"""

savedName = """<html>
<head/>
<body>
<p align="center">
<span style="font-size:10pt; font-weight:600; text-decoration: underline;">NAME</span>
</p>
</body>
</html>"""

savedDate = """<html>
<head/>
<body>
<p align="center">
<span style="font-size:10pt; font-weight:600; text-decoration: underline;">DATE CREATED</span>
</p>
</body>
</html>"""

saveStart = """<html><head/><body><p align="center"><span style="font-size:10pt; font-weight:300;">"""
saveEnd = """</span></p></body></html>"""


labels = [save, ogLabel, nextText, tab0, tab1, tab2, tab3, tab4, tab5, tab6]
for text in labels:
    conn.execute("insert into Labels values (?);", [text])

intHelp = [text0, text1, text2, text3, text4, text5, text6, text7, text8, text9]
for text in intHelp:
    conn.execute("insert into Help values (?);", [text])

about = [text10, text11]
for text in about:
    conn.execute("insert into About values (?);", [text])

tabs = [tabHtml, tabEnd]
for text in tabs:
    conn.execute("insert into Display values (?);", [text])

saves = [savedName, savedDate, saveStart, saveEnd]
for text in saves:
    conn.execute("insert into Saves values (?);", [text])

conn.commit()

conn.close()

