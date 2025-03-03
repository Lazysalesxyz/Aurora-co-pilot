# Discord Bot Setup Instructions

To get your Discord bot working, you'll need to create a new bot application or update your existing "Aurora Co-Pilot" with a fresh token. Follow these steps:

## 1. Update Your Existing Bot Application

If you already have the "Aurora Co-Pilot" application set up in Discord Developer Portal:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Find and select your "Aurora Co-Pilot" application
3. In the left sidebar, click on "Bot"

## 2. Configure Bot Settings

1. Under the "Privileged Gateway Intents" section, ensure these are enabled:
   - Presence Intent
   - Server Members Intent
   - Message Content Intent (this is especially important)
   
2. Under "Bot Permissions", ensure these are enabled:
   - Read Messages/View Channels
   - Send Messages
   - Read Message History
   - Use Slash Commands
   - Add Reactions

## 3. Get a New Bot Token

1. Click the "Reset Token" button 
2. Confirm and copy the new token
3. Open your `.env` file in the project directory
4. Replace `YOUR_NEW_TOKEN_HERE` with the token you just copied

## 4. Invite the Bot to Your Server (if not already added)

1. In the left sidebar, click on "OAuth2" -> "URL Generator"
2. Under "Scopes", select "bot"
3. Under "Bot Permissions", select:
   - Read Messages/View Channels
   - Send Messages
   - Read Message History
   - Use Slash Commands
   - Add Reactions
4. Copy the generated URL at the bottom
5. Open this URL in your browser and select the server where you want to add the bot

## 5. Start the Bot

Run the bot with:
```
npm start
```

Your bot should now connect to Discord successfully!
