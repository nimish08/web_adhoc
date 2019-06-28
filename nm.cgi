#!/usr/bin/python3

import cgi
import subprocess
import cgitb
# to show common error in browser
cgitb.enable()

print("content-type:text/html")
print("")

webdata=cgi.FieldStorage() # this  will collect all the html code with data

# now extracting value of x
data=webdata.getvalue('x')
# sending output client via web server
#print(data)
output=subprocess.getoutput(data)
print("<pre>")
#print("<h1>")
print(output)
#print("/h1")
