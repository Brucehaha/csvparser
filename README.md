# Data Engineering Coding Challenges


## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec.
- Implement a parser that can parse the fixed width file and generate a csv file. 
- DO NOT use pre built python libraries like pandas for parsing. You can use a library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

## Project Directory

### bin:
-  run.py: port to run the whole program, csv parser code is located in src file
### config:
-  settings.py: contain all the environment variables, such as BASEDIR, location of log file, spec.json file, and input and output file
### files:
- input and outputfolder: input is the location of the file waiting for parsing, output is the result folder.
### fixed-width: 
-  spec.json: this folder contains the requirements for output file.
### lib
storing customized function or class
-  log.py: customized loging class base on logging package
### log
-  storing the log file
### src
core code to parse file
-  csvparser.py: contains code to parse the file to required csv file
-  scripts.py: interface to run csvparser.py by bin/run.py
### test
-  contains all the test file for this program, will automatically run with 'docker-compose up'

### how to run this program
- put your files input file in to 'files/input' to replace the sample file win.txt(windows-1252), or customize you own location in 'config/settings.py'
- in the shell, exec 'docker-compose up', it will automatically run the test file and 'bin/run.py' file.
- if you want change the spec.json, just put the new one in 'fixed-with' and change the name in config/settings.py  SPEC_FILE variable
- find all the result files in 'files/output'.
- if files are not found. Please check the run.log in 'log' folder.
- any error, you may find in log folder as well.

### Further Improvement
- This project is just a broker to parse file on backend.
- This project does not specify the automatic way to input a file, like using a user interface(GUI), Web form upload and download interface, or pass parameters by sys.argv
- This broker program will be easily coupled with GUI or Web application.
- By default, the input encoding is 'windows-1252', this program could be improved by using package 'chardet' to get the confident level of encoding type.
- If you failed to parse a file or get an error in log, try replace 'OPEN_ERROR="strict' to 'OPEN_ERROR="replace' in 'config/settings.py instead
- This program is not for very large file, could be improved by adding reading with specific chunk size, and writing to several splited files from one input file
- could be improved the parsing speed by multi-processing or multi-threading, although python's GIL is a pain for multi-core processing.

 

