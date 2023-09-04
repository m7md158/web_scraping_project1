# import the Library
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

# list of the values
job_title = []
company_name = []
location_name = []
job_skill = []
date = []
page_num = 0




while True:

    # use request to fetch the url
    result = requests.get(f"https://wuzzuf.net/search/jobs/?q=python&start={page_num}")

    # Save page content
    src = result.content

    # Create soup object to parse conten
    soup = BeautifulSoup(src, 'lxml')
    page_limit = int(soup.find("strong").text)
    
    if (page_num > page_limit // 15):
        print("page ended")
        break



    # find the element containing info we need 
    #-- job title, job skills, company names, location names

    job_titles = soup.find_all("h2", {"class":"css-m604qf"})
    company_names = soup.find_all("a",{"class":"css-17s97q8"})
    location_names = soup.find_all("span", {"class":"css-5wys0k"})
    job_skills = soup.find_all("div", {"class": "css-y4udm8"})
    posted_new = soup.find_all("div",{"class":"css-4c4ojb"})
    posted_old = soup.find_all("div",{"class":"css-do6t5g"})
    posted = [*posted_new, *posted_old]





    # Loop over returned lists to extract needed info into other lists
    for i in range(len(job_titles)):
        job_title.append(job_titles[i].text)
        company_name.append(company_names[i].text)
        location_name.append(location_names[i].text)
        job_skill.append(job_skills[i].text)
        date.append(posted[i].text)
    page_num += 1
    print("Page Switched")






# unpacking for the data
file_list = [job_title, company_name, date, location_name, job_title]
exported = zip_longest(*file_list)

# Create csv file and fill it with values
with open("D:\course\web_scraping\python_project\job_sets.csv","w", encoding="utf-8") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['Job Title','Company Name','Date', 'Location Name','Job Skill', 'Link'])   # write title of dataset
    wr.writerows(exported)

