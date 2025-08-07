import csv
import os
from datetime import datetime
from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class ActionSaveContact(Action):
    def name(self):
        return "action_save_contact"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot("name") or "Неизвестно"
        phone = tracker.get_slot("phone") or "Не е подаден"
        email = tracker.get_slot("email") or "Не е подаден"
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_path = "contacts.csv"
        file_exists = os.path.isfile(file_path)

        with open(file_path, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Име", "Телефон", "Имейл", "Дата"])
            writer.writerow([name, phone, email, date])

        dispatcher.utter_message(response="utter_contact_saved")
        return []
