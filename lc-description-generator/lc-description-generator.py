from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import sys
import os

def fetch_leetcode_description(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    try:
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

    url = f'https://leetcode.com/problems/{question_slug}/'

    description = fetch_leetcode_description(url)
    
    #dir_path = f"{question_slug}"

    dir_path = f"/Users/rjain/personal/dsa/leetcode/{question_slug}"

    #dir_path = f"/Users/rjain/personal/dsa/main/arrays/{question_slug}"

    # dir_path = f"/Users/rjain/personal/dsa/main/linked-lists/{question_slug}"

    # dir_path = f"/Users/rjain/personal/dsa/main/stack-and-queue/{question_slug}"

    #dir_path = f"/Users/rjain/personal/dsa/main/bfs-in-a-grid/{question_slug}"

    # dir_path = f"/Users/rjain/personal/dsa/main/backtracking/{question_slug}"

    # dir_path = f"/Users/rjain/personal/dsa/main/dp-on-strings/{question_slug}"

    # dir_path = f"/Users/rjain/personal/dsa/main/dp/{question_slug}"

    # Create directory if not present
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


    # Create file
    file = open(f'{dir_path}/description.md', "w")

    file_content = [f'<h2><a href="{url}" target="_blank">{title}</a></h2>\n', "<hr>", description]

    file.writelines(file_content)
     
    # Close file
    file.close()