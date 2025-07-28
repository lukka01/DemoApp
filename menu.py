from diarybook import DiaryBook
import utils
import sys


class Menu:
    def __init__(self):
        self.diarybook = DiaryBook()
        self.choices = {
            "1.": self.show_all_diaries,
            "2.": self.add_diary,
            "3.": self.search_diaries,
            "4.": self.populate_database,
            "5.": self.quit
        }

    def show_all_diaries(self):
        if len(self.diarybook.diaries) == 0:
            print("There are no diaries.")
        else:
            for diary in self.diarybook.diaries:
                print(f"{diary.id} - {diary.memo} (Tags: {diary.tags})")

    def create_account(self):
        name = input("Enter your name: ")
        if name in self.users:
            print("An account with this name already exists.")
            return
        password = input("Enter your password: ")
        self.users[name] = password
        print(f"Account created for user '{name}'.")

    def sort_by_id(self):
        self.diaries.sort(key=lambda d: d.id)

    def sort_by_memo(self):
        self.diaries.sort(key=lambda d: d.memo.lower())

    def add_diary(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags (optional): ")
        self.diarybook.new_diary(memo, tags)
        print("Your note has been added successfully.")

    def search_diaries(self):
        keyword = input("Enter a keyword: ")
        filtered_diaries = self.diarybook.search_diary(keyword)
        if len(filtered_diaries) == 0:
            print("We couldn't find any diary matching the given keyword.")
        else:
            for diary in filtered_diaries:
                print(f"{diary.id} - {diary.memo} (Tags: {diary.tags})")

    def populate_database(self):
        diaries = utils.read_from_json_into_app("data.json")
        for diary in diaries:
            self.diarybook.diaries.append(diary)
        print(f"{len(diaries)} diary entries loaded from data.json.")

    def quit(self):
        print("Thanks for using DiaryBook! Goodbye.")
        sys.exit(0)

    def display_menu(self):
        print("""
DiaryBook Menu:
  1. Show all diaries
  2. Add diary
  3. Search with keyword
  4. Populate diarybook from file
  5. Quit
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} is not a valid choice.")


if __name__ == "__main__":
    Menu().run()




