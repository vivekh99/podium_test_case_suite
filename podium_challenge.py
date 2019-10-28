
import requests
import bs4
import string

#pre-selected words that denote positive connotation, list is not exhaustive
positive_words = ["happy", "good", "amazing", "well", "attentive", "recommend", "help", "helped",
					"helpful", "like", "liked", "professional", "easy", "kind", "excellent", "best", 
					"great", "thank you", "thankful", "quick", "fast", "courteous", "pleasure", "fun", "enjoyable", 
					"receptive", "friendly", "satisfied",  "appreciate", "responsive", "trustworthy", 
					"awesome", "outstanding", "genuine", "pleased", "thorough", "knowledgeable", "accomadating", "positive", "impressed"]
all_reviews_dict = {};

#set all values for the keys in the review to zero, avoiding KeyErrors later on
for all_reviews in range(0, 50):
	all_reviews_dict[all_reviews] = all_reviews_dict.get(all_reviews, 0); 
#total review counter
num_of_total_reviews = 0;
#loops through 5 pages of the dealer's reviews, adding the review and associatined positive connotation value to the dictionary all_reviews_dict
#change range below for personal test cases
for page in range(1, 6):
		
	#copy-paste test cases from the README here within the parenthesis of .get(PASTE TEXT HERE)
	#will get data from each page we intend to scrape
	website = requests.get("https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page" + str(page) + "/?filter=ALL_REVIEWS");
	#parses html from website and sotres it in site_html
	site_html = bs4.BeautifulSoup(website.text, 'html.parser');
	#returns a list of elements that contain dealer recommendation "yes or "no" (len == 10)
	recommend_dealer_init = site_html.find_all("div", class_="td small-text boldest")

	#returns a list of the content that was in the review for each review (len == 10)
	review_text_init = site_html.find_all("p", class_="font-16 review-content margin-bottom-none line-height-25")
	#initial header of the review
	review_header_init = site_html.find_all("h3", class_="no-format inline italic-bolder font-20 dark-grey")

	#strip tags and new lines from text and append to new list
	recommend_dealer = [];
	for i in recommend_dealer_init:
		recommend_dealer.append(i.text.strip());

	#strip tags and new lines from text and append to new list
	review_text = [];
	for j in review_text_init:
		review_text.append(j.text.strip());

	#strip tags and new lines from text and append to new list, the header is the text above the review on dealerrater.com
	header_info = [];
	for k in review_header_init:
		header_info.append(k.text.strip());

	#dictionary created to map values to, (int, int), where the first int is an index of the review
	#and the second int is a value that depicts the positive connotation value of a review, the higher the values, the greater the positivity
	review_dict = {};

	#this should index the dictionary (map) to each index and a put a corresponding value of zero for 
	#the positive connotation value. This is done to avoid KeyErrors later on
	for u in range(0, len(review_text)):
		review_dict[u] = review_dict.get(u, 0);

	#place a heavier weight on this because im using this to simulate the 5 star review vs the 1 star review, reviews given -1000 are reviews that are "1 star reviews" and 
	#therefore shouldn't be considered (hence the very large negative rating given)
	for recommendation in range(0, len(recommend_dealer)):
		if (recommend_dealer[recommendation] == "Yes"):
			review_dict[recommendation] += 8; 
		else:
			review_dict[recommendation] -= 10000; 

	#loops thru the words in the header, and checks for whether there are matching words and adds that to the positive connotation value for that review
	for info in range(0, len(header_info)):
		words_in_header = header_info[info].split();
		for word in words_in_header:
			word = word.lower();
			for character in string.punctuation:
				word = word.replace(character, "");
			for preset_words in positive_words:
				if (word == preset_words):
					review_dict[info] += 1;
	
	#loops thru the words in the header, and checks for whether there are exclamation marks and adds that to the positive connotation value for that review
	for info in range(0, len(header_info)):
		words_in_header = header_info[info].split();
		for word in words_in_header:
			for letter in word:
				if (letter == '!'):
					review_dict[info] += 1;


	#loops thru the words in the actual review, and checks for whether there are matching words and adds that to the positive connotation value for that review
	#I strip punctuation here as well as put the word to lowercase temporarily so that we can match with the preset words (which don't have punctuation)
	for review in range(0, len(review_text)):
		words_in_a_review = review_text[review].split();
		for word in words_in_a_review:
			word = word.lower();
			for character in string.punctuation:
				word = word.replace(character, "");
			for preset_words in positive_words:
				if (word == preset_words):
					review_dict[review] += 1;
					break;

	#loops thru the words in the review, and checks for whether there are exclamation marks and adds that to the positive connotation value for that review
	for review in range(0, len(review_text)):
		words_in_a_review = review_text[review].split();
		for word in words_in_a_review:
			for letter in word:
				if (letter == '!'):
					review_dict[review] += 1;

	#place a little bit less weight on finding a capital letter because it possible that only one word is capitalized, it would heavily skew data if we gave a +1 
	#for each capital letter
	for review in range(0, len(review_text)):
		words_in_a_review = review_text[review].split();
		for word in range(0, len(words_in_a_review)):
			for letter in range(0, len(words_in_a_review[word])):
				if (letter != 0 and ord(words_in_a_review[word][letter]) >= 65 and ord(words_in_a_review[word][letter]) <= 90):
					review_dict[review] += 0.3;

	#here we add the items added to this dictionary from this page to the dictionary that is holding all of the reviews (by index)
	dict_count = 0;
	for i in review_dict.items():
		all_reviews_dict[num_of_total_reviews] = review_dict[dict_count];
		dict_count += 1;
		num_of_total_reviews += 1;

#sort the dictionary so that the greatest positive connotation values for each review are at the beginning of the dictionary, then print the next three values
all_reviews_dict = sorted(all_reviews_dict.items(), key=lambda x: x[1], reverse=True);
#print top 3 reviews
for top_reviews in range(0, 3):
	print("Review " + str(all_reviews_dict[top_reviews][0]) + " with a score of " + str(all_reviews_dict[top_reviews][1]));
print("(Reviews are zero-indexed)")
