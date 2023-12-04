class VoteSystem:
    # Class to manage candidate information
    candidates = []
    num_candidates = 0

    @classmethod
    def set_candidates(cls, candidate_names):
        # Set the candidate names
        cls.candidates = candidate_names

    @classmethod
    def get_candidates(cls):
        # Get the candidate names
        return cls.candidates

    @classmethod
    def set_num_candidates(cls, num_candidates):
        # Set the number of candidates
        cls.num_candidates = num_candidates

    @classmethod
    def get_num_candidates(cls):
        # Get the number of candidates
        return cls.num_candidates

    @classmethod
    def save_candidate_names(cls, candidate_names):
        # Save the candidate names
        cls.set_candidates(candidate_names)

    @classmethod
    def save_num_candidates(cls, num_candidates):
        # Save the number of candidates
        cls.set_num_candidates(num_candidates)
