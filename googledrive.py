from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def upload_photo(credentials_path, photo_path, photo_name, folder_id):
    creds = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    drive_service = build('drive', 'v3', credentials=creds)

    file_metadata = {
        'name': photo_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload(photo_path, mimetype='image/jpeg')

    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f'File ID: {file["id"]}')
    print(f'Photo {photo_name} uploaded successfully.')


# if __name__ == '__main__':
#     credentials_path = 'шлях/до/вашого/файлу.json'
#     photo_path = 'шлях/до/photo.jpg'
#     photo_name = 'photo.jpg'
#     folder_id = 'ID_вашої_папки'
#
#     upload_photo(credentials_path, photo_path, photo_name, folder_id)
