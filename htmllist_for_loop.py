items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for i in range(len(items)):
	if(i == 0 ):
		print(html_str)
		
	print("<li> {} <li>".format(items[i]))
	


print(html_str)