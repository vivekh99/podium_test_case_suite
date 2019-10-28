# podium_test_case_suite

Podium Challenge
================================
This classifier, written in Python, will search the first 5 pages of a dealership on dealerrater.com and return the first 3 reviews that the classifier determines to be overly positive based on the metrics defined below

Metrics to define positivity:
=============================
    Positive reviews were determined by 
        Is the dealer recommended in the review (this simulates the star rating given on the review)?
        Do the words in the review match a pre-selected list of words
        that are used to express positivity?
        What are the number of exclamation marks used in the review?
        Are there capital letters used (that are not the first character of a word)?

External Libraries used:
==========================
    BeautifulSoup4 (bs4)
    requests
    string

How to execute:
========================
This code can be executed in your machine's terminal by running 
`python3 podium_challenge.py`
However, before running, make sure to have installed the bs4 library using
`pip3 install beautifulsoup4`
pip is a command used to install python libraries

-If you want to run this code directly in VS Code, you will need to download
openSSL which can be found here https://slproweb.com/products/Win32OpenSSL.html,
in addition to the download of the bs4 library.

Test Cases:
===================
-These test cases were ran by using real data off of dealerrater.com.
copy-paste the exact lines below (including the quotations) and paste in between
the parenthesis of the `.get()` method located on line 25

"https://www.dealerrater.com/dealer/Cueter-Chrysler-Jeep-Dodge-review-22324/page" + str(page) + "/?filter=ALL_REVIEWS"

"https://www.dealerrater.com/dealer/Mike-Riehl-s-Roseville-Chrysler-Dodge-Jeep-Ram-review-27075/page" + str(page) + "/?filter=ALL_REVIEWS"

"https://www.dealerrater.com/dealer/Fox-Hills-Chrysler-Jeep-review-106467/page" + str(page) + "/?filter=ALL_REVIEWS"

"https://www.dealerrater.com/dealer/Gene-Butman-Ford-review-18132/" + str(page) + "/?filter=ALL_REVIEWS"


Personal Test Cases:
===============================
-These were personally made test cases and can be found in this repo. Please look at source code for them for comments
IMPORTANT - to run these test cases, you must change the range of the for loop in line 21
from `for page in range(1, 6):` to `for page in range(1, 2):`

You must also copy the exact lines (test cases) below (including the quotations) and 
paste them in between
the parenthesis of the `.get()` method located on line 25.
You should paste one test (one line) in, run the file, then paste the next test (replacing the one you had pasted in previously) and run the script to run each test file.
The test files website can be found at https://vivekh99.github.io/podium_test_case_suite/. Correct output for the test files can be found there as well.

"https://vivekh99.github.io/podium_test_case_suite/index.html"

"https://vivekh99.github.io/podium_test_case_suite/exclamation_in_header.html"

"https://vivekh99.github.io/podium_test_case_suite/capitals.html"

"https://vivekh99.github.io/podium_test_case_suite/preset_words.html"

"https://vivekh99.github.io/podium_test_case_suite/edgecases.html"

