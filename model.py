
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:05:00 2020

@author: CN261
"""
# Resume Phrase Matcher code


#importing all required libraries

import os
from functions import pdfextract, create_profile, requirement_match
from datetime import datetime
    
#Function to read resumes from the folder one by one
main_dir = os.getcwd()
data_dir = os.path.join(main_dir,'data')
resume_list = os.listdir(data_dir)

# Validation Check
candidate_name = []
pagecount = []
time_taken = []
Match_details = []
for i in range(len(resume_list)):
    if pdfextract(os.path.join(data_dir,resume_list[i]))['corpus'] == ['']:
        a = datetime.now()
        page_count = pdfextract(os.path.join(data_dir,resume_list[i]))['page_count']
        candidate_name.append(resume_list[i].split('_')[0])
        Match_details.append('No Information found due to image format conversion to pdf')
        pagecount.append(page_count)
        b=datetime.now()
        time_taken.append((b-a))

    else:
        a = datetime.now()
        page_count = pdfextract(os.path.join(data_dir,resume_list[i]))['page_count']
        output = requirement_match(create_profile(os.path.join(data_dir,resume_list[i]),main_dir))
        b=datetime.now()
        time_taken.append((b-a))
        candidate_name.append(resume_list[i].split('_')[0])
        pagecount.append(page_count)
        Match_details.append(output)



meta_data = {'candidate_name': candidate_name,
             'page_count': page_count,
             'time_taken': time_taken,
             'Resume_Match_Details': Match_details
             }        


print(meta_data)