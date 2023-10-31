text="Мировая экономика также сталкивается с вызовами, связанными с изменением климата и устойчивостью ресурсов.Стремление к сокращению выбросов парниковых газов и более эффективному использованию природных ресурсов становится всё более актуальным.Секторы, такие как здравоохранение и образование, остаются важными для развития мировой экономики.Здоровое население и образованная рабочая сила способствуют экономическому росту и инновациям.Секторы, такие как здравоохранение и образование, остаются важными для развития мировой экономики.Здоровое население и образованная рабочая сила способствуют экономическому росту и инновациям."
count_econom=0
for i in text.split():
    if (i=="экономика"):
        count_econom+=1
print("кількість слів економіка = ",count_econom)#найти количество слов экономика
def reduce_text_length(text):
    half_length = len(text) // 2
    reduced_text = text[:half_length]
    return reduced_text
reduced_text = reduce_text_length(text)
count_econom = 0
for word in reduced_text.split():
    if word == "экономика":
        count_econom += 1
print("Кількість слів 'економіка' в уменьшеному тексті =", count_econom)

def add_spaces_after_period(text):
    sentences = text.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    result = '. '.join(sentences)
    return result

result = add_spaces_after_period(reduced_text)
print(result)

def replace_characters(sentence, old, new):
    new_sentence = sentence.replace(old, new)
    return new_sentence

modified_text = replace_characters(result, 'о', 'x')
print(modified_text)

def remove_long_words(modified_text):
    words = text.split()  #Разбить предложение на слова
    filtered_words = [word for word in words if len(word) <= 7]  #Фильтровать слова
    cleaned_text = ' '.join(filtered_words)  #Объединить слова обратно в строку
    return cleaned_text

cleaned_text = remove_long_words(modified_text)
print(cleaned_text)
