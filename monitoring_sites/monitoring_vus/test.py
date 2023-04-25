import sqlite3
import random

sites = {
	'https://www.hse.ru/': 13,
	'https://spbu.ru/': 12,
	'https://mephi.ru/': 11,
	'https://mipt.ru/': 10,
	'https://www.msu.ru/': 9
}

users_id = [i for i in range(1,12)]

query = """
	INSERT INTO monitoring_vus_comments (user_id, site_id, evaluation, review)
	VALUES (?, ?, ?, ?) 
"""

conn = sqlite3.Connection(r'C:\Users\user\Desktop\project_2\project_prof\monitoring_sites\db.sqlite3')
cursor = conn.cursor()

for site in sites:
	site_id = sites[site]
	for user_id in users_id:
		evaluation = random.randint(1,5)
		print(f'[INFO] evaluation = {evaluation}')
		review = input('Введите отзыв:\n') 

		try:
			cursor.execute(query, (user_id, site_id, evaluation, review))

			print('[+] Sucsess')
		except Exception as _ex:
			print(_ex)

conn.commit()
conn.close()