from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager

#Please download the latest chrome wedriver from this trusted chromium source
#    https://chromedriver.chromium.org/downloads
#and extract the chromedriver.exe file path
#as the parameter in command given below
chromedriver_autoinstaller.install()

a = chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-insecure-localhost') # differ on driver version. can ignore. 

caps = options.to_capabilities()
caps["acceptInsecureCerts"] = True

driver = webdriver.Chrome(executable_path = a, options=options, desired_capabilities=caps)
#print(driver.getCapabilities().getCapability("chrome"))


driver.get("https://web.whatsapp.com/")
driver.minimize_window()
wait = WebDriverWait(driver, 600)

# Type in the name of your chat or
# group in target placeholder below
target = input(r'''Type usernames/group names of all receivers
separated by ';' in a single line below:
''')

target = target.replace('; ', ';').split(';')

print(target)

#######################################################################################################################################


# Replace the below string with your own message
string = input('Type ur message: ')

for i in range(0, len(target)):
    target[i] = '"'+(target[i])+'"'

msgcount = (input('Please enter no. of msgs to send: '))

if msgcount == '':
    msgcount = 1
else:
    msgcount = int(msgcount)

print()

for i in target:

    x_arg = '//span[contains(@title,' + i + ')]'

    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    print ("Wait for few seconds")
    group_title.click()

    for i in range(0, msgcount):
        try:
            message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
            message.send_keys(string)

            sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
            sendbutton.click()
        except:
            pass
        print('Sent', i+1, 'of', msgcount)

    
print('\nAll message(s) were succesfully sent to all receiver(s)')


driver.quit()
