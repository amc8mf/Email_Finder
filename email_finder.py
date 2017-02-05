#Alex_Colegrove CS1111, Fall 2016

import urllib.request
import re

def find_emails_in_website(url):

    stream = urllib.request.urlopen(url)
    emails = []
    regex = re.compile(r"[\w\d\.\-]+@[\w\d\.\-]+\.[a-zA-Z]{2,}")
    Results = []
    for line in stream:

        decoded = line.decode("UTF-8")
        replaced = re.sub('[^\w\d\.\-]+((@)|(at)|(AT)|(aT)|(At))[^\w\d\.\-]+', '@', decoded)
        if '"' in replaced:
            replaced.replace('"',' ')
        replaced = replaced.split()



        for i in range(len(replaced)):
            results = regex.findall(replaced[i])
            for result in results:
                result = result.replace("NOSPAM", "")
                if result not in emails:
                    emails.append(result)


    return emails






#replaced = re.sub('[^\w\d\.-]+((.)|(dot)|(doT)|(dOt)|(dOT)|(Dot)|(DoT)|(DOt)|(DOT))[^\w\d\.-]+', '.', replaced)