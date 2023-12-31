from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QRadioButton, QPushButton
from PyQt6.QtCore import pyqtSignal

class CandidateVoterWindow(QDialog):
    """
    Window for casting votes for candidates.
    """
    vote_completed = pyqtSignal(str)

    def __init__(self, main_window):
        """
        Initialize the CandidateVoter Window.
        """
        super(CandidateVoterWindow, self).__init__()

        # Initialize the CandidateVoter Window
        self.setWindowTitle("Candidate Voter")
        self.setGeometry(200, 200, 400, 300)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Who do you want to vote for?", self)
        self.layout.addWidget(self.instruction_label)

        self.radio_buttons = []
        for candidate, votes in self.main_window.candidates.items():
            radio_button = QRadioButton(str(candidate), self)
            self.radio_buttons.append(radio_button)
            self.layout.addWidget(radio_button)

        self.vote_button = QPushButton("VOTE", self)
        self.vote_button.clicked.connect(self.vote)
        self.layout.addWidget(self.vote_button)

        self.result_label = QLabel("", self)  # Added QLabel for displaying results
        self.layout.addWidget(self.result_label)

        self.back_button = QPushButton("Back", self)  # Added Back button
        self.back_button.clicked.connect(self.close_and_show_main_window)
        self.layout.addWidget(self.back_button)

        self.setLayout(self.layout)

    def vote(self):
        """
        Cast a vote for the selected candidate.
        """
        selected_candidate = None
        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                selected_candidate = radio_button.text()
                break

        if selected_candidate:
            # Check if the selected candidate exists in the dictionary
            if selected_candidate in self.main_window.candidates:
                # Increment the vote count for the selected candidate
                self.main_window.candidates[selected_candidate] += 1

                # Display the result in the window itself
                self.result_label.setText(f"You voted for {selected_candidate}.")

            else:
                self.result_label.setText(f"Error: {selected_candidate} not found in candidates.")

        else:
            self.result_label.setText("A candidate must be voted.")

    def back_clicked(self):
        """Handle the Back button click."""
        self.reject()  # Close the dialog with QDialog.Rejected

    def get_selected_candidate(self):
        """
        Get the selected candidate.
        """
        for radio_button in self.radio_buttons:
            if radio_button.isChecked():
                return radio_button.text()
        return None

    def close_and_show_main_window(self):
        """
        Close the current window and show the main window.
        """
        self.accept()
        self.main_window.show()
