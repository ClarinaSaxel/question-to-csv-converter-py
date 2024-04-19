# question-to-csv-converter-py
greekdoctor has already provided a java script snippet to get questions from the website finalexam.hu in a text file [here](https://github.com/greekdoctor/finalexam-questioncollector-js/tree/main). I am now changing that format to a csv file so it can be used for [brainyoo flashcards](https://brainyoo.de/dokumentation/karteikarten-der-desktop-client-fuer-win-mac/108777-2/).

# usage
1. Have all the textfiles in .txt format in one folder and copy the path to the folder
2. Save the python file and run it in the editor of your choice (I used Microsoft's Visual Studio Code)
3. You will be prompted to give the path as input or press enter if the files are in the same folder as your python file
4. This will create a csv file for every textfile in the specified folder or crash if the textformat does not fit the one of the questions
5. Reruns will overwrite the previous csv files
