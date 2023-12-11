# Telegram Bot for Storing Addresses and Meter Readings
This project is a Telegram bot that assists users in storing addresses and meter readings in Google Sheets, as well as saving photos of meters in Google Drive.

## Installation and Setup
### 1) Create a Telegram bot:

- Reach out to BotFather on Telegram and create a new bot.
- Obtain the token for accessing the bot API. 
- 
### 2) Generate a Google API key:

- Create a project in Google Cloud Console.
- Enable Google Sheets and Google Drive APIs for your project.
- Create a service account and download the JSON file with the access key.
- Install dependencies: 
`$ pip install -r requirements.txt` 
- Configure the environment:

### 3) Create a .env file and add the following parameters:

`$ TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN`
`$ GOOGLE_DRIVE_TOKEN=GOOGLE_DRIVE_TOKEN`

### Usage
Start the Telegram bot and interact with it to store addresses and meter readings.
Upload meter photos to the bot, and they will be saved in Google Drive.
Access the stored data in Google Sheets for further analysis.
Feel free to customize and extend the functionality according to your specific needs.






