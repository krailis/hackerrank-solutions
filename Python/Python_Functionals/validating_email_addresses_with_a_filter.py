#=====================================================================

import re

def fun(s):
    # return True if s is a valid email, else return False
    return bool(re.match(r"[a-z0-9_-]+@[a-z0-9]+\.[a-z]{1,3}$", s))

#=====================================================================

def filter_mail(emails):
    return filter(fun, emails)

if __name__ == '__main__':
    n = int(raw_input())
    emails = []
    for _ in range(n):
        emails.append(raw_input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print filtered_emails
