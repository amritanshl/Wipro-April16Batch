import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
# xml_data = """<bookstore>...</bookstore>"""
root = tree.getroot()
#root = ET.fromstring(xml_data)

for item in root.findall('book'):
    title = item.find('title').text
    category = item.get('category')
    print(f"Book {title} | Category {category}")

root = ET.Element("college")

student1 = ET.SubElement(root, "student", id="111")
ET.SubElement(student1, "name").text ="Amritansh Lal"
ET.SubElement(student1, "major").text ="Computers"
ET.SubElement(student1, "gpa").text ="3.9"

student2 = ET.SubElement(root, "student", id="222")
ET.SubElement(student2, "name").text ="Aravind kumar"
ET.SubElement(student2, "major").text ="Accounts"
ET.SubElement(student2, "gpa").text ="2.8"

tree = ET.ElementTree(root)

with open("new_sample.xml", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)


