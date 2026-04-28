# Data Dictionary
#### This file will clarify the meaning of each column and its binarization.

## google_index
#### Most legitimate websites appear in Google's search index. Phishing websites are too new or hidden to be indexed. (1 = indexed, 0 = not indexed)

## page_rank
#### Represents the ranking (from 0 to 10) of a page based on links from other sites. Phishing pages' rank is usually 0 or low.

## domain_age
####  The amount of time that has passed since the domain was registered. Phishing pages use domains that are too new.

## web_traffic
####  Measures how many people visit the site. Phishing sites usually have extremely low traffic or none.

## safe_anchor
####  The percentage of links that lead back to the same website. 

## phish_hints
####  Searches for sensitive words such as ('login', "secure", 'pay', etc.)

## ratio_intHyperlinks
####  The ratio of internal links to the total number of links.

## nb_hyperlinks
####  The total count of link on the page. Phishing websites usually have few links.

## length_url
####  The length of the URL. Phishing URLs are commonly longer > 75 characters

## nb_www
####  The presense of 'www' is usually a sign of a safe URL.

## ratio_digits_url
####  The percentage of numbers in the URL. More numbers means it's more likely to be phishing.

## length_hostname
####  Long hostnames are commonly used to keep the actual domain out of the visible are in mobile browsers. It's a clear sign of phishing.

## longest_word_path
####  Identifies the longest string in the URL. Long, nonsensical words are usually a sign of phishing.

## char_repeat
####  Characters repeated more than two times raise red flags.

## avg_word_path
####  The average length of words in the URL. The red fglag is if it's > 10 characters.

## shortest_word_host
####  Determines the shortest word in the hostname to identify suspicious and short subdomains.

## longest_words_raw
####  Finds which word is the longest. If it's > 30 character then it's a sign of phishing.

## length_words_raw
####  Measurements of word length accross the URL to identify abnormalities. Presence of abnormalities could mean it's a phish.

## ratio_extRedirection
####  The frequency of which a page redirects the user to external websites. High redirection is a sign of phishing.

## ratio_extHyperlinks
####  The ratio of external hyperlinks to the total number of links. If it's more than 60%, it's most likely phishing.

## status
#### States whether the URL is legitimate or phishing.