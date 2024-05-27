name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "frank"
last_name = "alimimian"
full_name = first_name + " " + last_name
print(first_name.title() + " " + last_name.title())
print(f"{first_name.title()} {last_name.title()}")
print("Hello," + " "+ full_name.title())

#Using \n and \t for newline and tab
print("Programming languages:\n\tJavascript\n\tPython\n\tRuby\n\tJava\n\tC++\n\tC\n\tPHP")

#Striping whitespace from inputs using rstrip(),lstrip() and strip()
favorite_language = " python "
print(favorite_language.lstrip().rstrip())

#Exercise
name = "Favour"
message = "Hello "+  name +", would you like to learn some python today?"
print(message)

first_person = "johnny drille"
print(first_person.title())
print(first_person.lower())
print(first_person.upper())

famous_quote = 'Jesus once said, "Blessed are the poor in spirit, theirs is the kingdom of God"'
print(famous_quote) 

famous_person = "Abraham Lincoln"
quote = '"How you do something is how you do anything"'
print(famous_person + ' once said: ' + quote)
