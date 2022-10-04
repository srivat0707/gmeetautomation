import time
import pandas as pd
import datetime 
import calendar 
from datetime import date
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.alert import Alert 
from selenium.webdriver.chrome.options import Options
import webbrowser
from webdriver_manager.chrome import ChromeDriverManager
a=0
def idlink():
  try:
    dates = date.today()
    today=dates.strftime('%d %m %Y')
    day, month, year = (int(i) for i in today.split(' '))     
    dayNumber = calendar.weekday(year, month, day)
    t = time.localtime()
    current_time = time.strftime("%H ", t)
    current_times = time.strftime("%H %M", t)
    ct=current_times.split()
    print(ct)
    if ct[0]<11 and ct[0]>8:
      if ct[1]<45:
        current_time-=1
    elif ct[0]>15:
      if ct[1]<15:
        current_time-=1
    master_link=[['',"frt-jesp-wss","",'',"sdc-dcua-nmd",'',"qpk-vxjr-cvi"],["cvd-ybbr-jyp","ifc-anwh-ded","1",'','',"2",''],["","ifc-anwh-ded","",'',"zuy-acbi-unr","yxh-cdzj-vdv",''],['',"1",'',"2"],['','','','','','',"ifc-anwh-ded"],["tjv-afrs-uwz"]]
    df = pd.DataFrame(master_link,columns=['08','09','10','11','14','15','16'])
    s=df[current_time]
    return s[dayNumber]
  except:
    print("no class")
    time.sleep(2)
    webbrowser.open_new_tab('index.html')
    global a
    a+=1


gmailId="124158078@sastra.ac.in"
passWord='Srivatsan07@!'
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("user-data-dir=C:\environments\selenium")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2
  })
if a==0:
  driver = webdriver.Chrome(ChromeDriverManager().install(),options=opt)
  driver.get("https://gmail.com")
  meet=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]/div')
  meet.click()
  Id=idlink()
  id=driver.find_element_by_xpath('//*[@id="yDmH0d"]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
  id.send_keys(Id,Keys.ENTER)
  driver.implicitly_wait(10)
  camera=driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div')
  camera.click()
  driver.implicitly_wait(9)
  join=driver.find_element_by_xpath("//span[@class='NPEfkd RveJvd snByac' and contains(text(), 'Join now')]")
  join.click()
