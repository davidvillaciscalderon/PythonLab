text="Hello world"

print text[::-1]
print text[::2]

index_found=text.find("world")
print index_found
print text[:index_found]

print text.replace("world","wall")

