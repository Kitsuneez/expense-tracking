import re
import datetime
import json
def DBS(raw_file_content):
    with open('category.json', 'r') as file:
        category_lib = json.load(file)
    month_grouping = {
        "month":"",
        "total":0,
        "breakdown": {
            "Food & Beverages":0.00,
            "Education":0.00,
            "Health & Wellness":0.00,
            "Entertainment":0.00,
            "Transportation":0.00,
            "Shopping":0.00,
            "MISC":0.00,
            "Groceries":0.00,
            "Unknown":0.00
        }
    }
    items = []
    iterations = [x.group() for x in re.finditer(r'[0-9]{2} (Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec) .*SG [0-9]{2} (JAN|FEB|MAR|APR|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\n(REF NO.*\$) [0-9]+.[0-9]{2}', raw_file_content)]
    for i in iterations:
        values = re.findall(r'([0-9]{2} (?:Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)) (.*)SINGAPORE.*SG ([0-9]{2} (?:JAN|FEB|MAR|APR|JUN|JUL|AUG|SEP|OCT|NOV|DEC))\nREF NO.*\$ ([0-9]+.[0-9]{2})', i)
        #should have 4 indexes
            # date charged, not important
            # name
            # date visited
            # price
        output = []
        for value in values:
            for item in value:
                output.append(item.rstrip())
        item = {
            "name": output[1],
            "date": output[2],
            "price": output[3],
            "month": datetime.datetime.strptime(output[2], "%d %b").month
        }
        items.append(item)
    food = 0
    for item in items:
        for key,value in category_lib.items():
            if item.get("name") in value:
                #item is in category list already
                month_grouping["breakdown"][key] = round(month_grouping["breakdown"][key] + float(item.get("price")),2)
                month_grouping["total"] = round(month_grouping["total"]+float(item.get("price")),2)
                break
        # need to add into lib
        month_grouping["breakdown"]["Unknown"] += float(item.get("price"))
        month_grouping["total"] += float(item.get("price"))
    print(month_grouping)
