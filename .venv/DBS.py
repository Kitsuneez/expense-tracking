import re
def DBS(raw_file_content):
    this_month = 0
    {
        
    }
    iterations = [x.group() for x in re.finditer(r'[0-9]{2} (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec) .*SG [0-9]{2} (JAN|FEB|MAR|APR|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\n(REF NO.*\$) [0-9]+.[0-9]{2}', raw_file_content)]
    for i in iterations:
        values = re.findall(r'([0-9]{2} (?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)) (.*)SINGAPORE.*SG ([0-9]{2} (?:JAN|FEB|MAR|APR|JUN|JUL|AUG|SEP|OCT|NOV|DEC))\nREF NO.*\$ ([0-9]+.[0-9]{2})', i)
        #should have 4 indexes
            # date charged
            # name
            # date visited
            # price
        out = []
        for value in values:
            for item in value:
                out.append(item.rstrip())
        print(out)