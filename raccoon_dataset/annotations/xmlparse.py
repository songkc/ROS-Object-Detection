import os
import xml.etree.ElementTree as ET

def modifyFileExtension(file):
    tree = ET.parse(file)
    root = tree.getroot()

    text = root.find("filename").text
    text = text.replace('.png', '.jpg', 1)
    # print(text)
    root.find('filename').text = text

    text = root.find("path").text
    text = text.replace('.png', '.jpg', 1)
    text = text.replace('/Users/datitran/Desktop/raccoon/', 
                        '/home/songkc/catkin_ws/src/rosproject/raccoon_dataset/', 1)
    # print(text)
    root.find('path').text = text

    tree.write(file)

if __name__=='__main__':
    # modifyFileExtension('raccoon-1.xml')

    filelists = os.listdir('../annotations')
    for file in filelists:
        if file.endswith('.xml'):
            # print(path)
            modifyFileExtension(file)
