import xml.etree.ElementTree as ET
import arcpy

xmlfile = 'D:/Working/Test/xml_test.xml'
element_tree = ET.parse(xmlfile)
root = element_tree.getroot()
agreement = root.findall(".//TCASE")
result = []
elements = ('LOG', 'DATE','VERDICT')

for a in agreement:
    obj = {}
    for e in elements:
        obj[e] = a.find(e).text
    result.append(obj)

arcpy.AddMessage(result)



#######################################################



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