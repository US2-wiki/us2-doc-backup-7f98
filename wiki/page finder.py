with open('Full index.md', 'r') as rfp:
    content = rfp.read()
    index = 0
    while True:
        location = content.find('[[', index)
        if location == -1:
            break
        if content[location-1] == '!':
            attachment = True
        else:
            attachment = False
        end_bracket = content.find(']]', location)
        if not attachment:
            print(content[location+2:end_bracket])
        index = end_bracket
        
