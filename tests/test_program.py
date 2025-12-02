import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def configure_selenium() -> webdriver:
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(service=service, options=options)

    # 👉 URL da sua aplicação React (Vite)
    driver.get("http://localhost:5173/")
    driver.maximize_window()
    return driver


# ================================
# 0. Senha mínima
# ================================
def test_senha_minima_invalida():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com")

    # Senha menor que 8
    driver.find_element(By.ID, "signup_password").send_keys("1234567")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("1234567")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Password must contain at least 8 characters!"


# ================================
# 1. Telefone inválido
# ================================
def test_telefone_invalido():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 1234-5678")  # errado
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-09")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Invalid phone format!"


# ================================
# 2. CPF inválido
# ================================
def test_cpf_invalido():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("123.456.789-00")  # inválido
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Invalid CPF!"


# ================================
# 3. Email inválido
# ================================
def test_email_invalido():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste@com")  # inválido
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste@com")
    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Invalid email format!"


# ================================
# 4. Double Check Email incorreto
# ================================
def test_double_check_email_incorreto():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "signup_email").send_keys("teste@exemplo.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("errado@exemplo.com")

    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Emails do not match!"


# ================================
# 5. Double Check Senha incorreta
# ================================
def test_double_check_senha_incorreta():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Teste")
    driver.find_element(By.ID, "signup_telefone").send_keys("(11) 91234-5678")
    driver.find_element(By.ID, "signup_cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "signup_email").send_keys("teste@exemplo.com")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@exemplo.com")

    driver.find_element(By.ID, "signup_password").send_keys("87654321")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")  # errado

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Passwords do not match!"


# ================================
# 6. Cadastro com sucesso
# ================================
def test_cadastro_sucesso():
    driver = configure_selenium()
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "signup_name").send_keys("Nome Completo")
    driver.find_element(By.ID, "signup_telefone").send_keys("(75) 95544-4444")
    driver.find_element(By.ID, "signup_cpf").send_keys("210.830.180-19")
    driver.find_element(By.ID, "signup_email").send_keys("teste@teste.com.br")
    driver.find_element(By.ID, "signup_confirm_email").send_keys("teste@teste.com.br")

    driver.find_element(By.ID, "signup_password").send_keys("12345678")
    driver.find_element(By.ID, "signup_confirm_password").send_keys("12345678")

    driver.find_element(By.ID, "signup_button").click()

    message = wait.until(EC.visibility_of_element_located((By.ID, "signupMessage"))).text
    assert message == "Account created successfully!"
