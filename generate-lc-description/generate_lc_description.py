from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys
import os

def fetch_leetcode_description(question_slug):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
        url = f'https://leetcode.com/problems/{question_slug}/'
        driver.get(url)

        wait = WebDriverWait(driver, 10)
        question_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="qd-content"]/div[1]/div/div[1]/div/div[2]/div/div/div[3]/div[2]')))

        rendered_html = driver.page_source
        soup = BeautifulSoup(rendered_html, 'html.parser')


        description_element = soup.find('div', {'data-track-load':'description_content'})
        
        # Removing div tag
        description = ''.join(map(str, description_element.contents))

        return description
    
    finally:
        driver.quit()



if __name__ == '__main__':
    title = "Two Sum" # Passing default question

    # Pass title in command line arg while running script
    if len(sys.argv) > 1:
        title = sys.argv[1]

    
    # Title converted to lower case, split by space, joined by - to generate quesiton slug
    question_slug = "-".join(title.lower().split())  

    description = fetch_leetcode_description(question_slug)

    
    dir_path = f"{question_slug}"

    # Create directory if not present
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


    # Create file
    file = open(f'{dir_path}/description.md', "w")

    file_content = [f'<h2> {title} </h2> \n', "<hr>", description]

    file.writelines(file_content)
     
    # Close file
    file.close()