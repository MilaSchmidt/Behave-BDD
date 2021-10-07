from behave import *
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from features.funciones import Funciones_Globales

@given(u'Abriendo el navegador')
def step_impl(context):
    global driver, f
    context.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
    f = Funciones_Globales(context.driver)
    f.Navegar("https://demoqa.com/text-box", 2)

@when(u'Cargando el nombre del "{user}"')
def step_impl(context, user):
    print(u'STEP: When Cargando el nombre del usuario')
    f.Texto_Mixto("id", "userName", user, 1)

@then(u'Cargando su "{email}"')
def step_impl(context, email):
    print(u'STEP: Then Cargando su email')
    f.Texto_Mixto("id", "userEmail", email, 2)

@then(u'Cargando su nueva "{dir}"')
def step_impl(context, dir):
    f.Texto_Mixto("id", "currentAddress", dir, 2)
    context.driver.close()
