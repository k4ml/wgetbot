## Web Get Bot
Simple bot to fetch web page. Just to learn implementing Telegram Bot using polling
method. Turn out to be much simpler than using [webhook method][1] which require HTTPS endpoint.

## Get Started

```
virtualenv wgetbot
cd wgetbot
git clone https://github.com/k4ml/wgetbot.git
cd wgetbot
../bin/pip install -r requirements.txt
../bin/python main.py <BOT TOKEN>
```

## Usage

<img src="http://i.imgur.com/8e7e1g8.png"></img>

If the web page too large, Telegram refuse the message so you can specify
offset and length to pull out the text.

[1]:https://gist.github.com/k4ml/04867dc17389a1cfba45

## Stub
