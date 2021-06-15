from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox()
browser.get("http://www.instagram.com")

time.sleep(3)

girisYap = browser.find_element_by_xpath("//*[@id='react-root']/selection/main/article/div[2]div[2]/p/a")
girisYap.click()

time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)


loginButton = browser.find_element_by_xpath("//*[id='react-root']/section/main/article/div[2]/div[1]/div/form/span/button")
loginButton.click()

time.sleep(5)


profileButton = browser.find_element_by_xpath("//*[id='react-root']/section/nav/div[2]/div/div/div[3]/a")
profileButton.click()

time.sleep(3)

buttons = browser.find_element_by_css_selector("._bnq48")
followersButton = buttons[1]
followersButton.click()

time.sleep(5)

#Console kısmında js codu çalıştıracagız
#followers = document.querySelector("._gs38e")
#followers bastırılır.
#scroll kısmını çalıştırmak için
#followers.scrollTo(0,followers.scrollHeight) çalıştırılır. Şimdi artık bu kodu selenıumda kullanalım

jscommand = """
            followers = document.querySelector("._gs38e");
            followers.scrollTo(0,followers.scrollHeight);
            var lenOfPage = followers.scrollHeight;
            return lenOfPage;
            """

lenOfPage = browser.execute_script(jscommand)
match = False
while match == False:
    lastCount = lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match = True
time.sleep(5)

followersList = []

followers = browser.find_element_by_css_selector("._2g7d5.notranslate._o5iw8")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt", "w", encoding = "UTF-8") as file:
    for follower in followersList:
        file.write(follower + "\n")

browser.close()

