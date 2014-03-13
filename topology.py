from xml.etree.ElementTree import *

def load_tree(file):
    tree = ElementTree()
    tree.parse(file)
    root = tree.getroot()
    return [tree, root]

def readNodes(file):
    
    [tree, root] = load_tree(file)

    for ro in root.iter('node'):
        print ('Routers ID '+ro.get('id'))
        for details in ro.iter('interfaces'):
            for details in ro.iter('interface'):
                print('Inteface ID ' + str(details.get('id')))
        for details in ro.iter('powerprofileid'):
            print('Power profile ID '+str(details.get('id')))
        for details in ro.iter('nodestatus'):
            print('Status '+ str(details.get('status')))
        for details in ro.iter('powerprofilesleepid'):
            print('Power profile sleep ID '+str(details.get('id')))
        for details in ro.iter('loadmax'):
            print('load max '+str(details.get('load')))
        for details in ro.iter('loadcurrent'):
            print('load current '+str(details.get('load')))
        print '\n'
    return

def readLinks(file):

    [tree,root] = load_tree(file)
    for details in root.iter('link'):
        print('Link id ' + str(details.get('id')))
        for details in root.iter('from'):
            print('From ' + str(details.get('node')) + ' if '+str(details.get('if')))
        for details in root.iter('to'):
            print('To ' + str(details.get('node')))
        for details in root.iter('bw'):
            print('Bandwidth '+str(details.attrib))
        for details in root.iter('delay'):
            print('Delay '+str(details.get('delay')))
        print '\n'
    return




file = 'Topology.xml'
readNodes(file)
readLinks(file)






    
    
    





    





            
      
