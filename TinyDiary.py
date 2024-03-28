from datetime import datetime
import json
import os

from TinyDiaryArt import logos

current_month = datetime.now().month

logo = logos.get(current_month)

today = datetime.today().strftime("%m.%d.%Y")

def clear():
    '''Clears the terminal.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def load_diary_pages():
    '''Loads diary pages from the file.'''
    try:
        with open("TinyDiaryPages.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_diary_pages(diary_pages):
    '''Saves diary pages to the file.'''
    with open("TinyDiaryPages.json", "w") as file:
        json.dump(diary_pages, file)

def write_entry(diary_pages):
    '''Writes a journal entry.'''
    clear()
    print(logo)
    entry_date = input(f"If the entry is for today {today}, press enter.\n"
                       f"If the entry is for a previous date, enter the date (mm.dd.yyyy):\n") or today
    journal_entry = input("Please write 3-5 sentences describing your day:\n\n")
    diary_pages[entry_date] = journal_entry
    save_diary_pages(diary_pages)
    input("\nYour journal entry has been saved! Press enter to continue.")

def read_entry(diary_pages):
    '''Reads a journal entry.'''
    clear()
    print(logo)
    date_view = input("What date would you like to read?\nFormat your entry like mm.dd.yyyy:\n")
    if date_view in diary_pages:
        print(diary_pages[date_view])
    else:
        print("No entry found for this date. Please try again.")
    input("Press enter to continue.")

def still_journaling(diary_pages):
    '''Asks if the user wants to continue journaling.'''
    clear()
    print(logo)
    decision = input("Would you like to continue journaling (yes/no)?\n")
    return decision.lower() in {"yes", "y"}

def Tiny_Diary():
    '''Main function for the journaling application.'''
    diary_pages = load_diary_pages()
    while True:
        clear()
        print(logo)
        choice = input("Would you like to read or write?\n")
        if choice.lower() == "write": 
            write_entry(diary_pages)
        elif choice.lower() == "read":
            read_entry(diary_pages)
        else:
            print("Invalid choice.")
        if not still_journaling(diary_pages):
            print("Have a good day!")
            break

if __name__ == "__main__":
    Tiny_Diary()
