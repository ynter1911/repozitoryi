from lxml import etree

xml_file = 'example.xml'
xsd_file = 'example.xsd'

xml_doc = etree.parse(xml_file)
with open(xsd_file, 'rb') as f:
    schema_doc = etree.XML(f.read())

schema = etree.XMLSchema(schema_doc)

if schema.validate(xml_doc):
    print("Успех")
else:
    print("Ошибка")
    print(schema.error_log)