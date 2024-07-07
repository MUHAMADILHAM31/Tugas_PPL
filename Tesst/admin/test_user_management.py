from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Fungsi untuk melakukan pengujian manajemen pengguna
def test_user_management():
    # Inisialisasi WebDriver dengan Chrome
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
    driver.maximize_window()  # Maksimalkan jendela browser
    
    try:
        # Buka halaman manajemen pengguna (misalnya, admin panel)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        
        # Tunggu hingga halaman memuat sepenuhnya
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "element_id_or_css_selector")))
        
        # Lakukan operasi manajemen pengguna di sini
        # Contoh: Tambah pengguna baru
        # Misalnya, klik tombol "Add User"
        driver.find_element(By.ID, "btn_add_user").click()
        
        # Isi formulir tambah pengguna
        driver.find_element(By.ID, "username").send_keys("newuser")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "email").send_keys("newuser@example.com")
        
        # Klik tombol untuk menyimpan pengguna baru
        driver.find_element(By.ID, "btn_save_user").click()
        
        # Tunggu hingga pesan sukses atau validasi muncul
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "success_message")))
        
        # Verifikasi pesan sukses atau hasil operasi lainnya
        success_message = driver.find_element(By.ID, "success_message").text
        if "User added successfully" in success_message:
            print("User Management Test Passed")
        else:
            print("User Management Test Failed")
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
    
    finally:
        # Tutup browser setelah pengujian selesai
        driver.quit()

# Panggil fungsi untuk menjalankan pengujian manajemen pengguna
if __name__ == "__main__":
    test_user_management()
