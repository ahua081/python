from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QSpinBox, QPushButton

class CandidateNumberChangerWindow(QDialog):
    def __init__(self, main_window):
        super(CandidateNumberChangerWindow, self).__init__()

        self.setWindowTitle("Change Number of Candidates")
        self.setGeometry(200, 200, 300, 200)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Please enter the number of candidates you want:", self)
        self.layout.addWidget(self.instruction_label)

        self.candidate_spin_box = QSpinBox(self)
        self.layout.addWidget(self.candidate_spin_box)

        self.error_label = QLabel("", self)  # New label to display errors
        self.layout.addWidget(self.error_label)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def save_changes(self):
        # Implement saving changes based on entered number of candidates
        new_candidate_count: int = self.candidate_spin_box.value()

        if new_candidate_count <= 1:
            self.error_label.setText("2 or more candidates are required.")
            return

        # Update the main window with the new candidate count
        self.main_window.candidates = {}  # Reset the candidate data
        self.main_window.new_candidate_count = int(new_candidate_count)
        # self.main_window.candidates.update({f"Candidate {i + 1}": f"Name {i + 1}" for i in range(new_candidate_count)})

        self.error_label.clear()  # Clear any previous error message
        self.accept()  # Close the dialog and return QDialog.Accepted
