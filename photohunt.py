import os
import exifread
from tkinter import filedialog, Tk
from colorama import Fore, init
from PIL.ExifTags import TAGS

init(autoreset=True)

languages = {
    "ru": {
        "logo": Fore.CYAN + "╔═══╗╔╗╔╗╔══╗╔════╗╔══╗╔╗╔╗╔╗╔╗╔╗─╔╗╔════╗\n"
                "║╔═╗║║║║║║╔╗║╚═╗╔═╝║╔╗║║║║║║║║║║╚═╝║╚═╗╔═╝\n"
                "║╚═╝║║╚╝║║║║║──║║──║║║║║╚╝║║║║║║╔╗─║──║║──\n"
                "║╔══╝║╔╗║║║║║──║║──║║║║║╔╗║║║║║║║╚╗║──║║──\n"
                "║║───║║║║║╚╝║──║║──║╚╝║║║║║║╚╝║║║─║║──║║──\n"
                "╚╝───╚╝╚╝╚══╝──╚╝──╚══╝╚╝╚╝╚══╝╚╝─╚╝──╚╝──\n",
        "developer": Fore.GREEN + "Разработчик - https://github.com/justoperator/\n",
        "menu": Fore.MAGENTA + "\n1. Язык\n2. Получить информацию\n3. Как использовать?\n4. Выход",
        "select_language": "\nВыберите язык:\n1. English\n2. Русский",
        "choose_option": "Выберите опцию: ",
        "get_info_menu": "\n1. Открыть по пути (рекомендуется для Termux)\n2. Открыть через проводник",
        "enter_path": "Введите путь к файлу: ",
        "file_not_found": Fore.RED + "Файл не найден. Попробуйте снова.",
        "loading": "Загрузка...",
        "exit": "\nНажмите 'Enter' для возврата в меню.",
        "exit_message": Fore.RED + "Выход из программы...",
        "instructions": Fore.CYAN + "\nИнструкция по использованию:\n"
                       "1. Выберите 'Получить информацию'.\n"
                       "2. Выберите способ загрузки фото: по пути или через проводник.\n"
                       "3. Инструмент извлечет и покажет метаданные из файла.\n"
                       "4. Нажмите 'Enter', чтобы вернуться в главное меню.",
    },
    "en": {
        "logo": Fore.CYAN + "╔═══╗╔╗╔╗╔══╗╔════╗╔══╗╔╗╔╗╔╗╔╗╔╗─╔╗╔════╗\n"
                "║╔═╗║║║║║║╔╗║╚═╗╔═╝║╔╗║║║║║║║║║║╚═╝║╚═╗╔═╝\n"
                "║╚═╝║║╚╝║║║║║──║║──║║║║║╚╝║║║║║║╔╗─║──║║──\n"
                "║╔══╝║╔╗║║║║║──║║──║║║║║╔╗║║║║║║║╚╗║──║║──\n"
                "║║───║║║║║╚╝║──║║──║╚╝║║║║║║╚╝║║║─║║──║║──\n"
                "╚╝───╚╝╚╝╚══╝──╚╝──╚══╝╚╝╚╝╚══╝╚╝─╚╝──╚╝──\n",
        "developer": Fore.GREEN + "Developer - https://github.com/justoperator/\n",
        "menu": Fore.MAGENTA + "\n1. Language\n2. Get info\n3. How to use?\n4. Exit",
        "select_language": "\nSelect a language:\n1. English\n2. Русский",
        "choose_option": "Choose an option: ",
        "get_info_menu": "\n1. Open by path (Recommended for Termux)\n2. Open by explorer",
        "enter_path": "Enter the file path: ",
        "file_not_found": Fore.RED + "File not found. Please try again.",
        "loading": "Loading...",
        "exit": "\nPress 'Enter' to return to the menu.",
        "exit_message": Fore.RED + "Exiting program...",
        "instructions": Fore.CYAN + "\nHow to use:\n"
                       "1. Select 'Get info'.\n"
                       "2. Choose how to open the image: by path or through explorer.\n"
                       "3. The tool will extract and display metadata from the file.\n"
                       "4. Press 'Enter' to return to the main menu.",
        }
    }

current_language = "en"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def choose_language():
    global current_language
    print(languages[current_language]["select_language"])
    choice = input(languages[current_language]["choose_option"])
    if choice == "1":
        current_language = "en"
    elif choice == "2":
        current_language = "ru"
    else:
        print(Fore.RED + "Invalid option")

def get_image_metadata(file_path, file_size_formatted=None, language='en'):
    try:
        with open(file_path, 'rb') as image_file:
            tags = exifread.process_file(image_file)
            print(Fore.YELLOW + "EXIF Data:")
            formatted_metadata = get_exif_data(file_path, file_size_formatted, language)
            print(formatted_metadata)
    except Exception as e:
        print(Fore.RED + f"Error processing file: {e}")

metadata_translations = {
    "FileName": {"en": "File Name: ", "ru": "Название файла: "},
    "FileSize": {"en": "File Size: ", "ru": "Размер файла: "},
    "ModifyDate": {"en": "File Modify Date: ", "ru": "Дата редактирования файла: "},
    "FileExtension": {"en": "File Extension: ", "ru": "Расширение файла: "},
    "MimeType": {"en": "MIME Type: ", "ru": "MIME тип: "},
    "ExifByteOrder": {"en": "Exif Byte Order: ", "ru": "Exif – Порядок байтов: "},
    "Copyright": {"en": "Copyright: ", "ru": "Авторское право: "},
    "ImageDescription": {"en": "Image Description: ", "ru": "Описание изображения: "},
    "Make": {"en": "Make: ", "ru": "Производитель: "},
    "Model": {"en": "Model: ", "ru": "Модель камеры: "},
    "Orientation": {"en": "Orientation: ", "ru": "Ориентация: "},
    "DateTimeOriginal": {"en": "Date Time Original: ", "ru": "Дата съёмки: "},
    "ColorSpace": {"en": "Color Space: ", "ru": "Цветовое пространство: "},
    "ExifVersion": {"en": "Exif Version: ", "ru": "Версия Exif: "},
    "FlashPixVersion": {"en": "Flashpix Version: ", "ru": "Версия Flashpix: "},
    "GPSImgDirection": {"en": "GPS Image Direction: ", "ru": "GPS – Ориентир направления камеры: "},
    "GPSImgDirectionRef": {"en": "GPS Image Direction Ref: ", "ru": "GPS – Направления камеры при съёмке: "},
    "XResolution": {"en": "X Resolution: ", "ru": "Разрешение по X: "},
    "YResolution": {"en": "Y Resolution: ", "ru": "Разрешение по Y: "},
    "ImageWidth": {"en": "Image Width: ", "ru": "Ширина изображения: "},
    "ImageHeight": {"en": "Image Height: ", "ru": "Высота изображения: "},
    "Aperture": {"en": "Aperture: ", "ru": "Диафрагменное число: "},
    "DateTimeDigitized": {"en": "Date Time Digitized: ", "ru": "Дата оцифровки: "},
    "FocalLength": {"en": "Focal Length: ", "ru": "Фокусное расстояние: "},
}


def format_file_size(size_in_bytes):
    if size_in_bytes < 1024:
        return f"{size_in_bytes} bytes"
    elif size_in_bytes < 1024 ** 2:
        return f"{size_in_bytes / 1024:.2f} KB"
    elif size_in_bytes < 1024 ** 3:
        return f"{size_in_bytes / (1024 ** 2):.2f} MB"
    elif size_in_bytes < 1024 ** 4:
        return f"{size_in_bytes / (1024 ** 3):.2f} GB"
    else:
        return f"{size_in_bytes / (1024 ** 4):.2f} TB"

def open_file_dialog():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    file_size_bytes = os.path.getsize(file_path)
    file_size_formatted = format_file_size(file_size_bytes)
    return file_path, file_size_formatted

def get_exif_data(file_path, file_size_formatted, language=choose_language):
    with open(file_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)

    metadata = {
        "FileName": file_path,
        "FileSize": file_size_formatted,
        "ModifyDate": tags.get('EXIF DateTime', 'N/A'),
        "FileExtension": file_path.split('.')[-1] if '.' in file_path else 'N/A',
        "Copyright": tags.get('EXIF ImageDescription', 'N/A'),
        "ImageDescription": tags.get('Image ImageDescription', 'N/A'),
        "Make": tags.get('Image Make', 'N/A'),
        "Model": tags.get('Image Model', 'N/A'),
        "Orientation": tags.get('Image Orientation', 'N/A'),
        "DateTimeOriginal": tags.get('EXIF DateTimeOriginal', 'N/A'),
        "ColorSpace": tags.get('EXIF ColorSpace', 'N/A'),
        "ExifVersion": tags.get('EXIF ExifVersion', 'N/A'),
        "FlashPixVersion": tags.get('EXIF FlashPixVersion', 'N/A'),
        "GPSImgDirection": tags.get('GPS GPSImgDirection', 'N/A'),
        "GPSImgDirectionRef": tags.get('GPS GPSImgDirectionRef', 'N/A'),
        "XResolution": tags.get('Image XResolution', 'N/A'),
        "YResolution": tags.get('Image YResolution', 'N/A'),
        "ImageWidth": tags.get('Image ImageWidth', 'N/A'),
        "ImageHeight": tags.get('Image ImageLength', 'N/A'),
        "Aperture": tags.get('EXIF ApertureValue', 'N/A'),
        "DateTimeDigitized": tags.get('EXIF DateTimeDigitized', 'N/A'),
        "FocalLength": tags.get('EXIF FocalLength', 'N/A'),
    }

    formatted_metadata = []
    for key, value in metadata.items():
        label = metadata_translations.get(key, {}).get(language, key)
        formatted_metadata.append(f"{label}{value}")

    return '\n'.join(formatted_metadata)

def get_info():
    print(languages[current_language]["get_info_menu"])
    choice = input(languages[current_language]["choose_option"])
    if choice == "1":
        file_path = input(languages[current_language]["enter_path"])
        if os.path.exists(file_path):
            file_size_formatted = format_file_size(os.path.getsize(file_path))
            get_image_metadata(file_path, file_size_formatted, language=current_language)
        else:
            print(Fore.RED + "File not found.")
    elif choice == "2":
        file_path, file_size_formatted = open_file_dialog()
        if file_path:
            get_image_metadata(file_path, file_size_formatted, language=current_language)
        else:
            print(Fore.RED + "No file selected or file path is invalid")
    else:
        print(Fore.RED + "Invalid option")


def main_menu():
    while True:
        clear_screen()
        print(languages[current_language]["logo"])
        print(languages[current_language]["developer"])
        print(languages[current_language]["menu"])
        choice = input(languages[current_language]["choose_option"])
        
        if choice == "1":
            choose_language()
        elif choice == "2":
            get_info()
        elif choice == "3":
            print(languages[current_language]["instructions"])
        elif choice == "4":
            print(languages[current_language]["exit_message"])
            break
        else:
            print(Fore.RED + "Invalid option")
        
        input(languages[current_language]["exit"])

if __name__ == "__main__":
    main_menu()
