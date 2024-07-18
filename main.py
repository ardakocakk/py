import pyautogui
import keyboard

# Başlangıç ve bitiş koordinatları
start_x = 450
start_y = 350
end_x = 650
end_y = 500

# Her kaç pikselde bir sol click yapılacağı
click_interval = 10

# İşlemi durdurmak için bir flag
stop_flag = False

def on_caps_lock_press(event):
    global stop_flag
    stop_flag = True

# Caps Lock tuşuna basıldığında on_caps_lock_press fonksiyonunu çağır
keyboard.on_press_key("caps lock", on_caps_lock_press)

# Fareyi her pikselde hareket ettirip belirli aralıklarla sol click basılı tut
pyautogui.moveTo(start_x, start_y)
pyautogui.mouseDown()  # İlk başta sol click basılı tut

for y in range(start_y, end_y + 1, click_interval):
    for x in range(start_x, end_x + 1, click_interval):
        if stop_flag:
            print("İşlem durduruldu.")
            break
        pyautogui.moveTo(x, y)
    if stop_flag:
        break

for x in range(start_x, end_x + 1, click_interval):
    for y in range(start_y, end_y + 1, click_interval):
        if stop_flag:
            print("İşlem durduruldu.")
            break
        pyautogui.moveTo(x+5, y+5)
    if stop_flag:
        break



# Fareyi bırak
pyautogui.mouseUp()

print("Çizim tamamlandı.")