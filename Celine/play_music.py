from selenium import webdriver  
from time import sleep
driver=webdriver.Chrome()
def open_music(song_name):
    driver.get(f"https://www.youtube.com/results?search_query={song_name}")
    driver.implicitly_wait(10)
    driver.find_element_by_id("video-title").click()
open_music('EK raat')