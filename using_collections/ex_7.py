# Write Python code to replace all the : characters in the string below with +.
# Try this problem using the methods you've learned about in this chapter.
# Once you have that working, use the Python documentation for the str type to find an alternative solution

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

part = info.split(':')
result = '+' .join(part)
print(result)

updated_info = info.replace(':', '+')

print(updated_info)