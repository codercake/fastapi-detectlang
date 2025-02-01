from indicnlp.tokenize import sentence_tokenize
from indicnlp.morph import morph_analyzer

class LanguageProcessor:
    def __init__(self, language):
        self.morph = morph_analyzer.MorphAnalyzer(language)
        self.grammar_rules = self.load_grammar_rules(language)
    
    def analyze_text(self, text):
        tokens = sentence_tokenize.sentence_split(text, lang='mar')
        errors = []
        for token in tokens:
            analysis = self.morph.analyze(token)
            errors.extend(self.check_grammar_rules(analysis))
        return errors
