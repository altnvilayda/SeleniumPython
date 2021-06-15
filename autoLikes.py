from selenium import webdriver
import loginInfo  #şifre ve kullanıcım var bunda tabii benim yok tweet hesabı../
import time

browser = webdriver.Firefox()
browser.get("https://twitter.com/")

time.sleep(3)
giris_yap = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div")

giris_yap.click()
time.sleep(5)

username = browser.find_element_by_xpath("//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]")
password = browser.find_element_by_xpath("//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)
time.sleep(3)

login = browser.find_element_by_xpath("//*[@id='page-container']/div/div[1]/form/div[2]/button")
login.click()

time.sleep(5)

searchArea = browser.find_element_by_xpath("//*[@id='search-query']")
searchButton = browser.find_element_by_xpath("//*[@id='global-nav-search']/span/button")
searchArea.send_keys("#yazilimayolver")

searchButton.click()
time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeigh;return lenOfPage;")
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

elements = browser.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")

for element in elements:
    try:
        element.click()

    except Exception:
        print("Bir sorun oluştu...")


browser.close()










