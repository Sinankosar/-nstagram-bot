from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from instagramUserInfo import username, password
import time
s = Service(r"C:\Program Files (x86)\chromedriver.exe")
class Instagram:
    def __init__(self, username, password):  
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{'intl.accept_langueges':'en,en_US'})
        self.browser = webdriver.Chrome(service=s, options=self.browserProfile)
        self.username = username
        self.password = password
        self.sayi =1
        self.liste =[]
        
        
    def signIn(self):
        self.browser.get("https://www.instagram.com")
        time.sleep(2)
        emailInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        emailInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(4)
        

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(3)
       
        # takipcilere tıklama
        self.browser.get(f"https://www.instagram.com/{self.username}/following/?next=%2F")
        time.sleep(4)
        
        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[class='_aano'] div div")
        liste = dialog.find_elements(By.CSS_SELECTOR, "div[class='x1dm5mii x16mil14 xiojian x1yutycm x1lliihq x193iq5w xh8yej3']")
        users = []
        dialog.click()
    
        for i in liste:
            a = i.find_element(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1'] span").text
            print(f"{self.sayi}. : {a}")
            self.liste.append(a)
            users.append(a)
            self.sayi +=1
        
        with open("Following.txt","w",encoding="UTF-8") as file:
            for j in users:
                    file.write(j+ "\n")        
    def unfollow(self):
        for i in self.liste:
            self.browser.get(f"https://www.instagram.com/{i}/")
            time.sleep(5)
            
            #takiptesin butonu
            buton = self.browser.find_element(By.CSS_SELECTOR, "button[class =' _acan _acap _acat _aj1- _ap30']")
            buton.click()
            time.sleep(3)
            takibi_bırak_but =self.browser.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div/div/div/span/span")
            if takibi_bırak_but.text == "Takibi Bırak":
                takibi_bırak_but.click()

instgrm = Instagram(username, password)
instgrm.signIn()
instgrm.getFollowers()
instgrm.unfollow()
