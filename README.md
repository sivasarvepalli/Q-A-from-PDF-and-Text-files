<h1 align="center">
  Q&A from TEXT Files
</h1>


## DEMO video

[![Watch the video]([https://img.youtube.com/vi/](https://github.com/sivasarvepalli/Team-Kalki/assets/163630482/3bc70dda-ac4f-4694-91c9-fd5d2a5b6c48))]






### Project descripition
Q&A system from PDF and text files. The application provides a user-friendly interface using the Streamlit framework, allowing users to interact with the Q&A functionality seamlessly.The uploaded file is analysed and answers are povided for the asked quation from the file. 

In this we have 2 sections, one is pdf analyser using openai API Key and other is text documents analyser using an API Key from Hugging Face Transformers which is a pre-trained Q&A system.

(final · Streamlit - Brave 2024-03-17 01-07-41.zip](https://github.com/sivasarvepalli/Team-Kalki/files/14625062/final.Streamlit.-.Brave.2024-03-17.01-07-41.zip)

# Team Details 
Team Number - VH088
| Name    | Email           |
|---------|-----------------|
| S.Siva Kumar | sivasarvepalli4@gmail.com |
| P.Varun Tej | varuntej.p22@gmail.com |
| P.Jaya Vardhan | jayavardhan1810@gmail.com |
| M.karthik Reddy | mandapatikarthikreddy@gmail.com |

## Problem Statement
problem  : To study the whole pdf or text file is timne taking process. While it is good to resd the whole pdf and text files but it also consumes a lot of time when preparing for exams and when quick 
information is required it is hard to go through the whole document.

## About the Project

solution : By using this application, questions asked by the user will be answered from the pdf or the text file.  
we can simply say this is a student assistant.
Primary goal of this project is to assist the students for time efficient preparation.
This project mainly helps students to travers the pdf and text files in short time.
It uses openAI API KEY with which it reads the pdf files and answer the questions asked.
simple user interface.

## Technical implementation
- A pdf or Text file is taken as input.

- The text in the files is divided into fragments and anylsied.
  
- Then the user asks a quation & the model analysies the quation and finds the similer words from the Q and writes a Anawer.

<div style="display: flex; flex-wrap: wrap;">
   <img src="https://github.com/sivasarvepalli/Team-Kalki/assets/131340671/981b0387-d671-4a88-bc51-7749a7fe3e56" style="width: 30%; margin: 5px;">
    <img src="https://github.com/sivasarvepalli/Team-Kalki/assets/131340671/98def8d9-12eb-4d55-9dfa-7794922b1ae5" alt="Image 2" style="width: 30%; margin: 5px;">
    <img src="https://github.com/sivasarvepalli/Team-Kalki/assets/131340671/1fad1468-9f0c-4475-b476-73ce3269d349" alt="Image 3" style="width: 30%; margin: 5px;">
    
</div>


# Techstacks used

`streamlit` , `Hugging Face Transformers ` , `OpenAI API` , `Requests` , `CSS `
`os` , `importlib  `

# How to run locally
- step 1 : clone the repo
   `git clone https://github.com/sivasarvepalli/Team-Kalki`
- step 2 : run the commande 
  `cd Team-Kalki`
- step 3 : install the required packages
   `pip install -r requirements.txt`   
- step 4 : run this command to run the web application
   `streamlit run final.py`

# What's next
For the future plans we are trying to completly fuse both the section in this project without decresing the accuracy of the model and remove the need of openai API Key.

# Declaration
We confirm that the code presented here was either developed entirely during the development process or underwent significant updates within the development timeframe. We understand that any plagiarism from external sources would result in disqualification of our project, and our participation in the project will be revoked.
