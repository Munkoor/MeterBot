import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authenticate_google_sheets():
    # Шлях до файлу з ключем API (завантажте файл JSON з консолі розробника Google)
    credentials = ServiceAccountCredentials.from_json_keyfile_name('personal-info.json',
                                                                   ['https://spreadsheets.google.com/feeds',
                                                                    'https://www.googleapis.com/auth/drive'])

    # Аутентифікація та отримання об'єкта екземпляра
    gc = gspread.authorize(credentials)

    # Ім'я таблиці (Змініть на своє)
    spreadsheet_name = 'personal info'

    # Відкриття таблиці
    sh = gc.open(spreadsheet_name)

    return sh.sheet1  # Повертає перший лист таблиці


def write_dictionary_to_sheet(dictionary):
    sheet = authenticate_google_sheets()

    last_row = len(sheet.get_all_values()) + 1

    for col, value in enumerate(dictionary.values(), 1):
        sheet.update_cell(last_row, col, value)
