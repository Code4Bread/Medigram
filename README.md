# Medigram 
_Build 1.0_

## **Setup Instructions**
---
#### Install Dependencies

`cd {Medigram directory folder}`

_For Pip2_
`pip install -r requirements.txt`

_For Pip3_
`pip3 install -r requirements.txt`

#### Configure Script for your TelegramBOT

Search for `send_update` Function in `pipeline.py`

`bot = telegram.Bot("{TOKEN}")`
Replace `{TOKEN}` with your Bot Auth Token

`bot.send_message('{Reply_ID}',...`
Replace `{Reply_ID}` with your Chat ID

#### Change The Source of the Feed

Search for `get_update` Function in `pipeline.py`
`url = 'https://medium.com/feed/@{USERID}'`


#### Change Interval of the Update

Search for `get_updateInterval` Function in `pipeline.py`

`schedule.every(5).minutes.do(getUpdate)`
Change as you prefer

##### _To Read More About_ <a href="https://github.com/dbader/schedule">Schedule Module</a>

#### Running the script

Run `medigram.py` file.

## **Features**
---
* **Fetch Articles from Specific Medium User Feed & Store in Sqlite Database**

* **Get update on User Posts with invterval and send new posts to Telegram user through Desired Telegram Bot**

