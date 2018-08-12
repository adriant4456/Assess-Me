### Main Scraper

from bs4 import BeautifulSoup
import requests
import lxml

assessment_url = 'https://www.courses.uq.edu.au/student_section_loader.php?section=5&profileId=87384#assessmentDetail'
assessment_page = requests.get(assessment_url).text
soup = BeautifulSoup(assessment_page, 'lxml')

assessment_table = soup.findAll('table')[6]
rows = assessment_table.findAll('tr')
for i in range(1,len(rows)):
    for i in rows[i].findAll('div'):
        if '<i>' in i.contents:
            
    




