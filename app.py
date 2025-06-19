from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/start-server', methods=['GET'])
def start_server():
    try:
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

        driver.get("https://aternos.org/accounts/")
        driver.find_element(By.ID, "user").send_keys("بريدك")
        driver.find_element(By.ID, "password").send_keys("كلمة_المرور")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)
        driver.get("https://aternos.org/server/")
        time.sleep(5)

        start_button = driver.find_element(By.ID, 'start')
        start_button.click()

        driver.quit()
        return "✅ تم إرسال أمر التشغيل إلى Aternos."

    except Exception as e:
        print(e)
        return f"❌ حدث خطأ: {e}"
