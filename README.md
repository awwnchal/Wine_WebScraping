
# Wine Web Scraping with Selenium and MongoDB
This project involves automated web scraping of 1000 wine pages from the Vivino wine website, storing reviews and various metadata in a MongoDB database. The code was written in Python using Selenium to navigate and scrape data from the website.

Introduction:
The Vivino wine website is a popular platform that provides detailed information about different wines. The website contains various pages that list wines based on their colors, ratings, and prices. This project aims to use Selenium to extract data from the Vivino wine website and store it in a MongoDB database. The extracted data includes wine details, reviews, links, and taste. The project involves writing Python code to perform web scraping and MongoDB storage tasks.


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
