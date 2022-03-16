import csv, sqlite3

con = sqlite3.connect('log.db')
cur = con.cursor()

#cur.execute('''CREATE TABLE log
#             (id integer primary key, date datetime, project_id int, task text, hours number, description text, project_hours number, total_hours number)''')

cur.execute("INSERT INTO projects (project, total_hours) VALUES (?, ?)",('Journey Log', 2))
con.commit()

#with open('log.csv','r') as file: # `with` statement available in 2.5+
    # csv.DictReader uses first line in file for column headings by default
#    reader = csv.DictReader(file) # comma is default delimiter
#    to_db = [(i['date'], i['project_id'], i['task'], i['hours'], i['description'], i['project_hours'], i['total_hours']) for i in reader]

#cur.executemany("INSERT INTO log (date, project_id, task, hours, description, project_hours, total_hours) VALUES (?, ?, ?, ?, ?, ?, ?)", to_db)
#con.commit()
#con.close()