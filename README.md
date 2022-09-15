
# Automated dataset creation for Spanish vocabulary Flash Cards with Python.

Use a [RAE API](https://pypi.org/project/pyrae/) to create several Spanish Words Flash Cards data.
This automation take a .txt as input file. Returns both .json and .csv 
files.
The data includes two categories:

* question: Spanish Word 
* answer: Word etymology, class, definition and examples. 

Definition and class are guaranteed for each word in RAE dictionary.
   

  




## Installation

1. [Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) 
   to your local device. 
2. Navigate to the main project folder in terminal.   
3. [Create](https://stackoverflow.com/questions/48787250/set-up-virtualenv-using-a-requirements-txt-generated-by-conda) 
   virtualenv  using `requirements.txt`
   
```cmd
# Using pip
pip install -r requirements.txt

# Using conda
conda create --name <env_name> --file requirements.txt
```
    
## How to use

Codes are located inside `./code/` and some variables inside refers to files located
in `./Vocabulary/ESP/`.

Avoid to rename files. 

To create your own Spanish Flash Cards data:

1. Navigate to `./Vocabulary/ESP/` folder and edit `vocabulario_esp.txt` with your own word. 
   Make sure to insert 1 word per line:

        word1,
        word2,
        word3,
        word4,

 It's ok to include `,` character at the end of each word.  
 Avoid to use any other punctuation i.e. (`.`, `:`, `;`, `etc`).
 
 `UTF-8` encoding is used to take over the common accentuation
 at spanish words.

2. Execute `main.py` to get the `flash_cards_esp.json` file stored on
   `Vocabulary/Esp/`. To do this, navigate to the main 
   project folder in terminal and type:

       conda activate <env_name> 
       cd code 
       python main.py

   You'll see the code workflow in terminal... something like this:

        2022-09-14 11:08:37,339 - INFO    - dle.search_by_url - Performing request to: 'https://dle.rae.es/connivencia'...
        2022-09-14 11:08:38,002 - INFO    - dle.search_by_url - Performing request to: 'https://dle.rae.es/aunar'...
        2022-09-14 11:08:38,746 - INFO    - dle.search_by_url - Performing request to: 'https://dle.rae.es/vivisecciones'...    

3. At this point you can execute `create_csv.py` which uses the json data created
   before to create `flash_cards_esp.csv` file into `Vocabulary/Esp/` folder.
	
        python create_csv.py
   
4. You can use the created data to import several Flash Cards in apps.

   Some options:


   &nbsp;If you are an IOS user, 
   you can install [this free app](https://apps.apple.com/cl/app/flash-cards/id1454664875?l=en&fbclid=IwAR0fd_d8gPQNVyOSXNUBvjEbL3p6L2r584AeiDAONxe6I3zfd7P9b9SrxMA) 
   that allows import cards from json formatted data: Copy text inside `flash_cards_esp.json` and paste to the import box. 

   &nbsp;In online Apps like [this one](https://www.cram.com/flashcards/create) you can use the csv formatted data.
   Open the `flash_cards_esp.csv` in raw mode (it should look like &nbsp;[this](https://raw.githubusercontent.com/Nicolamunozi/FC_SV_txt/main/Vocabulary/Esp/flash_cards_esp.csv)).
   Copy the raw text and paste it to the `COPY AND PASTE YOUR DATA` section. Then, select `COMMA` option for `BETWEEN TERM AND`&nbsp; `DEFINITION` and `CUSTOM` in `BETWEEN DEFINITION AND CARD` 
   and fill the box with `."\n`. Finally, create flash cards. IMPORTANT: Make &nbsp;sure that hint side is hide. 

   &nbsp;In this [another option](https://www.goconqr.com/) you can directly import flash cards uploading the CSV file. 





        

 








## Authors

- [@Nicolás Muñoz](https://www.github.com/Nicolamunozi)


## Feedback

If you have any feedback, please reach out me at nicolamunozi@gmail.com

