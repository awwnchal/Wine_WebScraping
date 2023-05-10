#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 18:25:44 2023

@author: anchalchaudhary
"""
#Assignments 8 & 9

#WARM-UP

# =============================================================================
# (a) (We have done most of this in class in class already.) Write a program in Python that [uses]
# Selenium to remote control a browser to [access] https://www.vivino.com/US-CA/en/, [clicks] on
# “Wines” in the upper left hand corner, and displays all “Red” wines (only “Red”, “White” needs to be
# [deactivated]). [Select] “Any rating”.
# 
# =============================================================================
from selenium import webdriver #selenium automates web browsers
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo
import json
import random
import re

def main():
    #q3_and_q4_q5()
    q7()

    
def q1():
    
    
    driver = webdriver.Chrome(executable_path='/Applications/chromedriver')
    driver.implicitly_wait(10)
    driver.set_script_timeout(120)
    driver.set_page_load_timeout(10)
    
    driver.get("https://www.vivino.com/US-CA/en/");
    
    wines = driver.find_element(By.CSS_SELECTOR, "span[title='Wines']")
    wines.click()
    
    time.sleep(2)
    
    white = driver.find_element(By.XPATH, "//span[text()='White']");
    white.click()
    time.sleep(2)
    
    sparkling = driver.find_element(By.XPATH,"//span[text()='Sparkling']");
    sparkling.click()
    time.sleep(2)
    
    rose = driver.find_element(By.XPATH,"//span[text()='Rosé']");
    rose.click()
    time.sleep(5)
    
    
    clear_button = driver.find_element(By.XPATH, "//input[@name='rating'][@id='1']")
    
    clear_button.click()
    time.sleep(2)
    driver.quit()


#part b 


# =============================================================================
# This is the only part that doesn’t require programming: click on some red wines listed at
# https://www.vivino.com/US-CA/en/ and see how Vivino’s URL changes for every wine. Typical Vivino
# wine URLs are
#  https://www.vivino.com/US-CA/en/bethel-heights-pinot-noir-rose/w/45
#  https://www.vivino.com/US-CA/en/benton-lane-winery-pinot-noir/w/128
#  https://www.vivino.com/US-CA/en/belle-pente-estate-reserve-pinot-noir/w/1810061
# First notice how the wine ID changes. Try modifying the URL / wine ID yourself. Second notice also that
# the URL still functions even if you drop the wine name. E.g., try navigating to
# https://www.vivino.com/US-CA/en/w/128. Third notice also that some URLs yield 404 errors, e.g.
# https://www.vivino.com/US-CA/en/w/1. Last notice that some wine IDs get forwarded, e.g.
# https://www.vivino.com/US-CA/en/w/11 get forwarded to ID 2419093.
# # ===========================================================================


#  noticed all things said in part2





# part (c)

# =============================================================================
# For the wine IDs 1, 11, and 128, [use] Selenium to access the pages https://www.vivino.com/US-
# CA/en/w/[ID]. Leave some pause between page loads. [Print] the ID to terminal. [Read] the URL of the
# resulting page and [print] it to terminal. [Check] whether it exists (404 error or not) and [print] to
# terminal “404 error” or “no 404 error”. Lastly, check if the resulting page has an ID different to the one
# you tried to access and [print] to terminal “not forwarded” or “forwarded to [ID]”.
# (d) [Use] Selenium to access the wine ID 1695288 (exists, is not forwarded, and is Lokoya’s expensive
# Cabernet Sauvignon). [Scroll] to the bottom of the page. In Selenium, [scrolling] can be achieved by
# [pressing] the page-down button about 10 times.
# =============================================================================

def q2():
    try:
             
    
        driver = webdriver.Chrome(executable_path='Applications/chromedriver')
        driver.implicitly_wait(10)
        driver.set_script_timeout(120)
        driver.set_page_load_timeout(10)
        wine_ids = [128,11,1]
        #driver.get("https://www.vivino.com/US-CA/en/benton-lane-winery-pinot-noir/w/1")
        
        for wine_id in wine_ids:
           
          # Construct the URL and navigate to it
          url = f"https://www.vivino.com/US-CA/en/w/{wine_id}"
          driver.get(url)      
          time.sleep(2)
        
          wid = driver.current_url.split('/')[-1]
      
          print(wid)
          if str(wine_id) == wid:
               print("Not forwarded")
          else:
               print("Forwarded")
          
          link_element = driver.find_element(By.CSS_SELECTOR,'link[rel="canonical"]')
          link = link_element.get_attribute('href')
          print(link)
          
          
        
                   
          print("No 404 error" ) 
          
          
    except:
        
         print("404 error found" ) 
        

    driver.quit()


#part d and part e

# =============================================================================
# (d) [Use] Selenium to access the wine ID 1695288 (exists, is not forwarded, and is Lokoya’s expensive
# Cabernet Sauvignon). [Scroll] to the bottom of the page. In Selenium, [scrolling] can be achieved by
# [pressing] the page-down button about 10 times.
# (e) [Click] on “Show more reviews”.
# 
#didnt do part f
#part g
# =============================================================================
def q3_and_q4_q5():
  

        driver = webdriver.Chrome(executable_path='Applications/chromedriver')
        driver.implicitly_wait(10)
        driver.set_script_timeout(120)
        driver.set_page_load_timeout(10)
        # Access the wine ID 1695288
        url = "https://www.vivino.com/US-CA/en/w/1695288"
        driver.get(url)
        
        # Scroll to the bottom of the page
        for i in range(8):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            # Click on the "Show more reviews" button
        show_more_button = driver.find_element(By.XPATH, "//span[text()='Show more reviews']");
        show_more_button.click()
        time.sleep(2)     
        page_source = driver.page_source
        
        # Add some lines to the top of the HTML code
        header_lines = """
        <!--ID:1695288-->
        <!--URL:https://www.vivino.com/US-CA/en/lokoya-winery-mount-veeder-cabernet-sauvignon/w/1695288-->
        """
        page_source = header_lines + page_source + "</body></html>"
        
        # Save the modified HTML code to a file
        with open('vivino_id_1695288.html', "w") as f:
            f.write(page_source)
        
        driver.quit()
        
from bs4 import BeautifulSoup


# =============================================================================
# (f) IF YOU CAN (please skip this question if you cannot figure out a solution within 30 minutes of trying)
# Find a way to [scroll] down to load as many reviews as you can within the review window. One way is to
# [select] an element within the review window and then [press] the page-down button to [scroll] down.
# Really no worries if you skip this question.        
# =============================================================================
#part h
def q6():
    
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
     
    
    db = client["vivino"] #database
    #“wines”, “reviews”, “links”,
    wines = db["wines"]   
    reviews = db["reviews"]
    links = db["links"]
    taste = db["taste"]
    
    wines.drop()  
    reviews.drop()
    
    filename = "vivino_id_1695288.html"
    
    with open(filename, 'r') as file:
        
        
         d = {}
         soup = BeautifulSoup(file, 'html.parser')                      
         a_tag = soup.find('a', {'class': 'anchor_anchor__m8Qi- vintageListRow__anchor--2qyEJ', 'href': True})
         d["wine ID"] = a_tag['href'].split('/')[-1]
         d["winery"] = soup.select("a.winery")[0].text
         d["name"] = soup.select("span.vintage")[0].text
         d["grapes"] = soup.select("td.wineFacts__fact--3BAsi")[1].text
         d["region"] = soup.select("td.wineFacts__fact--3BAsi")[2].text
         d["winestyle"] = soup.select("td.wineFacts__fact--3BAsi")[3].text
         d["allergens"] = soup.select("td.wineFacts__fact--3BAsi")[4].text
         badges =  soup.select("div.rightColumn")
         d["average rating"] = soup.select("div.vivinoRating_averageValue__uDdPM")[0].text
         d["no of ratings"] = soup.select("div.vivinoRating_caption__xL84P")[0].text
         d["average price"] = soup.select("span.purchaseAvailability__currentPrice--3mO4u")[0].text
         d["goes well with"] = soup.select("a.anchor_anchor__m8Qi-.foodPairing__imageContainer--2CtYR")
         
         goes_well_list = []
         
         for i in  d["goes well with"]:
             goes_well_list.append(i.text)
            
         
         badge_list = []
         

         for i in  badges:
             badge_list.append(i.text.strip())   
         badge_list = list(set(badge_list))
         
         #print(badge_list) 

         
         d["badges"] = badge_list
         

         
         d["goes well with"] = goes_well_list
         d["badge list"] = badge_list
         
         wines.insert_one(d)
         
         
         
       
         
         user_name = soup.select("a.anchor_anchor__m8Qi-.userAlias_userAlias__ztmrT")
        # user_name = re.sub(r'\(.*?\)', '', user_name)
         
         star_ratings = soup.select("span.userRating_ratingNumber__cMtKU")
         
         
         list_number_of_likes = soup.select("div.likeButton__likeCount--1stJS")
         list_num_of_comments = soup.select("div.commentsButton__commentsCount--3CoCn")
         text_list = soup.select("span.communityReview__reviewText--2bfLj")
         vintage = soup.select("a.anchor_anchor__m8Qi-.reviewAnchor__anchor--2NKFw.communityReview__reviewContent--3xA5s")
  
         output_list = []
        
        
         for i in range(len(user_name)):
             d1 = {}
            
             un = user_name[i].text
             un = re.sub(r'\(.*?\)', '', un)
             d1["user_name"] = un 
            
             d1["star_ratings"] = star_ratings[i].text
            
             d1["number_of_likes"] = list_number_of_likes[i].text
             d1["number_of_commens"] = list_num_of_comments[i].text
             d1["text"] = text_list[i].text
            
             if len(vintage[i].select("span.reviewedVintageYear__vintageText--3TZOW.communityReview__vintageText--vW6OI")) != 0: 
                 d1["vintage"]= vintage[i].select("span.reviewedVintageYear__vintageText--3TZOW.communityReview__vintageText--vW6OI")[0].text
             else:
                 d1["vintage"] = "None"
            
            
             reviews.insert_one(d1)
            


def q7():
    import random

    wine_ids = random.sample(range(1, 999999), 1000)
    #wine_ids = [100267,10]
    try:
         client = pymongo.MongoClient()
    except Exception:
         print("Error: " + Exception) 
    db = client["vivino"] #database
    #“wines”, “reviews”, “links”,
    wines = db["wines"]   
    reviews = db["reviews"]
    taste = db["taste"]
    wines.drop()  
    reviews.drop()
    taste.drop()

    for wine_id in wine_ids:
        
        driver = webdriver.Chrome(executable_path='/UApplications/chromedriver')
        driver.implicitly_wait(2)
        driver.set_script_timeout(120)
        driver.set_page_load_timeout(2)
        # Access the wine ID 1695288
        url = "https://www.vivino.com/US-CA/en/w/"+ str(wine_id)
        driver.get(url)
        
        # Scroll to the bottom of the page
        for i in range(8):
            driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
            page_source = driver.page_source
            # Click on the "Show more reviews" button
        try:
            show_more_button = driver.find_element(By.XPATH, "//span[text()='Show more reviews']");
            show_more_button.click()
            time.sleep(2)     
            
        except:
            print("No wine found for this wine_id")
        
        # Add some lines to the top of the HTML code
        header_lines = """
        <!--ID:{}-->
        <!--URL:https://www.vivino.com/US-CA/en/w/{}-->
        """.format(wine_id, wine_id)
        page_source = header_lines + page_source + "</body></html>"
        
        # Save the modified HTML code to a file
        file_name = 'vivino_id_{}.html'.format(wine_id)
        with open(file_name, "w") as f:
            f.write(page_source)
        
        
        
        
        with open(file_name, 'r') as file:
            
            
             d = {}
             soup = BeautifulSoup(file, 'html.parser')                      
             #a_tag = soup.find('a', {'class': 'anchor_anchor__m8Qi- vintageListRow__anchor--2qyEJ', 'href': True})
        
             try:
                 d["wine ID"] = wine_id
                 d["winery"] = soup.select("a.winery")[0].text
                 d["name"] = soup.select("span.vintage")[0].text
                 d["grapes"] = soup.select("td.wineFacts__fact--3BAsi")[1].text
                 d["region"] = soup.select("td.wineFacts__fact--3BAsi")[2].text
                 d["winestyle"] = soup.select("td.wineFacts__fact--3BAsi")[3].text
    #             d["allergens"] = soup.select("td.wineFacts__fact--3BAsi")[4].text
                 badges =  soup.select("div.rightColumn")
                 d["average rating"] = soup.select("div.vivinoRating_averageValue__uDdPM")[0].text
                 d["no of ratings"] = soup.select("div.vivinoRating_caption__xL84P")[0].text
    #             d["average price"] = soup.select("span.purchaseAvailability__currentPrice--3mO4u")[0].text
    #             d["goes_well_with"] = soup.select("a.anchor_anchor__m8Qi-.foodPairing__imageContainer--2CtYR")
                 
    #              goes_well_list = []
    #              
    #              for i in  d["goes_well_with"]:
    #                  goes_well_list.append(i.text)
    #                 
    
                 
                 badge_list = []
                 
            
                 for i in  badges:
                     badge_list.append(i.text.strip())   
                 badge_list = list(set(badge_list))
                 
                 #print(badge_list) 
            
                 
                 d["badges"] = badge_list
                 
            
                 
    #             d["goes well with"] = goes_well_list
                 d["badge list"] = badge_list
                 
                 wines.insert_one(d)
                 
                 
                 
               
                 
                 user_name = soup.select("a.anchor_anchor__m8Qi-.userAlias_userAlias__ztmrT")
                # user_name = re.sub(r'\(.*?\)', '', user_name)
                 
                 star_ratings = soup.select("span.userRating_ratingNumber__cMtKU")
                 
                 
                 list_number_of_likes = soup.select("div.likeButton__likeCount--1stJS")
                 list_num_of_comments = soup.select("div.commentsButton__commentsCount--3CoCn")
                 text_list = soup.select("span.communityReview__reviewText--2bfLj")
                 vintage = soup.select("a.anchor_anchor__m8Qi-.reviewAnchor__anchor--2NKFw.communityReview__reviewContent--3xA5s")
              
                 output_list = []
                
                
                 for i in range(len(user_name)):
                     d1 = {}
                    
                     un = user_name[i].text
                     un = re.sub(r'\(.*?\)', '', un)
                     d1["user_name"] = un 
                    
                     d1["star_ratings"] = star_ratings[i].text
                    
                     d1["number_of_likes"] = list_number_of_likes[i].text
                     d1["number_of_commens"] = list_num_of_comments[i].text
                     d1["text"] = text_list[i].text
                    
                     if len(vintage[i].select("span.reviewedVintageYear__vintageText--3TZOW.communityReview__vintageText--vW6OI")) != 0: 
                         d1["vintage"]= vintage[i].select("span.reviewedVintageYear__vintageText--3TZOW.communityReview__vintageText--vW6OI")[0].text
                     else:
                         d1["vintage"] = "None"
                    
                    
                     reviews.insert_one(d1)
                 
                     
    
                 spans = soup.find_all('span', class_='indicatorBar__progress--3aXLX')
                 properties = {"bold","tannic", "sweet","acidic"}
    
                 for span, property in zip(spans, properties):
                     d2 = {}
                     style = span['style']
                     d2["id"] = wine_id
                     d2[property] = re.search(r'left:\s*([\d.]+)%', style).group(1)
                     taste.insert_one(d2)
                 
             except:
                 print("No wine found for this wine id")
             
                

        
        driver.quit()
        
        
    







# =============================================================================
if __name__ == '__main__':
	main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


