import nltk
from nltk.corpus import stopwords
import re
import pandas as pd
import os 
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

positive_words = set(['good', 'great', 'excellent', 'positive', 'fortunate', 'correct', 'superior'])
negative_words = set(['bad', 'terrible', 'poor', 'negative', 'unfortunate', 'wrong', 'inferior'])

def clean_text(text):
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def sentiment_analysis(text):
    words = text.split()
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    polarity_score = (positive_score - negative_score) / ((positive_score + negative_score) + 0.000001)
    subjectivity_score = (positive_score + negative_score) / (len(words) + 0.000001)
    return positive_score, negative_score, polarity_score, subjectivity_score

def readability_analysis(text):
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    complex_words = [word for word in words if len(nltk.word_tokenize(word)) > 2]
    average_sentence_length = len(words) / len(sentences)
    percentage_complex_words = len(complex_words) / len(words)
    fog_index = 0.4 * (average_sentence_length + percentage_complex_words)
    return average_sentence_length, percentage_complex_words, fog_index

def other_metrics(text):
    words = nltk.word_tokenize(text)
    word_count = len(words)
    complex_word_count = len([word for word in words if len(nltk.word_tokenize(word)) > 2])
    syllable_count = sum([len(re.findall(r'[aeiouy]+', word.lower())) for word in words])
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    average_word_length = sum(len(word) for word in words) / len(words)
    return word_count, complex_word_count, syllable_count, personal_pronouns, average_word_length

input_dir = 'articles extracted' 

results = []

for file_name in os.listdir(input_dir):
    if file_name.endswith('.txt'):
        file_path = os.path.join(input_dir, file_name)
        url_id = file_name.split('.')[0]

        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        
        cleaned_text = clean_text(text)

        
        pos_score, neg_score, pol_score, subj_score = sentiment_analysis(cleaned_text)

        
        avg_sent_length, perc_complex_words, fog_index = readability_analysis(cleaned_text)

        
        word_count, complex_word_count, syllable_count, personal_pronouns, avg_word_length = other_metrics(cleaned_text)

        
        results.append([
            url_id, pos_score, neg_score, pol_score, subj_score,
            avg_sent_length, perc_complex_words, fog_index,
            word_count, complex_word_count, syllable_count, personal_pronouns, avg_word_length
        ])


columns = [
    'URL_ID', 'Positive_Score', 'Negative_Score', 'Polarity_Score', 'Subjectivity_Score',
    'Average_Sentence_Length', 'Percentage_of_Complex_Words', 'Fog_Index',
    'Word_Count', 'Complex_Word_Count', 'Syllable_Count', 'Personal_Pronouns', 'Average_Word_Length'
]
results_df = pd.DataFrame(results, columns=columns)

output_file_path = 'Output Data Structure.xlsx'
results_df.to_excel(output_file_path, index=False)

print(f"Text analysis complete. Results saved to {output_file_path}.")