import xml.dom.minidom
def main():
 doc = xml.dom.minidom.parse("e:/btap python nâng cao/chương 2/bai2.3.xml");
 print(doc.nodeName)
 print(doc.firstChild.tagName)
 expertise = doc.getElementsByTagName("expertise")
 print("%d expertise:" % expertise.length)
 for skill in expertise:
   print(skill.getAttribute("name"))
 newexpertise = doc.createElement("expertise")
 newexpertise.setAttribute("name", "AI")
 doc.firstChild.appendChild(newexpertise)
 print(" ")
 expertise = doc.getElementsByTagName("expertise")
 print("%d expertise:" % expertise.length)
 for skill in expertise:
   print(skill.getAttribute("name"))

if __name__=="__main__":
 main();