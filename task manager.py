#!/usr/bin/env python
# HTTPS://BIOSTUMBLEMATIC.WORDPRESS.COM
 
import sys
from pysqlite2 import dbapi2 as sqlite
 
# Creating a new task
newtask = raw_input('What do you need to do? >> ')
t = (newtask,)
 
connection = sqlite.connect('tasks.db')
cursor = connection.cursor()
cursor.execute('insert into task_list values (?, date("now"))', t)
connection.commit()
 
# Write today's tasks
cursor.execute('select * from task_list where added_on=date("now")')
 
todaystasks=[]
for row in cursor:
    todaystasks.append('> '+row[0]+'\n')
 
output = open('todaystasks.txt', 'w')    
output.writelines(todaystasks)
output.close()
 
cursor.close()
