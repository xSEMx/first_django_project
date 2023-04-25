import os
import asyncio
import aiohttp
import aiosqlite
from aiosmtplib import SMTP
from telegram import Bot
from dotenv import load_dotenv
from django.conf import settings

load_dotenv('.env')

async def get_notification_urls():
    async with aiosqlite.connect('db.sqlite3') as conn:
        async with conn.execute("SELECT sites.id, sites.url FROM monitoring_vus_sites sites WHERE sites.status = 1") as query:
            query_res = await query.fetchall()
            notification_urls = {i[0]: i[1] for i in query_res}

            return notification_urls


async def send_email(contact, message):
    try:
        async with SMTP(hostname="smtp.mail.ru", port=465, use_tls=True, timeout=30) as smtp:
            await smtp.login('samir_abbasov_1977@bk.ru', os.getenv('EMAIL_PASSWORD'))
            await smtp.sendmail('samir_abbasov_1977@bk.ru', contact, message)
            return True
        
    except Exception:
        return False

        
async def process_site(conn, site):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(site['url']) as resp: 
                status_code = resp.status
                true_status = True if status_code == 200 else False

                await conn.execute("UPDATE monitoring_vus_sites SET status = ? WHERE id = ?", (true_status, site['id']))
                await conn.commit()
                    
        except aiohttp.InvalidURL as e:
            print(f"Error while sending request to {url}: {e}")


async def process_notification(conn, notification):
    site_url = await conn.execute("SELECT url FROM monitoring_vus_sites WHERE id = ?", (notification['site_id'],))  
    site_url = await site_url.fetchone()
    site_url = site_url[0]

    message = f"Сайт {site_url} доступен для посещения".encode("utf-8")

    sent = await send_email(notification['email'], message)   

    if sent:
        await conn.execute("DELETE FROM monitoring_vus_notifications WHERE id = ?", (notification['id'],))
        await conn.commit()


async def update_sites_status(conn):
    async with conn.execute("SELECT * FROM monitoring_vus_sites") as sites_query:
        rows = await sites_query.fetchall()
        column_names = [description[0] for description in sites_query.description]
        sites = [dict(zip(column_names, row)) for row in rows]


    async with conn.execute("SELECT n.* FROM monitoring_vus_notifications n JOIN monitoring_vus_sites s ON n.site_id = s.id WHERE s.status = 1") as notifications_query:
        rows = await notifications_query.fetchall()
        column_names = [description[0] for description in notifications_query.description]
        notifications = [dict(zip(column_names, row)) for row in rows]

    tasks = []
    for site in sites:
        tasks.append(process_site(conn, site))

    for notification in notifications:
        tasks.append(process_notification(conn, notification))

    await asyncio.gather(*tasks)


async def update_db():
    async with aiosqlite.connect('db.sqlite3') as conn:
        while True:
            await update_sites_status(conn)
            print('True')
            await asyncio.sleep(60)

def start_updating_db():
    asyncio.run(update_db())
