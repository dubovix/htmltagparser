from bs4 import BeautifulSoup, Tag
file = open("test.html", "r")
index = file.read()
#print(file.read())
soup = BeautifulSoup(index, "lxml")
#page_h1 = soup.findAll("h1")
#print(page_h1)
all_tags = ([tag.name for tag in soup.find_all()])
print(all_tags)
for item in all_tags:
    item_tag_name = item.get(all_tags)

#print([str(tag) for tag in soup.find_all()])
