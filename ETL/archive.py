from pathlib import Path
from datetime import datetime
from shutil import move
from extract import extract_weather

def archive_file(file_path):
    # Ensure the archive directory exists
    archive_dir = Path("data/archive")
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Create a timestamped filename for the archived file
    timestamp = datetime.now().strftime("%Y%m%d%H%M")
    archived_file_name = f"{file_path.stem}_archived_at_{timestamp}{file_path.suffix}"
    archived_file_path = archive_dir / archived_file_name

    # Move the file to the archive directory
    move(file_path, archived_file_path)

    print(f"Archived {file_path} to {archived_file_path}")


if __name__ == "__main__":
    # Example usage
    file_path = extract_weather()
    archive_file(file_path)



