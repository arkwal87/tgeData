import xml.etree.ElementTree as ET

filePath = "C:\\Users\\arkad\\OneDrive\\Dokumenty\\pyData\\curves\\"
my_xml = filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml"

myTree = ET.parse(my_xml)
myRoot= myTree.getroot()

for x in myRoot.iter("Point"):
    # print(type(x))
    # print(x[0].attrib.items())
    item = x.find("Qty")
    print(item.attrib.items())

# print(myRoot.tag)
# print(myRoot[9][0].tag)