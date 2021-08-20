from selenium import webdriver

driver = webdriver.chrome(executable_path="D:/Source/Chrome/chromedriver.exe")
driver.maximize_window();

driver.get("http://localhost/form.php")