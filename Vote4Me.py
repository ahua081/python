import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QMessageBox, QDialog
from PyQt6.QtCore import Qt
from PyQt6 import uic
from candidate_name_changer import CandidateNameChangerWindow
from candidate_number_changer import CandidateNumberChangerWindow
from candidate_voter import CandidateVoterWindow


class Vote4MeWindow(QMainWindow):
    def __init__(self):
        super(Vote4MeWindow, self).__init__()

        # Initialize the main window
        self.setWindowTitle("VOTE 4 ME")
        self.setGeometry(100, 100, 400, 300)

        # Set up the central widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        #Create and add widgets to the layout
        self.title_label = QTextEdit("VOTE 4 ME", self)
        self.title_label.setReadOnly(True)
        self.layout.addWidget(self.title_label)

        self.message_label = QTextEdit("Welcome to Vote 4 Me, please choose one of the buttons below.", self)
        self.message_label.setReadOnly(True)
        self.layout.addWidget(self.message_label)

        self.vote_button = QPushButton("Vote For Candidate", self)
        self.exit_button = QPushButton("Exit", self)
        self.change_candidates_button = QPushButton("Change Number of Candidates", self)
        self.change_names_button = QPushButton("Change Candidate Names", self)

        self.layout.addWidget(self.vote_button)
        self.layout.addWidget(self.exit_button)
        self.layout.addWidget(self.change_candidates_button)
        self.layout.addWidget(self.change_names_button)

        # Connect button clicks to corresponding methods
        self.vote_button.clicked.connect(self.open_voter_window)
        self.exit_button.clicked.connect(self.exit_program)
        self.change_candidates_button.clicked.connect(self.open_number_changer_window)
        self.change_names_button.clicked.connect(self.open_name_changer_window)

        # Set up the layout for the central widget
        self.central_widget.setLayout(self.layout)

        # Dictionary to store candidate names and votes
        self.candidates = {}
        self.number_of_candidates = 0
        self.new_candidate_count = 0

    def open_voter_window(self):
        # Open the CandidateVoter Window
        voter_window = CandidateVoterWindow(self)
        if voter_window.exec() == QDialog.Accepted:
            self.show()

    def open_number_changer_window(self):
        # Open the CandidateNumberChanger Window
        number_changer_window = CandidateNumberChangerWindow(self)
        number_changer_window.exec()

    def open_name_changer_window(self):
        # Open the CandidateNameChanger Window
        name_changer_window = CandidateNameChangerWindow(self)
        name_changer_window.exec()

    def exit_program(self):
        # Generate and display a summary when exiting the program
        summary_text = self.generate_summary()
        self.message_label.setPlainText(summary_text)

    # def generate_summary(self):
    #     # Generate a summary of the votes
    #     summary_text = "Summary:\n"
    #     for candidate, votes in self.candidates.items():
    #         summary_text += f"{candidate}: {votes} votes\n"
    #     total_votes = sum(self.candidates.values())
    #     summary_text += f"\nTotal: {total_votes} votes"
    #     return summary_text

    def update_summary(self):
        summary_text = self.generate_summary()
        self.message_label.setPlainText(summary_text)

if __name__ == "__main__":
    app = QApplication([])
    main_window = Vote4MeWindow()
    main_window.show()
    app.exec()
