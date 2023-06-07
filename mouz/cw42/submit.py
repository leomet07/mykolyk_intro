#!/usr/bin/python

# Import modules for CGI handling 
import cgi
from cw42 import htmlTop
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('subject'):
   subject = form.getvalue('subject')
else:
   subject = "Not set"

htmlTop()
print(f"Subject is {form.getvalue('subject')}, form is {form.keys()}")
