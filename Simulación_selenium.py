#Imports necesarios
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class pruebaSauceDemo(unittest.TestCase):

    #Inicia el controlador de Microsoft Edge
    def setUp(self):
        edge_opciones = webdriver.EdgeOptions()
        edge_opciones.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Edge(options=edge_opciones)
        self.driver.get("https://www.saucedemo.com")

    def login(self, username, password):
        driver = self.driver
        driver.find_element(By.ID, "user-name").clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        
    #Caso de prueba 1
    def test_agrgar_producto_al_carrito(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        time.sleep(2)
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        self.assertEqual(cart_count.text, "1")

    #Caso de prueba 2
    def test_eliminar_producto_del_carrito(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
        time.sleep(2)
        driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(2)
    
    #Caso de prueba 3
    def test_proceso_de_compra(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        driver.find_element(By.ID, "checkout").click()
        time.sleep(2)
        driver.find_element(By.ID, "first-name").send_keys("Bryan")
        driver.find_element(By.ID, "last-name").send_keys("CH")
        driver.find_element(By.ID, "postal-code").send_keys("12345")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(2)
        driver.find_element(By.ID, "finish").click()
        time.sleep(2)
        confirmation_message = driver.find_element(By.CLASS_NAME, "complete-header").text
        self.assertEqual(confirmation_message, "Thank you for your order!")
        driver.find_element(By.ID, "back-to-products").click()
        time.sleep(3)
        
    #Caso de prueba 4
    def test_filtrar_productos(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='za']").click()
        time.sleep(2)
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='lohi']")
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='hilo']").click()
        time.sleep(2)
        sort_dropdown = driver.find_element(By.CLASS_NAME, "product_sort_container")
        sort_dropdown.click()
        sort_dropdown.find_element(By.XPATH, "//option[@value='az']")
        time.sleep(3)

    #Caso de prueba 5
    def test_navegar_por_la_pagina(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(2)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "reset_sidebar_link").click()
        time.sleep(2)
        driver.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(2)
        current_url = driver.current_url
        self.assertEqual(current_url, "https://saucelabs.com/")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        self.assertEqual(driver.current_url, "https://www.saucedemo.com/")
        self.login("standard_user", "secret_sauce")
        time.sleep(3)

    #Caso de prueba 6
    def test_logout(self):
        self.login("standard_user", "secret_sauce")
        time.sleep(3)
        driver = self.driver
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(2)
        driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(2)
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(2)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()
        
#Ejecuta los casos de prueba
if __name__ == "__main__":
    unittest.main()
