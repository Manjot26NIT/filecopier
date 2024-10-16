This Python script is designed to detect newly connected drives on a Windows system and copy files with a specified extension from those drives to a specified directory. The script continuously monitors for drive changes and performs the copy operation when a new drive is detected.

How It Works
Argument Parsing: The script uses the argparse module to parse command-line arguments for the source directory path and the file extension to be copied.

path: The directory where files will be copied to.
extension: The file extension of the files to be copied.
Drive Detection: The script detects all available drives on the system using the os.path.exists method and stores them in a list.

Drive Change Detection: The script continuously monitors for changes in the list of available drives:

If a drive is removed, it prints the removed drive.
If a new drive is detected, it prints the drive details and its disk usage statistics.
File Copying: When a new drive is detected, the script:

Walks through the directory structure of the new drive.
Copies files with the specified extension to the target directory.
Performance Measurement: The script measures and prints the time taken to copy the files.