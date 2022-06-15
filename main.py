from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from helpers import email,password,faultyUserName,faultyUserEmail,faultyUserPhone, locationData ,roleData

print("hello")
print(email)

chrome_driver_path = r"C:\Users\eruiz\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://onelink.localhost:8080/")
#SELECT EMAIL FIELD TO POPULATE
emailElement = driver.find_element(By.ID , "email")
emailElement.click()


#RETRIVE AND INPUT EMAIL
userEmail = email
emailElement.send_keys(userEmail)

#SELECT PASSWORD FIELD TO POPULATE
passwordElement = driver.find_element(By.ID , "password")
passwordElement.click()
userPassword = password
passwordElement.send_keys(userPassword)

#SUBMIT FORM
passwordElement.send_keys(Keys.ENTER)

#FIRST FORM CHECK : ADMIN ADD USER FORM
adminTab = driver.find_element(By.ID , "tab-admin")
adminTab.click()

manageUsers = driver.find_element(By.LINK_TEXT , "Manage Users")
manageUsers.click()

newUserButton = driver.find_element(By.LINK_TEXT , "New User")
newUserButton.click()

#INPUT FORM DATA WITH SPECIAL CHARACTERS

nameInput = driver.find_element(By.ID , "name")
nameInput.click()
nameInput.send_keys(faultyUserName)

emailInput = driver.find_element(By.ID , "email")
emailInput.click()
emailInput.send_keys(faultyUserEmail)

phoneInput = driver.find_element(By.ID , "phone")
phoneInput.click()
phoneInput.send_keys(faultyUserPhone)

locationInputDropdown = driver.find_element(By.CLASS_NAME , "select2-selection__arrow")
locationInputDropdown.click()
locationSearch = driver.find_element(By.XPATH , "/html/body/span/span/span[1]/input")
locationSearch.click()
locationSearch.send_keys(locationData)
locationSearch.send_keys(Keys.ENTER)

roleInputDropdown = driver.find_element(By.XPATH , '//*[@id="select2-roles-container"]')
roleInputDropdown.click()
roleSearch = driver.find_element(By.XPATH , "/html/body/span/span/span[1]/input")
roleSearch.click()
roleSearch.send_keys(roleData)
roleSearch.send_keys(Keys.ENTER)

#SEND FORM WITH FAULTY DATA
saveUserButton = driver.find_element(By.XPATH , '//*[@id="user-editor"]/fieldset/input')
saveUserButton.click()



# driver.quit()
# driver = webdriver.ChromiumEdge(executable_path=chrome_driver_path)

#  import org.openqa.selenium.Webdriver;
# import org.openqa.selenium.chrome.ChromeDriver;
# public class ChromiumBrowser{
#    public static void main(String[] args) {
#       WebDriver driver = new ChromeDriver();
#       // chromedriver.exe path set
#       System.setProperty("webdriver.chrome.driver",
#          "C:\\Users\\ghs6kor\\Desktop\\Java\\chromedriver.exe");
#       String u = "https://www.tutorialspoint.com/index.htm";
#       driver.get(u);
#    }
# }