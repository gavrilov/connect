Connect: small service to send a direct message to a user telegram
==================================================================

Connect is an open-source app that allows you to send a message from a website directly to telegram.

Try the demo - send a message to me! 
`https://connectkonst.herokuapp.com/ <https://connectkonst.herokuapp.com/>`_

How to deploy with Heroku:
--------------------------
- Fork the repo
- Create a new Heroku app
- Connect app to GitHub repo in Deploy tab
- Add the following variables to Config Vars on the Setting tab:
   - SECRET_KEY
   - TELEGRAM_BOT_TOKEN
   - TELEGRAM_CHAT_ID
- Click "Open app"
- Done - you are handsome!