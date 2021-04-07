import cloudscraper
from bs4 import BeautifulSoup as BS
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import date 
import database_handler
import Email_temp
import Email_handler

"""
   This is the which will scrape the website 
    udemylearn.blogpost.com for the update of new courses and
    it will save the link of the new discounted courses
    an and send you a e-mail for latest notifcation.
       
"""
current_date =  date.today()

def scrape():
    BASE_URL = "https://www.booksandcoupons.com/"
    course_list = []
    course_dict = {}
    udemy_url = []
    browser = {}
    scraper = cloudscraper.create_scraper(browser)
    # Creating a cloudscraper object so that will bypass any cloudscraper protection
    try:
        r = scraper.get(BASE_URL) ## base url
    except:
        raise ValueError("Fetching site error")

    try:
        soup = BS(r.text,"html.parser")
        # Use beutifulsoup to pasre the html data extract information data.
        header_courses = soup.find("h3",class_="post-title entry-title")
        for i,tag in enumerate(header_courses):
            course_list.insert(1,(tag.text,tag["href"]))
        courses = soup.find_all("h3",class_="post-title entry-title")
        for no,link in enumerate(courses):
            course_link = link.find("a")
            course_list.append((course_link.text,course_link["href"]))
    except error:
        print(error)
        
    for i,j in dict((course_list)).items():
        course_dict.setdefault(i,j)

    for name,urls in course_dict.items():
        r2 = scraper.get(urls)
        if r2.status_code == 200:
            soup2 = BS(r2.text,"html.parser")
            tags2 = soup2.find_all("a",string="ENROLL NOW")
            if len(tags2) == 1:
                udemy_url.append((current_date,name,tags2[0]["href"]))
            else:
                udemy_url.append((current_date,name,tags2[1]["href"]))

    return udemy_url


if os.path.exists("udemy.db"):
    
    for url in scrape():
        if database_handler.Check_avail(url[1]):
            continue
        else:
            database_handler.Insert_ONE(url)
else:
    database_handler.Create_database()
    for url in scrape():
        if database_handler.Check_avail(url[1]):
            continue
        else:
            database_handler.Insert_ONE(url)



Email_handler.email(Email_temp.format(database_handler.query_bydate(current_date)))






    


