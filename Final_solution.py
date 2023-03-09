import openai
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service


openai.api_key = "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"

def generate_response(prompt):
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].text.strip()

# Initialize Firefox driver with options
options = webdriver.FirefoxOptions()
driver_service = Service(executable_path=GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service, options=options)
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code to log in to WhatsApp web

def send_message(message):
    wait = WebDriverWait(driver, 20)
    chat_box = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]' )))
    chat_box.send_keys(message + Keys.ENTER)


while True:
    user_input = input('You: ')
    prompt = 'User: ' + user_input + '\nBot: '
    bot_response = generate_response(prompt)
    send_message(bot_response)

