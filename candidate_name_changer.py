from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class CandidateNameChangerWindow(QDialog):
    def __init__(self, main_window):
        """
        Initialize the CandidateNameChangerWindow.
        """
        super(CandidateNameChangerWindow, self).__init__()

        # Initialize the CandidateNameChanger Window
        self.setWindowTitle("Change Candidate Names")
        self.setGeometry(200, 200, 400, 300)

        self.main_window = main_window

        self.layout = QVBoxLayout()

        self.instruction_label = QLabel("Please enter the names of the candidates you want:", self)
        self.layout.addWidget(self.instruction_label)

        self.name_labels = []
        self.name_inputs = []

        # Create input fields for candidate names
        for i in range(self.main_window.new_candidate_count):
            name_label = QLabel(f"Candidate {i + 1}:", self)
            name_input = QLineEdit(self)
            self.name_labels.append(name_label)
            self.name_inputs.append(name_input)

            self.layout.addWidget(name_label)
            self.layout.addWidget(name_input)

        self.save_button = QPushButton("SAVE", self)
        self.save_button.clicked.connect(self.save_changes)
        self.layout.addWidget(self.save_button)

        self.error_label = QLabel("", self)  # New label to display errors
        self.layout.addWidget(self.error_label)

        self.setLayout(self.layout)

    def save_changes(self):
        """
        Save changes based on entered names.
        """
        for i, input_field in enumerate(self.name_inputs):
            candidate_name = input_field.text().strip()

            # Validate candidate name
            if not candidate_name:
                self.error_label.setText("All candidates must be named.")
                return

            if any(char.isdigit() for char in candidate_name):
                self.error_label.setText("Only letters must be entered in the candidates' names.")
                return

            # Save the candidate names in the main window
            self.main_window.candidates[candidate_name] = 0

        self.error_label.clear()  # Clear any previous error message
        self.accept()  # Close the dialog and return QDialog.Accepted
