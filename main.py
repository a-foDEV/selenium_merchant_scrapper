from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import sched
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.python.org")

s = sched.scheduler(time.time, time.sleep)


def main(sc):
    print(driver.title)
    sc.enter(30, 1, main, (sc,))


if __name__ == '__main__':
    s.enter(30, 1, main, (s,))
    s.run()
