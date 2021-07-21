# -*- coding: utf-8 -*-

import platform
import time
from datetime import datetime

from pyvirtualdisplay import Display
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import BLL

# Main Program
if platform.system() == "Windows":
    driver = webdriver.Chrome(ChromeDriverManager().install())
elif platform.system() == "Linux":
    # Initalize virtual display for headless pi
    display = Display(visible=0, size=(800, 800))
    display.start()
    driver = webdriver.Chrome()

driver.get("https://info.bbdc.sg/members-login/")

BLL.LogicalFullSteps(driver)
# # Idie of 10 minutes (600 seconds) before attempting to get latest slot availbility
while True:
    print(
        "["
        + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        + "] "
        + "Snoozing for 600 seconds"
    )
    time.sleep(BLL.readJSON()["generalSettings"]["refreshTimeIntervalInSeconds"])
    print(
        "["
        + datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        + "] "
        + " Waking up from sleep"
    )
    BLL.reloadSessionsAvailbility(driver)