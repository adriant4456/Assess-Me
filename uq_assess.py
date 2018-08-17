### Main Scraper

from bs4 import BeautifulSoup, Tag, ResultSet, NavigableString
import requests
import lxml

assessment_url = 'https://www.courses.uq.edu.au/student_section_loader.php?section=5&profileId=87384#assessmentDetail'
assessment_page = requests.get(assessment_url).text
soup = BeautifulSoup(assessment_page, 'lxml')

assessment_table = soup.findAll('table')[6]
rows = assessment_table.findAll('tr')

def unwrap(content, content_list):
    if len(content) > 1 and isinstance(content, Tag):
        iter_list = content.contents
        for j in iter_list:
            if len(unwrap(j, content_list)) > 1:
                for k in unwrap(j, content_list):
                    content_list.append(k)
                else:
                    content_list.append(unwrap(j, content_list))
        return content_list
    elif len(content) > 1 and isinstance(content, ResultSet):
        for i in content:
            print(unwrap(i, content_list))
            if len(unwrap(i, content_list)) > 1:
                for l in unwrap(i, content_list):
                    content_list.append(l)
                else:
                    content_list.append(unwrap(i, content_list))
        return content_list
    elif len(content) == 1 and isinstance(content, Tag):
        print(content.text)
        return content.text
    elif isinstance(content, NavigableString):
        print(str(content))
        return str(content)
            


"""
    try:
        next_contents = content.contents
        unwrapped_content = unwrap(next_contents)
        return unwrapped_content
    except AttributeError:
        return content
"""
for i in range(1,len(rows)):
     for j in rows[i].findAll('div'):
         content = j.contents
         if len(content) > 1:
             for k in content:
                 print(unwrap(k))
         else:
             print(j.text)
        
             
            






