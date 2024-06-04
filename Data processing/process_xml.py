import xml.etree.ElementTree as ET
import glob
import os
import csv
import pandas as pd

path = '/Downloads/Dataset/2015' 
pattern = '**/*.XML'
xml_files = glob.glob(os.path.join(path, pattern), recursive=True)
with open('/Downloads/Dataset/2015/processed_xml_2015.csv', mode='w', newline='') as csv_file:
    fieldnames = ['title', 'id', 'claim', 'date', 'class', 'class_search', 'inv_country', 'no_figs', 'sheets', 'file_names', 'fig_desc']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for file in xml_files:
            tree = ET.parse(file)
            root = tree.getroot()
            
            # Extract the data from each XML file as before
            patent_title = root.find('.//invention-title').text
            patent_id = root.find('.//doc-number').text
            claim = root.find('.//claim-text').text
            class_USPC = root.find('.//classification-national/main-classification').text
            class_USPC_fur = root.find('.//classification-national/further-classification')
            search = root.findall('.//main-classification')
            sheets = root.find('.//number-of-drawing-sheets').text
            search_list = [elem.text for elem in search]
            date = root.find('.//date').text
            no_figs = root.find('.//number-of-figures').text
            print("Patent ID:", patent_id)
            countries = ','.join([c.find('.//country').text for c in root.findall('.//inventor') if c.find('.//country') is not None])
            #countries = ','.join([c.find('.//country').text for c in root.findall('.//inventor')])

            
            file_names = [img.get('file') for img in root.findall('.//img')]

            fig_list = []
            count = 0
            for p in root.iter('p'):
                if count < int(no_figs):
                    texts = list(p.itertext())
                    element = ' '.join(text.strip() for text in texts)
                    fig_list.append(element)
                    count += 1

            # Write the extracted data to the CSV file
            writer.writerow({
                'title': patent_title,
                'id': patent_id,
                'claim': claim,
                'date': date,
                'class': class_USPC + ',' + class_USPC_fur.text if class_USPC_fur is not None else class_USPC,
                'class_search': search_list,
                'inv_country': countries,
                'no_figs': no_figs,
                'sheets': sheets,
                'file_names': file_names,
                'fig_desc': fig_list
            })



