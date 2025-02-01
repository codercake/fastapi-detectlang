def grade_text(validation_results):
    return {
        "overall_score": calculate_score(validation_results),
        "breakdown": {
            "grammar": 8.5,
            "spelling": 9.0,
            "structure": 7.5
        }
    }
