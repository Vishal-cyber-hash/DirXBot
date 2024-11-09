import csv
import sqlite3
import os

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# Create a table for system commands if it doesn't exist already
cursor.execute("""
CREATE TABLE IF NOT EXISTS sys_command (
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100) UNIQUE, 
    path VARCHAR(1000)
)
""")

# Create a table for web commands if it doesn't exist already
cursor.execute("""
CREATE TABLE IF NOT EXISTS web_command (
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100) UNIQUE, 
    url VARCHAR(1000)
)
""")
# Create a table with the desired columns
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
               id integer primary key, 
               name VARCHAR(200), 
               mobile_no VARCHAR(255), 
               email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
desired_columns_indices = [0, 1]

# Read data from CSV and insert into SQLite table for the desired columns
with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        selected_data = [row[i] for i in desired_columns_indices]
        cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # List of websites with names and URLs
# websites = [
#     ("google", "https://www.google.com"),
#     ("youtube", "https://www.youtube.com"),
#     ("facebook", "https://www.facebook.com"),
#     ("twitter", "https://www.twitter.com"),
#     ("instagram", "https://www.instagram.com"),
#     ("linkedin", "https://www.linkedin.com"),
#     ("wikipedia", "https://www.wikipedia.org"),
#     ("amazon", "https://www.amazon.com"),
#     ("reddit", "https://www.reddit.com"),
#     ("netflix", "https://www.netflix.com"),
#     ("whatsapp", "https://web.whatsapp.com"),
#     ("canva", "https://www.canva.com"),
#     ("pinterest", "https://www.pinterest.com"),
#     ("yahoo", "https://www.yahoo.com"),
#     ("bing", "https://www.bing.com"),
#     ("ebay", "https://www.ebay.com"),
#     ("quora", "https://www.quora.com"),
#     ("tiktok", "https://www.tiktok.com"),
#     ("dropbox", "https://www.dropbox.com"),
#     ("zoom", "https://www.zoom.us"),
#     ("spotify", "https://www.spotify.com"),
#     ("medium", "https://www.medium.com"),
#     ("apple", "https://www.apple.com"),
#     ("microsoft", "https://www.microsoft.com"),
#     ("nytimes", "https://www.nytimes.com"),
#     ("bbc", "https://www.bbc.com"),
#     ("cnn", "https://www.cnn.com"),
#     ("forbes", "https://www.forbes.com"),
#     ("weather", "https://www.weather.com"),
#     ("booking", "https://www.booking.com"),
#     ("airbnb", "https://www.airbnb.com"),
#     ("tripadvisor", "https://www.tripadvisor.com"),
#     ("yelp", "https://www.yelp.com"),
#     ("adobe", "https://www.adobe.com"),
#     ("github", "https://www.github.com"),
#     ("stackoverflow", "https://www.stackoverflow.com"),
#     ("gitlab", "https://www.gitlab.com"),
#     ("bitbucket", "https://www.bitbucket.org"),
#     ("digitalocean", "https://www.digitalocean.com"),
#     ("heroku", "https://www.heroku.com"),
#     ("cloudflare", "https://www.cloudflare.com"),
#     ("hulu", "https://www.hulu.com"),
#     ("vimeo", "https://www.vimeo.com"),
#     ("dailymotion", "https://www.dailymotion.com"),
#     ("twitch", "https://www.twitch.tv"),
#     ("soundcloud", "https://www.soundcloud.com"),
#     ("patreon", "https://www.patreon.com"),
#     ("kickstarter", "https://www.kickstarter.com"),
#     ("discord", "https://www.discord.com"),
#     ("slack", "https://www.slack.com"),
#     ("trello", "https://www.trello.com"),
#     ("asana", "https://www.asana.com"),
#     ("notion", "https://www.notion.so"),
#     ("udemy", "https://www.udemy.com"),
#     ("coursera", "https://www.coursera.org"),
#     ("edx", "https://www.edx.org"),
#     ("khanacademy", "https://www.khanacademy.org"),
#     ("udacity", "https://www.udacity.com"),
#     ("devto", "https://www.dev.to"),
#     ("producthunt", "https://www.producthunt.com"),
#     ("dribbble", "https://www.dribbble.com"),
#     ("behance", "https://www.behance.net"),
#     ("9gag", "https://www.9gag.com"),
#     ("imdb", "https://www.imdb.com"),
#     ("rottentomatoes", "https://www.rottentomatoes.com"),
#     ("goodreads", "https://www.goodreads.com"),
#     ("archive", "https://www.archive.org"),
#     ("wordpress", "https://www.wordpress.com"),
#     ("wix", "https://www.wix.com"),
#     ("shopify", "https://www.shopify.com"),
#     ("etsy", "https://www.etsy.com"),
#     ("alibaba", "https://www.alibaba.com"),
#     ("jd", "https://www.jd.com"),
#     ("target", "https://www.target.com"),
#     ("bestbuy", "https://www.bestbuy.com"),
#     ("zillow", "https://www.zillow.com"),
#     ("realtor", "https://www.realtor.com"),
#     ("craigslist", "https://www.craigslist.org"),
#     ("indeed", "https://www.indeed.com"),
#     ("glassdoor", "https://www.glassdoor.com"),
#     ("monster", "https://www.monster.com"),
#     ("basecamp", "https://www.basecamp.com"),
#     ("jira", "https://www.atlassian.com/software/jira"),
#     ("mailchimp", "https://www.mailchimp.com"),
#     ("constantcontact", "https://www.constantcontact.com"),
#     ("onedrive", "https://www.onedrive.com"),
#     ("google-drive", "https://www.google.com/drive"),
#     ("box", "https://www.box.com"),
#     ("mega", "https://mega.nz"),
#     ("icloud", "https://www.icloud.com"),
#     ("skype", "https://www.skype.com"),
#     ("webex", "https://www.webex.com")
# ]


# Insert each website into the web_command table
# for name, url in websites:
#     try:
#         cursor.execute(
#             "INSERT OR IGNORE INTO web_command (name, url) VALUES (?, ?)",
#             (name.lower(), url)
#         )
#     except sqlite3.IntegrityError:
#         print(f"Skipping duplicate entry for {name}")

# # Specify the location of the Start Menu Programs (for Windows)
# programs_dir = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs"

# Iterate over all files in the given directory and its subdirectories
# for root, dirs, files in os.walk(programs_dir):
#     for file in files:
#         # Check if the file is an executable or a shortcut (.lnk or .exe)
#         if file.endswith(".exe") or file.endswith(".lnk"):
#             # Get the full path of the file
#             full_path = os.path.join(root, file)
            
#             # Get the application name (without extension)
#             name = os.path.splitext(file)[0]

#             # Insert into the sys_command table, using NULL for the auto-increment id
#             try:
#                 cursor.execute(
#                     "INSERT OR IGNORE INTO sys_command (name, path) VALUES (?, ?)",
#                     (name.lower(), full_path)
#                 )
#             except sqlite3.IntegrityError:
#                 print(f"Skipping duplicate entry for {name}")

# # Commit the changes to the database
conn.commit()

print("Web domains and system commands have been added to the database.")

# Close the connection
conn.close()
