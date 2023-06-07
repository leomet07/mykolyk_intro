#!/usr/bin/python3

import cgi
import random

def htmlFile():
    with open("checkbox.html") as file_obj:
        return file_obj.read().strip()

def htmlTop():
    print("Content-Type: text/html\n\n")

def getData():
       
    formData = cgi.FieldStorage()
    firstname = formData.getvalue("first_name")
    return firstname
        
 

def main():
    htmlTop()
    print(htmlFile())
    #print('Hello {}'.format(getData()))
    #print('Random number {}'.format(random.randint(1,100)))
    #htmlTail()


if __name__ == '__main__':
    try:
        main()
    except:
        cgi.print_exception()
