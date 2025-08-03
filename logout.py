from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# configurações do navegador
options = webdriver.ChromeOptions()
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'username'))
    )

    driver.find_element(By.NAME, 'username').send_keys('Admin')

    driver.find_element(By.NAME, 'password').send_keys('admin123')

    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//p[@class="oxd-userdropdown-name"]'))
    )

    driver.find_element(By.XPATH, '//p[@class="oxd-userdropdown-name"]').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[text()="Logout"]'))
    )

    driver.find_element(By.XPATH, '//a[text()="Logout"]').click()

    print("Login e logout realizados com sucesso.")

except (TimeoutException, NoSuchElementException) as e:
    print(f"Erro: {e}")

finally:
    driver.quit()