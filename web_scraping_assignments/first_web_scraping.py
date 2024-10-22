from bs4 import BeautifulSoup
soup = BeautifulSoup(open("top_100_ebooks.html"), features="html.parser")

#print(soup.prettify())
tag = soup.find('h2')
#print(tag)
list = tag.find_next("ol")
print(list)
#for title in list:
	#print(title.get_text())