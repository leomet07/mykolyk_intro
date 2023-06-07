#!/usr/bin/python

# Import modules for CGI handling 
import cgi
from cw43 import htmlTop
# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
if form.getvalue('drink') != None:
   subject = form.getvalue('drink')
else:
   subject = "Not set"

htmlTop()
print(f"Drink is {subject}, form keys are {form.keys()}")
