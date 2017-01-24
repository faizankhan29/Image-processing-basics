import xml.etree.ElementTree
from xml.dom import minidom
xmldoc = minidom.parse('10.1.1.1.2004_4.xml')
print(xmldoc)
itemlist = xmldoc.getElementsByTagName('Char')
print(len(itemlist))
print(itemlist[0].attributes['Text'].value)
for s in itemlist:
    print(s.attributes['Text'].value)
