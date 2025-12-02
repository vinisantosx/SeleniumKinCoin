import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def get_path_with_file_name(filename: str) -> str:
    return os.getcwd() + filename


def configure_selenium() -> webdriver:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", False)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost:5174/")
    driver.maximize_window()
    return driver
    


# --------------------------
# 📌 TESTE 1 — Telefone inválido
# --------------------------
def test_telefone_invalido():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("João")
    driver.find_element(By.ID, "signup_telefone").send_keys("12345")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("teste@example.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@example.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "Telefone inválido!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 2 — CPF inválido
# --------------------------
def test_cpf_invalido():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("Maria")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("111.111.111-11")
    driver.find_element(By.ID, "signup_email").send_keys("email@email.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("email@email.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "CPF inválido!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 3 — Email inválido
# --------------------------
def test_email_invalido():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("Pedro")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("emailerrado")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("emailerrado")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "Formato de email inválido!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 4 — Emails não coincidem
# --------------------------
def test_double_check_email_incorreto():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("Pedro")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("a@a.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("b@b.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "Emails não coincidem!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 5 — Senha curta
# --------------------------
def test_senha_minima_invalida():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("Ana")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_password").send_keys("123")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("123")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "A senha deve conter no minimo 8 caracteres!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 6 — Senhas não coincidem
# --------------------------
def test_double_check_senha_incorreta():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("Lucas")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("email@email.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("email@email.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("87654321")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "Senhas não coincidem!"
    time.sleep(2)


# --------------------------
# 📌 TESTE 7 — Cadastro realizado com sucesso
# --------------------------
def test_cadastro_sucesso():
    driver = configure_selenium()
    driver.find_element(By.ID, "signUp").click()
    driver.find_element(By.ID, "signup_name").send_keys("João Silva")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    msg = driver.find_element(By.ID, "signupMessage").text
    assert msg == "Cadastro realizado com sucesso!"
    time.sleep(2)
