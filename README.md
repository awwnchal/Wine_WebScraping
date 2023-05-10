
# Wine Web Scraping with Selenium and MongoDB
This project involves automated web scraping of 1000 wine pages from the Vivino wine website, storing reviews and various metadata in a MongoDB database. The code was written in Python using Selenium to navigate and scrape data from the website.

Introduction:
The Vivino wine website is a popular platform that provides detailed information about different wines. The website contains various pages that list wines based on their colors, ratings, and prices. This project aims to use Selenium to extract data from the Vivino wine website and store it in a MongoDB database. The extracted data includes wine details, reviews, links, and taste. The project involves writing Python code to perform web scraping and MongoDB storage tasks.

# Project Overview

1. Navigating Vivino's Website

The first part of the project involves using Selenium to navigate the Vivino website. The program will automate browser actions to access specific pages, such as selecting "Wines," filtering by wine type, and choosing the desired rating. The goal is to familiarize yourself with Selenium and verify the functionality of the website.

2. Web Scraping

The next step is to implement web scraping functionality. The program will use Selenium to access wine pages with specified wine IDs, pause between page loads, and perform various actions. These actions include printing the ID and URL of the resulting page, checking for 404 errors, and determining if the page is forwarded to a different ID.

Additionally, the program will access specific wine pages, scroll to the bottom, and click on "Show more reviews" to load additional reviews. If possible, it will scroll down further to load as many reviews as possible within the review window.

The loaded page will be saved as an HTML file, with the original ID and destination URL added as headers.

3. Parsing and Storing

The final step involves parsing the saved HTML files and storing the extracted information in MongoDB. The program will create a MongoDB database named "vivino" with collections for wines, reviews, links, and taste. It will read the saved files and store the wine-related data in the "wines" collection, the reviews in the "reviews" collection, the encountered wine IDs in the "links" collection, and the taste information in the "taste" collection.

To expand the dataset, the program will repeat the web scraping and storing process for 1,000 random wine IDs between 1 and 999,999.


# Features
The following data is scraped and stored for each wine:

wine_id

winery

name

grapes

badges

region

wine_style

allergens

date_of_download

avg_rating

num_rating

avg_price

goes_well_with

user_id

user_name

num_user_reviews

vintage


# Technologies

The project is built using the following technologies:

Python 3.9

Selenium 4.0

MongoDB 5.0

# Getting Started

To get started with this project, follow these steps:

Clone the repository to your local machine.

Install the required Python packages using pip install -r requirements.txt.

Download and install the latest version of MongoDB from their official website.

Start MongoDB on your local machine.

Run the main.py script using python main.py.

The main.py script will automatically navigate to the Vivino wine website, scrape data for 1000 wines, and store the data in a MongoDB database.

Acknowledgments

This project was inspired by the need to automate the collection of wine data for furthur analysis.
