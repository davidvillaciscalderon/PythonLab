file = open("example_page.html", "r")
file_content=file.read()
print file_content
print file_content[file_content.find("Blacksburg"):]
file.close()