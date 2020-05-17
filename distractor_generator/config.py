from .distractor_models import *

tense_choice_init_params = {'spacy_model_name': 'en_core_web_sm'}
lex_item_choice_init_params = {'spacy_model_name': 'en_core_web_sm',
                               'question_vocab_dir': 'verbs_question_vocab', 'answer_vocab_dir': 'verbs_answer_vocab',
                               'nn_weights_path': 'model_weights/verbs_lex_model', 'right_answer_col': 'Right answer lemma'}
prepositions_init_params = {'spacy_model_name': 'en_core_web_sm',
                            'question_vocab_dir': 'preps_question_vocab', 'answer_vocab_dir': 'preps_answer_vocab',
                            'nn_weights_path': 'model_weights/preps_model', 'right_answer_col': 'Right answer'}

distractor_models = {
    'Tense_choice': (TenseChoiceModel, tense_choice_init_params),
    'Prepositions': (PrepositionsModel, prepositions_init_params),
    'lex_item_choice': (LexItemChoiceModel, lex_item_choice_init_params),
}