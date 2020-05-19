from .distractor_models import *

tense_choice_init_params = {'spacy_model_name': 'en_core_web_sm'}

prepositions_init_params = {'spacy_model_name': 'en_core_web_sm',
                            'question_vocab_dir': 'preps_question_vocab', 'answer_vocab_dir': 'preps_answer_vocab',
                            'nn_weights_path': 'model_weights/preps_model', 'right_answer_col': 'Right answer'}

verb_lex_choice_init_params = {'spacy_model_name': 'en_core_web_sm',
                               'question_vocab_dir': 'verbs_question_vocab', 'answer_vocab_dir': 'verbs_answer_vocab',
                               'nn_weights_path': 'model_weights/verbs_lex_model', 'right_answer_col': 'Right answer lemma'}

noun_lex_choice_init_params = {'spacy_model_name': 'en_core_web_sm',
                               'question_vocab_dir': 'nouns_question_vocab', 'answer_vocab_dir': 'nouns_answer_vocab',
                               'nn_weights_path': 'model_weights/nouns_lex_model', 'right_answer_col': 'Right answer lemma'}

adj_lex_choice_init_params = {'spacy_model_name': 'en_core_web_sm',
                               'question_vocab_dir': 'adj_question_vocab', 'answer_vocab_dir': 'adj_answer_vocab',
                               'nn_weights_path': 'model_weights/adj_lex_model', 'right_answer_col': 'Right answer lemma'}

distractor_models = [
    ('Tense_choice', (TenseChoiceModel, tense_choice_init_params)),
    ('Prepositions', (PrepositionsModel, prepositions_init_params)),
    ('lex_item_choice', (LexVerbsModel, verb_lex_choice_init_params)),
    ('lex_item_choice', (LexNounsModel, noun_lex_choice_init_params)),
    ('lex_item_choice', (LexAdjModel, adj_lex_choice_init_params)),
]