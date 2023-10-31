text="Мировая экономика также сталкивается с вызовами, связанными с изменением климата и устойчивостью ресурсов.Стремление к сокращению выбросов парниковых газов и более эффективному использованию природных ресурсов становится всё более актуальным.Секторы, такие как здравоохранение и образование, остаются важными для развития мировой экономики.Здоровое население и образованная рабочая сила способствуют экономическому росту и инновациям.Секторы, такие как здравоохранение и образование, остаются важными для развития мировой экономики.Здоровое население и образованная рабочая сила способствуют экономическому росту и инновациям."
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
