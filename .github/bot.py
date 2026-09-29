from telethon import TelegramClient
import asyncio
import os
import sys

# --- Environment Variables ---
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = int(os.environ.get("CHAT_ID"))

async def send_telegram_files(files):
    """
    Connects to Telegram and sends the specified files as a group message.
    """

    client = TelegramClient('bot_session', api_id=int(API_ID), api_hash=API_HASH)

    await client.start(bot_token=BOT_TOKEN)

    try:

        print("[+] Sending files as a group...")
        # Send the files together as an album/group
        await client.send_file(
            entity=CHAT_ID,
            file=files,
        )
        print("[+] Files sent successfully.")
    finally:
        await client.disconnect()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        # Get all file paths from command-line arguments
        apk_files = sys.argv[1:]
        print(f"[+] Found files to upload: {apk_files}")
        try:
            # Run the asynchronous function
            asyncio.run(send_telegram_files(apk_files))
        except Exception as e:
            print(f"[-] An error occurred: {e}")
    else:
        print("[-] No file paths provided as arguments.")