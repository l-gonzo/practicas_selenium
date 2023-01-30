from selenium import webdriver
import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
#direccion web
driver.get("http://localhost:3000/authenticate/login")

#login
driver.find_element(By.NAME, "email").send_keys("test@mail.com")
driver.find_element(By.NAME, "password").send_keys("test123")
driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg".replace(" ", ".")).click()
sleep(10)

print("Hizo login")

driver.find_element(By.CLASS_NAME, "m-auto justify-content-center".replace(" ", ".")).click()

print("entró al menu")

sleep(10)

#ir a nodo Antibody
driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div/div[2]/div/a[5]").click()
sleep(10)
print("entro a workflow 'antibody'")

#nodos tipo input
driver.find_element(By.XPATH, "/html/body/div/div/main/div[2]/div[4]/aside/details[1]/summary").click()
sleep(10)


print("desplegar menú input")

#Agarrar nodo
CASE1_node = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div.flexlayout__layout > div:nth-child(4) > aside > details:nth-child(3) > ol > li:nth-child(1) > div")
React_Flow = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div.flexlayout__layout > div:nth-child(7) > div > div > div.react-flow__renderer.react-flow__container > div.react-flow__pane.react-flow__container")

actions = ActionChains(driver)
actions.drag_and_drop(CASE1_node, React_Flow).perform()
"""
actions.click_and_hold(CASE1_node)
actions.release(React_Flow).perform()
"""
print("mover nodo")

sleep(5)

driver.refresh()

sleep(10)