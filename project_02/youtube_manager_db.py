import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_video():
    """Lists all videos with only name and time."""
    cursor.execute('SELECT name, time FROM videos')
    rows = cursor.fetchall()  # Fetch all rows

    if not rows:
        print("No videos found.")
    else:
        for name, time in rows:  # Correctly unpacking values
            print(f"Name: {name}, Time: {time}")

def add_video(name, time):
    """Adds a new video to the database."""
    cursor.execute('INSERT INTO videos (name, time) VALUES (?, ?)', (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    """Updates an existing video in the database."""
    cursor.execute('UPDATE videos SET name = ?, time = ? WHERE id = ?', (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    """Deletes a video from the database."""
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    """Main program loop."""
    while True:
        print("\nYouTube Manager App with DB")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_video()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            try:
                video_id = int(input("Enter video ID to update: "))
                name = input("Enter the new video name: ")
                time = input("Enter the new video time: ")
                update_video(video_id, name, time)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '4':
            try:
                video_id = int(input("Enter video ID to delete: "))
                delete_video(video_id)
            except ValueError:
                print("Invalid ID. Please enter a number.")
        elif choice == '5':
            print("Exiting application...")
            cursor.close()  # Close cursor before closing connection
            conn.close()
            break
        else:
            print("Invalid choice, please select a valid option.")

if __name__ == "__main__":
    main()
