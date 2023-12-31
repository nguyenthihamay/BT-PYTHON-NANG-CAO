import xml.dom.minidom
def main():
    path ="e:/btap python nâng cao/chương 2/bai2.3.xml"
    doc = xml.dom.minidom.parse(path)
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    expertise= doc.getElementsByTagName("expertise")
    print("%d expertise: " %expertise.length)
    for skill in expertise :
        print(skill.getAttribute("name"))

if __name__=='__main__':
    main();
