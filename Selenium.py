import tkinter as tk
import time
import pickle
import re
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By #By.CLASS bu olmadan undefined
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from tkinter.simpledialog import askstring
from selenium.webdriver.support.wait import WebDriverWait
