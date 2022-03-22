import csv, sqlite3

con = sqlite3.connect('log.db')
cur = con.cursor()

#cur.execute('''CREATE TABLE log
#             (id integer primary key, date datetime, project_id int, task text, hours number, description text, project_hours number, total_hours number)''')

#cur.execute('''CREATE TABLE projects
#             (id integer primary key, project text, total_hours number)''')

#cur.execute("DROP TABLE projects")
#con.commit()

#cur.execute("INSERT INTO projects (project, total_hours) VALUES (?, ?)",('Journey Log', 2))
#con.commit()

#with open('log.csv','r') as file: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
#    reader = csv.DictReader(file) # comma is default delimiter
#    to_db = [(i['date'], i['project_id'], i['task'], i['hours'], i['description'], i['project_hours'], i['total_hours']) for i in reader]

#cur.executemany("INSERT INTO log (date, project_id, task, hours, description, project_hours, total_hours) VALUES (?, ?, ?, ?, ?, ?, ?)", to_db)
#con.commit()
#con.close()

#cur.execute("INSERT INTO log (date, project_id, task, hours, description, project_hours, total_hours) VALUES(?, ?, ?, ?, ?, ?, ?)",("2022-03-17", 7, "Creating Log", 3, "", 11, 172))
#con.commit()
#cur.execute("INSERT INTO log (date, project_id, task, hours, description, project_hours, total_hours) VALUES(?, ?, ?, ?, ?, ?, ?)",("2022-03-21", 1, "Final Project", 19, "Really struggled with trying various data visualisation frameworks. Ended up using Google Charts and have finally got it working! Struggling to fully understand Javascript but really want to get my head around it", 140, 191))
#con.commit()

cur.execute('''UPDATE projects SET total_hours = 140 WHERE id = 1''')
con.commit()
cur.execute('''UPDATE projects SET total_hours = 8 WHERE id = 7''')
con.commit()

#cur.execute('''UPDATE log SET project_hours = 8 WHERE id = 58''')
#con.commit()

#check for missing rows from work pc
#update journey log total in projects tables