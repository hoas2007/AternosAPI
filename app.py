from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    return '✅ API جاهزة للعمل - استخدم /start-server لتشغيل Aternos'

@app.route('/start-server')
def start_server():
    email = os.getenv("ATERNOS_EMAIL")
    password = os.getenv("ATERNOS_PASSWORD")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        driver = webdriver.Chrome(options=options)

        # تسجيل الدخول
        driver.get("https://aternos.org/accounts/")
        driver.find_element(By.ID, "user").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)
        driver.get("https://aternos.org/server/")
        time.sleep(5)

        # زر التشغيل
        start_button = driver.find_element(By.ID, 'start')
        start_button.click()

        driver.quit()
        return "✅ تم إرسال أمر تشغيل السيرفر على Aternos."
    
    except Exception as e:
        return f"❌ خطأ: {str(e)}"
