from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

article = (
    "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. "
    "Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."
)

summary = summarizer(article, max_length=50, min_length=20, do_sample=False)

print("Rezumējums:")
print(summary[0]['summary_text'])
