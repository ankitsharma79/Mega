import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
import time
from selenium.common.exceptions import TimeoutException

def aura():
    with open("config.json", "r") as f:
        config = json.load(f)

    roll_no = config.get("roll_no")
    password = config.get("password")

    if not roll_no or not password:
        return

    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = uc.Chrome(
        version_main=143,
        browser_executable_path="chrome.exe",
        options=options,
        headless=False
    )

    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://eyojan.srmu.ac.in/psc/ps/?cmd=login&languageCd=ENG")

        wait.until(EC.presence_of_element_located((By.ID, "userid"))).send_keys(roll_no)
        wait.until(EC.presence_of_element_located((By.ID, "pwd"))).send_keys(password)

        time.sleep(1)

        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "SubmitX"))).click()
        except TimeoutException:
            return

        driver.get(
            "https://eyojan.srmu.ac.in/psp/ps/EMPLOYEE/SA/c/SRM_STDNT_ATT_MNU.SRM_STDNT_AT_CMP.GBL"
        )

        try:
            wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "missing_iframe")))
        except TimeoutException:
            return

        wait.until(
            EC.presence_of_element_located((By.ID, "SRM_STDNT_L0_TB_RUN_CNTL_ID"))
        ).send_keys(roll_no[::-1])

        try:
            wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='#ICSearchX']"))
            ).click()
        except TimeoutException:
            return

        input2 = wait.until(
            EC.presence_of_element_located((By.ID, "SRM_STDNT_L0_TB_STRM"))
        )
        input2.clear()
        input2.send_keys("0000")

        try:
            wait.until(
                EC.element_to_be_clickable((By.ID, "SRM_STDNT_WRK_BUTTON1X"))
            ).click()
        except TimeoutException:
            return

        try:
            wait.until(
                EC.element_to_be_clickable((By.ID, "SRM_STDNT_ATT_PDFX"))
            ).click()
        except TimeoutException:
            pass

    finally:
        time.sleep(2)
        driver.quit()

if __name__ == "__main__":
    aura()
