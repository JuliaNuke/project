import re

def email_parse(email):
    email_reg = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', re.IGNORECASE)
    match = email_reg.match(email)
    if match is None:
        raise ValueError("Wrong email address")

    domain = re.search('@.*', email).group()
    usr = re.search('^[a-z+]+@', email).group()
    return {'username': usr[:-1], 'domain': domain[1:]}

print(email_parse('qwe@ya.ru'))