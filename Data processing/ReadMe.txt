1. Link: https://bulkdata.uspto.gov/
2. Go to  Patent Grant Full Text Data with Embedded TIFF Images (JAN 2001 - PRESENT) (Grant Red Book based on WIPO ST.36).
3. The files are in .tar format. Apply extract_tar.py to extract the tar files
4. Apply folder_organize.py to delete all the folders except DESIGN 
5. Apply unzip.py unzip the folders and save it to the yearwise folder. Example 
I20220104.tar
↳I20220104 + I20220104-SUPP
    ↳I20220104
       ↳DESIGN+ ….+....+....
        ↳USD0939806-20220104.zip
    ↳USD0939806-20220104-D00001.TIF+USD0939806-20220104.XML
     6. Apply process_xml.py to process all the xml files