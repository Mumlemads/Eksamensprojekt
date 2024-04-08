import streamlit as st
from datetime import datetime

class BaseNote:
    def __init__(self, title, text, created_at):
        self.title = title
        self.text = text
        self.created_at = created_at

    def update_text(self, new_text):
        self.text = new_text

    def update_title(self, new_title):
        self.title = new_title



class ToDoNote(BaseNote):
    def __init__(self, title, text, created_at, due_date):
        super().__init__(title, text, created_at)
        self.due_date = due_date

    def update_due_date(self, new_due_date):
        self.due_date = new_due_date

class MeetingNote(BaseNote):
    def __init__(self, title, text, created_at, attendees):
        super().__init__(title, text, created_at)
        self.attendees = attendees

    def add_attendee(self, attendee):
        self.attendees.append(attendee)

    def remove_attendee(self, attendee):
        self.attendees.remove(attendee)


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note):
        self.notes.append(note)

    def update_note(self, note_idx, new_title, new_text):
        self.notes[note_idx].update_title(new_title)
        self.notes[note_idx].update_text(new_text)

    def delete_note(self, note_idx):
        del self.notes[note_idx]






class UI:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def create_note_ui(self):
        st.header("Create Note")
        title = st.text_input("Title:")
        text = st.text_area("Text:")
        if st.button("Save"):
            new_note = BaseNote(title=title, text=text, created_at=datetime.now())
            self.note_manager.add_note(new_note)
            st.success("Note saved successfully!")

    def list_notes_ui(self):
        st.header("List Notes")        
        for idx, note in enumerate(self.note_manager.notes):
            st.write(f"**{note.title}**")
            st.write(note.text)
            if st.button(f"Delete {note.title}"):
                self.note_manager.delete_note(idx)





class AdvancedUI(UI):
    def create_todo_ui(self):
        st.header("Create To-Do Note")
        title = st.text_input("Title:")
        text = st.text_area("Text:")
        due_date = st.date_input("Due Date:")
        if st.button("Save"):
            new_todo = ToDoNote(title=title, text=text, created_at=datetime.now(), due_date=due_date)
            self.note_manager.add_note(new_todo)
            st.success("To-Do Note saved successfully!")

    def create_meeting_ui(self):
        st.header("Create Meeting Note")
        title = st.text_input("Title:")
        text = st.text_area("Text:")
        attendees = st.text_input("Attendees (comma-separated):").split(",")
        if st.button("Save"):
            new_meeting = MeetingNote(title=title, text=text, created_at=datetime.now(), attendees=attendees)
            self.note_manager.add_note(new_meeting)
            st.success("Meeting Note saved successfully!")


def main():
    note_manager = NoteManager()
    ui = UI(note_manager)

    st.title("Notes App")
    menu_choice = st.sidebar.radio("Menu", ["Create Note", "List Notes"])

    if menu_choice == "Create Note":
        ui.create_note_ui()
    elif menu_choice == "List Notes":
        ui.list_notes_ui()

if __name__ == "__main__":
    main()

        