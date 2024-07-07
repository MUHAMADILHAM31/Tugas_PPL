from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Fungsi untuk melakukan pengujian login
def test_login():
    # Inisialisasi WebDriver dengan Chrome
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()  # Maksimalkan jendela browser
    
    try:
        # Buka halaman login OrangeHRM
        driver.get("https://opensource-demo.orangehrmlive.com/")
        
        # Tunggu hingga field username muncul
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "txtUsername")))
        
        # Masukkan username dan password
        driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        driver.find_element(By.ID, "txtPassword").send_keys("admin12")
        
        # Klik tombol Login
        driver.find_element(By.ID, "btnLogin").click()
        
        # Tunggu hingga dashboard muncul setelah login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "menu_dashboard_index")))
        
        # Verifikasi apakah login berhasil dengan memeriksa keberadaan elemen dashboard
        dashboard_element = driver.find_element(By.ID, "menu_dashboard_index")
        if dashboard_element.is_displayed():
            print("Login Test Passed")
        else:
            print("Login Test Failed")
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    
    finally:
        # Tutup browser setelah pengujian selesai
        driver.quit()

# Panggil fungsi untuk menjalankan pengujian login
if __name__ == "__main__":
    test_login()