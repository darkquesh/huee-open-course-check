import requests
from bs4 import BeautifulSoup

def openCourses():
	URL = 'http://www.ee.hacettepe.edu.tr/?link=300600&sublink=ugWeekly&lang=e'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id = 'mainPage')

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
	URL = 'http://www.ee.hacettepe.edu.tr/?link=301000&lang=e'
	page = requests.get(URL)

	soup = BeautifulSoup(page.content,'html.parser')
	results = soup.find(id = 'mainPage')

	courses = results.find_all('td', width="10%")
	#course_name = results.find_all('td', width="10%")

	b = []
	for course_elem in courses:
		course = course_elem.find('a')
		if course is not None:
			course = course.text.strip()[:6]
			b.append(course)
		else:
			continue
	return set(b)

def displayCourses():
	openCs = sorted(openCourses())
	allCs = sorted(getCourses())

	res = sorted(set(allCs).intersection(openCs))
	resToStr = '\n'.join(map(str,res))
	
	print("Open courses this term:\n", end='')
	print(resToStr)

if __name__ == '__main__':
	displayCourses()


#print("openCs: ",openCs)
#print("\n\nallCs: ",allCs)



'''for course in courses:
	print(course.text.strip())'''

#print(page.text)
