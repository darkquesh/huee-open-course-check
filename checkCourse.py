import requests
from bs4 import BeautifulSoup

def openCourses():
	URL = 'http://www.ee.hacettepe.edu.tr/?link=300600&sublink=ugWeekly'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content,'html.parser')
	results = soup.find(id='mainPage')

	open_courses = results.find_all('a')

	a = []
	for course_elem in open_courses:
		course = course_elem.find('b')
		if course is not None:
			course = course.text.strip()[:6]
			a.append(course)
		else:
			continue
	return set(a)

def getCourses():
	URL = 'http://www.ee.hacettepe.edu.tr/?link=301000'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content,'html.parser')
	results = soup.find(id='mainPage')

	courses = results.find_all('td',width="10%")

	b = []
	for course_elem in courses:
		course = course_elem.find('a')
		if course is not None:
			course = course.text.strip()[:6]
			b.append(course)
		else:
			continue
	return set(b)

openCs = sorted(openCourses())
allCs = sorted(getCourses())

res = sorted(set(allCs).intersection(openCs))
resToStr = ' '.join(map(str,res))
print("Courses open this term:",resToStr)
