# logic.py
class VoteSystem:
    candidates = {}

    @classmethod
    def initialize_candidates(cls, candidate_names):
        cls.candidates = {candidate: 0 for candidate in candidate_names}

    @classmethod
    def vote_for_candidate(cls, candidate):
        if candidate in cls.candidates:
            cls.candidates[candidate] += 1

    @classmethod
    def get_candidates(cls):
        return cls.candidates

    @classmethod
    def set_candidates(cls, candidate_names):
        # Set the candidate names with initial votes set to 0
        cls.candidates = {candidate: 0 for candidate in candidate_names}
