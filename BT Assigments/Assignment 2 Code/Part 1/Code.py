import xml.etree.ElementTree as ET
import pandas as pd  

cols = ["LOG", "DATE", "VERDICT"]
rows = []

tree = ET.parse('./XML.xml')
root = tree.getroot()
for elem in root:
        name = elem.find("LOG").text
        date = elem.find("DATE").text
        status = elem.find("VERDICT").text
            
        rows.append({"name": name, 
                  "date": date,
                  "status": status})

df = pd.DataFrame(rows, columns = cols) 
df.to_csv('./xml_test.csv')
