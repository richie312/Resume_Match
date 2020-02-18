

# Resume Match | ML Prediction, whether a selected will be hired or not 
Resume Match Platform provides the reviewers and recruiters to decide the strategy
to select a resume from huge pool of resume database in order to automate the cumbersome process.
This platform also predicts the possibility of selected resume for the final selection based on
the historical records. (which consider the keywords for domain, page count of the resume, percentage of
keywords match with the key_skill requirment and count of keywords from matches with the expected_threshold for specific domain.)

Finally this application will be integrated with https://github.com/richie312/Email_Django_App which will be another application/feature of the Resume Builder Application (Based on Django).

A chatbot (rasa core trained) will also be integrated with the Resume Builder Application.



## Steps to formulate the model 

1. Create the Expectation Threshold Matrix, which contains the minimum number of count
	and key skill for each domain. **Done** (&#x1F4D7;)

2. Make the function pdfextract, create_profile and requirement match. Documentationis 
available in doc string which can be accessed by inspect.getdoc(<<function_name>>) **Done**(&#x1F4D7;)
    
3. Apply it on multiple resume and collect the data in following field: **In Progress**(&#x1F4D9;)
	- Match Details
	- Page Count
	- Keywords used in Resume for each Domain
	- candidate name
	- time taken 

4. Database Setup and Insertion of the details:**In Progress**(&#x1F4D9;)
	
5. Get the actual hiring decision made on the Resume (Hired: 1| Not Hired: 0)**In Progress**(&#x1F4D9;)

