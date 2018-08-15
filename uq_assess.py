### Main Scraper

from bs4 import BeautifulSoup
import requests
import lxml

assessment_url = 'https://www.courses.uq.edu.au/student_section_loader.php?section=5&profileId=87384#assessmentDetail'
assessment_page = requests.get(assessment_url).text
soup = BeautifulSoup(assessment_page, 'lxml')

assessment_table = soup.findAll('table')[6]
rows = assessment_table.findAll('tr')

def unwrap(content):
    try:
        next_contents = content.contents
        unwrapped_content = unwrap(next_contents)
        return unwrapped_content
    except AttributeError:
        print(content)
        return content

for i in range(1,len(rows)):
     for j in rows[i].findAll('div'):
         content = j.contents
         if len(content) > 1:
             for k in content:
                 print(unwrap(content))
         else:
             print(j.text)
        
             
            






