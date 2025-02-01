class ErrorAnalyzer:
    def __init__(self):
        self.error_weights = {
            'spelling': 0.3,
            'grammar': 0.4,
            'punctuation': 0.3
        }
    
    def grade_text(self, errors):
        total_score = 100
        for error in errors:
            weight = self.error_weights[error.type]
            total_score -= (error.severity * weight)
        return max(0, total_score)
