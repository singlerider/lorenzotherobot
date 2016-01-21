# -*- coding: utf-8 -*-

# channel/channel_year_month_day.txt

import json
import os
import time

from apiclient.discovery import build
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

with open("src/lib/date.txt", "w") as f:  # save current date when app starts
    f.write(time.strftime("%Y_%m_%d", time.gmtime()))


def get_credentials():  # Saves valid credentials and points the app to the
    # correct Google Drive account and folders
    # = the content (messages to save)
    """Gets valid user credentials from storage.
    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.
    Returns:
    Credentials, the obtained credential.
    """
    # from google API console - load credentials from file
    gauth = GoogleAuth()  # Object to hold authentication information
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("credentials.txt")
    if gauth.credentials is None:
        print "No creds file"
        # Authenticate if they're not there
        gauth.CommandLineAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("credentials.txt")
    return GoogleDrive(gauth)  # To be passed as needed


def get_log_files(previous_date):
    log_files = []  # Stores eligible log txt files
    path = "src/logs/{0}/".format(previous_date.rstrip("\n"))
    for log in os.listdir(path):  # For every file in daily folder
        if log.endswith(".txt"):  # Ignore any files that may have snuck in
            log_files.append("{0}{1}".format(path, log))
    print log_files  # For debugging
    return path, log_files


def create_logs_folder_in_root(drive):  # checks to see if a logs folder exists
    # in the Google Drive root folder. If it doesn't, make one, if it does,
    # return the id of the folder
    root_files = drive.ListFile(
        {'q': "'root' in parents and trashed=false"}
    ).GetList()
    logs_folder_id = ""
    if len([x["id"] for x in root_files if x["title"] == "logs"]) == 0:
        folder = drive.CreateFile(  # Will always save to the first result of
            # a folder named "logs" in the root
            {'title': "logs",  # Folders are treated as files with special type
                "mimeType": "application/vnd.google-apps.folder"})
        folder.Upload()  # Send it up!
        logs_folder_id = folder["id"]
        print "No logs folder found. Creating one now."
    else:
        logs_folder_id = [x["id"] for x in root_files if x[
            "title"] == "logs"][0]  # '0B-Hk6r8-bsihgjlqaTBTTFBKbWM'
    print "continuing with logs folder found at: {0}".format(logs_folder_id)
    return logs_folder_id  # To be used as a parent id for dependent functions


def create_folders(drive, logs_folder_id, previous_date):
    folders = {}  # Will store pre-existing folders on Google Drive
    folder_list = drive.ListFile(
        {'q': "'{0}' in parents and trashed=false".format(logs_folder_id)}
    ).GetList()
    for entry in folder_list:
        if entry["mimeType"] == "application/vnd.google-apps.folder":
            print "title: {0}, id: {1}, mimetype: {2}".format(
                entry['title'], entry['id'],
                entry["mimeType"])
            folders[entry["title"]] = entry["id"]  # channel = id
    print "folders", folders  # For debugging
    path = "src/logs/{0}/".format(previous_date.rstrip("\n"))
    try:
        for log in os.listdir(path):  # For every file in daily directory
            if log.endswith(".txt"):  # Only check plaintext files
                channel = log.rstrip(".txt")
                if channel not in folders:  # If it's a new folder
                    folder = drive.CreateFile(  # Make one on Google Drive
                        {'title': channel,
                            "parents": [{"id": logs_folder_id}],
                            "mimeType": "application/vnd.google-apps.folder"})
                    folder.Upload()  # Send it up!
                    print "Creating folder for {0}...".format(channel)
                    folders[channel] = folder["id"]
                    # {u'general': u'0B-Hk6r8-bsihgjlqaTBTTFBKbWM'}
    except Exception as error:
        print "No logs found for {0}".format(previous_date)
        return  # On exception, just exit the loop
    return folders  # Know the folders that already exist


def save_file_to_drive(drive, log, channel, data, folders, previous_date):
    title = "{0}_{1}.txt".format(channel, previous_date)
    log = drive.CreateFile({"title": title,
                            "parents": [{"id": folders[channel]}]
                            })
    log["title"] = title  # Change title of the file
    log.SetContentFile(  # File is empty until here
        "src/logs/{0}/{1}.txt".format(
            previous_date.rstrip("/n"), channel))
    log.Upload(param={"convert": True})  # Files.update()


def save_logs_to_drive(drive, previous_date, folders):
    path, log_files = get_log_files(previous_date)
    for log in log_files:
        channel = log.rstrip(".txt").split("/")[3]  # Gets channel name from
        # folder name
        filename = channel + ".txt"
        print "Saving log for {0}...".format(channel)
        with open("{0}{1}".format(path, filename), "r") as f:
            data = f.read()
            save_file_to_drive(
                drive, log, channel, data, folders, previous_date)
    print "All done. Backup complete"


def cron(channel):  # TODO remove this arg requirement.
    drive = get_credentials()
    with open("src/lib/date.txt", "r") as f:
        previous_date = f.read()
    current_date = time.strftime("%Y_%m_%d", time.gmtime())
    if current_date != previous_date:
        date_to_log = previous_date  # reassign this to a new variable
        with open("src/lib/date.txt", "w") as f:
            f.write(current_date)
        logs_folder_id = create_logs_folder_in_root(drive)
        folders = create_folders(drive, logs_folder_id, date_to_log)
        if folders is not None:
            save_logs_to_drive(drive, date_to_log, folders)  # save to drive
        return


if __name__ == "__main__":  # Run this file as python src/lib/save_to_drive.py
    # in order to test any saved message logs' ability to upload to drive
    with open("src/lib/date.txt", "r") as f:
        previous_date = f.read()
    drive = get_credentials()
    logs_folder_id = create_logs_folder_in_root(drive)
    folders = create_folders(drive, logs_folder_id, previous_date)
    if folders is not None:
        save_logs_to_drive(drive, previous_date, folders)
