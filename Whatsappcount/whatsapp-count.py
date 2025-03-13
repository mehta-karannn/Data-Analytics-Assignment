import re
from collections import defaultdict

def count_whatsapp_messages(file_path):
    total_messages = 0
    photo_count = 0
    video_count = 0
    seen_count = 0
    unseen_count = 0
    text_message_count = 0
    date_messages = defaultdict(int)  # To store message count per date
    first_date, last_date = None, None

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Extract date using regex
            match = re.match(r'^(\d{1,2}/\d{1,2}/\d{2,4})', line)
            if not match:
                continue  # Skip lines that are not messages

            date = match.group(1)  # Extract the date
            date_messages[date] += 1  # Count messages per date
            total_messages += 1  # Count total messages

            if first_date is None:
                first_date = date  # Set first message date
            last_date = date  # Update last message date

            # Categorize messages
            if '[Photo]' in line:
                photo_count += 1
            elif '[Video]' in line:
                video_count += 1
            elif 'Seen' in line:
                seen_count += 1
            elif 'Unseen' in line:
                unseen_count += 1
            else:
                text_message_count += 1

    # Find the date with the most messages
    max_messages_date = max(date_messages, key=date_messages.get)
    max_messages_count = date_messages[max_messages_date]

    # Print statistics
    print(f"Chat Data From: {first_date} to {last_date}")
    print(f"Total Messages: {total_messages}")
    print(f"Text Messages: {text_message_count}")
    print(f"Photos Sent: {photo_count}")
    print(f"Videos Sent: {video_count}")
    print(f"Seen Messages: {seen_count}")
    print(f"Unseen Messages: {unseen_count}")
    print(f"Highest Messages on: {max_messages_date} ({max_messages_count} messages)")

   

# Run the function with your exported chat file
count_whatsapp_messages(r"C:\Users\karan\Desktop\Karan\WhatsApp Chat with Tanvi Chiman\WhatsApp Chat with Tanvi Chiman.txt")
