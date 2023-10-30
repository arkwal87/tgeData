import pandas as pd
import xml.etree.ElementTree as et
import lxml
import xml.dom.minidom

filePath = "C:\\Users\\arkad\\OneDrive\\Dokumenty\\pyData\\curves\\"

# print(filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml")
my_xml = filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml"

domtree = xml.dom.minidom.parse(my_xml)

group = domtree.documentElement

test = group.getElementsByTagName("PriceAmount")
# print(type(test))
# print(test.getElementsByTagName(""))
# print(test[0])
# test2 = test.getElementByTagName("Pos")
# print(test)
# #
for item in test:
    # print(item.firstChild.nodeName)
    # print(item.firstChild.attributes.items())
    # print(item.firstChild.nextSibling.firstChild.nextSibling.attributes.items())

    # print(item.parentNode.parentNode.parentNode.parentNode.nodeName)
    print(item.attributes.items())


    # print(type(item))


# #my_ds = pd.read_xml(filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml")
# #
# # print(my_ds)
#
# def intr_docs(xml_doc):
#     attr = xml_doc.attrib
#     for xml in xml_doc.iter("document"):
#         doc_dict = attr.copy()
#         doc_dict.update(xml.attrib)
#         doc_dict["data"] = xml.text
#
#         yield doc_dict
#
# etree = et.parse(filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml")
# doc_df = pd.DataFrame(list(intr_docs(etree.getroot())))
#
# # print(doc_df.iloc[0, :])
# print(doc_df)

# my_xml = filePath + "AggregatedOrdersPlFilteredForDeliveryDate_2023-05-29.xml"
#
# df = pd.read_xml(my_xml)
#
# print(df)