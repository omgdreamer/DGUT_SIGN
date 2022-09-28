from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Chrome浏览器
driver = webdriver.Chrome()
driver.get('https://yqfk-daka.dgut.edu.cn/')

time.sleep(2)
# 登录账号密码
text_label = driver.find_element(By.ID, 'username')
text_label.send_keys('202041413220')
text_label = driver.find_element(By.ID, 'password')
text_label.send_keys('Aa86532909')

# 执行单击操作
driver.find_element(By.ID, 'login_submit').click()

time.sleep(3)

# 1
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div')
# 填写温度
driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/form/div/div['
                              '2]/div/div/div/div/div/textarea').send_keys('36')
# 填写身体状况
time.sleep(3)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/form/div/div[1]/div/div/div/i')
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[5]/div/div[1]/button[2]')
driver.execute_script("arguments[0].click();", button)

# 填写校区
time.sleep(3)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/div/form/div/div[3]/div/div/div/i')
driver.execute_script("arguments[0].click();", button)
time.sleep(2)
button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[7]/div/div[1]/button[2]')
driver.execute_script("arguments[0].click();", button)

# 点击操作
time.sleep(3)
js = "document.getElementsByClassName('van-button van-button--info van-button--normal van-button--round')[0].click();"
driver.execute_script(js)
