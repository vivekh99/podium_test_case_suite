Podium Challenge
=======================================
This classifier, written in Python, will search the first 5 pages of a dealership on dealerrater.com and return the first 3 reviews that the classifier determines to be overly positive based on the metrics defined below

Metrics to define positivity:
    Positive reviews were determined by 
        Is the dealer recommended in the review (this simulates the star rating given on the review)?
        Do the words in the review match a pre-selected list of words that are used to express positivity?
        What are the number of exclamation marks used in the review?
        Are there capital letters used (that are not the first character of a word)?

External Libraries used:
    BeautifulSoup4 (bs4)
    csv
    requests
    string

How to execute:
    -This code can be executed in your machine's terminal by running 
        `python3 podium_challenge.py`
    -However, before running, make sure to have installed the bs4 library using
        `pip3 install beautifulsoup4`
    -pip is a command used to install python libraries

    -If you want to run this code directly in VS Code, you will need to download openSSL which can be found here https://slproweb.com/products/Win32OpenSSL.html, in addition to the download of the bs4 library.

Test Cases:
    -These test cases were ran by using real data off of dealerrater.com. The dealers used were:
        "https://www.dealerrater.com/dealer/Cueter-Chrysler-Jeep-Dodge-review-22324/page" + str(page) + "/?filter=ALL_REVIEWS"

        "https://www.dealerrater.com/dealer/Mike-Riehl-s-Roseville-Chrysler-Dodge-Jeep-Ram-review-27075/page" + str(page) + "/?filter=ALL_REVIEWS"

        "https://www.dealerrater.com/dealer/Fox-Hills-Chrysler-Jeep-review-106467/page" + str(page) + "/?filter=ALL_REVIEWS"

        "https://www.dealerrater.com/dealer/Gene-Butman-Ford-review-18132/" + str(page) + "/?filter=ALL_REVIEWS"

        copy-paste the exact lines above (including the quotations) and paste in between the parenthesis of the `.get()` method located on line 25

    -These were personally made test cases
        IMPORTANT
        "https://vivekh99.github.io/podium_test_case_suite/index.html"

