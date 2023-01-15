from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

driver_path = 'C:/Users/Admin/Desktop/SOFTDEV2/SOFTWARE-DEVELOPMENT-2/GoogleForm/chromedriver.exe'
chr_options = Options()
chr_options.add_experimental_option("detach", True)
chr_driver = webdriver.Chrome(driver_path, options=chr_options)
chr_driver.maximize_window()
chr_driver.get("https://docs.google.com/forms/d/e/1FAIpQLScodw0_8qRRC4cUV0ushbSVvEqiIc2_ddrzCB8iyXADaMFhlg/formResponse")

login_box = chr_driver.find_element(By.XPATH, "//input[@name='identifier']")
login_box.send_keys('s6401012630043@email.kmutnb.ac.th')
chr_driver.implicitly_wait(10)

nextBotton1 = chr_driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
nextBotton1.click()
chr_driver.implicitly_wait(10)

password_box = chr_driver.find_element(By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")
password_box.send_keys('1101501132323')
chr_driver.implicitly_wait(10)

nextBotton2 = chr_driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button/span")
nextBotton2.click()
time.sleep(5)

clear_form = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[2]/div/span/span")
clear_form.click()
time.sleep(1)

confirm_clear = chr_driver.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[2]/span/span")
confirm_clear.click()
time.sleep(1)

email_box = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input")
email_box.send_keys('s6401012630043@email.kmutnb.ac.th')
time.sleep(1)

choice_choose = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div[1]/div/span/div/div[1]/label/div")
choice_choose.click()
time.sleep(1)

multichoice_choose1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label")
multichoice_choose2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[2]/label")
multichoice_choose1.click()
multichoice_choose2.click()
time.sleep(1)

select_box = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[1]")
select_box.click()
select_choose = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[3]")
select_choose.click()
time.sleep(1)

nextBotton3 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div/span")
nextBotton3.click()
time.sleep(1)

short_box = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
short_box.send_keys('มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ')
time.sleep(1)

paragraph_box = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea")
paragraph_box.send_keys('มหาวิทยาลัยเทคโนโลยีพระจอมเกล้าพระนครเหนือ (KMUTNB) เป็นมหาวิทยาลัยในกำกับของรัฐบาล ก่อตั้งโดยความร่วมมือระหว่างรัฐบาลไทยกับรัฐบาลเยอรมนี ในปี พ.ศ. 2502 ในนาม "โรงเรียนเทคนิคพระนครเหนือ" ก่อนจะยกฐานะในปี พ.ศ. 2507 เป็น "วิทยาลัยเทคนิคพระนครเหนือ" และเป็น "สถาบันเทคโนโลยีพระจอมเกล้า วิทยาเขตพระนครเหนือ" ในปี พ.ศ. 2514 ต่อมาสถาบันเทคโนโลยีพระจอมเกล้าทั้งสามได้แยกออกจากกันโดยมีอำนาจบริหารเป็นอิสระ ในปี พ.ศ. 2529 และได้ถูกยกฐานะเป็น มหาวิทยาลัยในปี พ.ศ. 2551 ในปัจจุบันมหาวิทยาลัยฯ ได้แบ่งออกเป็น 3 วิทยาเขต ได้แก่ วิทยาเขตกรุงเทพมหานคร, ปราจีนบุรี และระยอง เปิดทำการเรียนการสอนทั้งหมด 13 คณะ 2 วิทยาลัย 2 บัณฑิตวิทยาลัย ตั้งแต่ระดับประกาศณียบัตรวิชาชีพ (ปวช.) ปริญญาตรี ปริญญาโท และ ปริญญาเอก')
time.sleep(1)

nextBotton4 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
nextBotton4.click()
time.sleep(1)

choose_scale = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/span/div/label[1]/div[2]/div/div/div[3]/div")
choose_scale.click()
time.sleep(1)

grid1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[2]/span/div[2]/div/div/div[3]/div")
grid1.click()
time.sleep(1)

grid2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[4]/span/div[3]/div/div/div[3]/div")
grid2.click()
time.sleep(1)

grid3 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[6]/span/div[4]/div/div/div[3]/div")
grid3.click()
time.sleep(1)

grid4 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[8]/span/div[6]/div/div/div[3]")
grid4.click()
time.sleep(1)

multi_grid1_1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/label[1]/div/div/div[2]")
multi_grid1_1.click()
multi_grid1_2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[2]/label[2]/div/div/div[2]")
multi_grid1_2.click()
time.sleep(1)

multi_grid2_1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/label[1]/div/div/div[2]")
multi_grid2_1.click()
multi_grid2_2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[4]/label[3]/div/div")
multi_grid2_2.click()
time.sleep(1)

multi_grid3_1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/label[1]/div/div/div[2]")
multi_grid3_1.click()
multi_grid3_2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[6]/label[4]/div/div/div[2]")
multi_grid3_2.click()
time.sleep(1)

multi_grid4_1 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/label[1]/div/div/div[2]")
multi_grid4_1.click()
multi_grid4_2 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[8]/label[5]/div/div")
multi_grid4_2.click()
time.sleep(1)

nextBotton5 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]/span")
nextBotton5.click()
time.sleep(1)

nextBotton6 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
nextBotton6.click()
time.sleep(1)

nextBotton7 = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span")
nextBotton7.click()
time.sleep(1)

# upload_file = chr_driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[2]/span/span[2]")
# upload_file.click()
# time.sleep(5)

# put_file = chr_driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/div/div[1]")
# put_file.send_keys("D:\BeforeUpdate.png")