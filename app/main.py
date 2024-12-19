from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

class Term(BaseModel):
    description: str

glossary: Dict[str, Term] = {
    "F1-Score": Term(description="Метрика, объединяющая точность (Precision) и полноту (Recall) модели машинного обучения."),
    "Recall": Term(description="Доля истинно положительных результатов среди всех положительных результатов."),
    "Precision": Term(description="Доля истинно положительных результатов среди всех положительных результатов, предсказанных моделью."),
    "False Alarm Rate": Term(description="Доля ложных срабатываний среди всех положительных результатов, предсказанных моделью."),
    "Точность анализа": Term(description="Степень соответствия результатов анализа фактическому состоянию системы."),
    "Метрики эффективности статического анализа": Term(description="Показатели, используемые для оценки качества статического анализа кода."),
    "Статический анализ кода": Term(description="Процесс анализа исходного кода без его выполнения, направленный на выявление ошибок и уязвимостей."),
    "SonarQube": Term(description="Платформа для статического анализа кода, используемая для выявления дефектов и улучшения качества кода."),
    "Svace": Term(description="Инструмент статического анализа кода, разработанный в России, для поиска ошибок и уязвимостей."),
    "PVS-Studio": Term(description="Статический анализатор кода, предназначенный для поиска ошибок и уязвимостей в C++ и C# коде."),
    "Статический анализатор": Term(description="Программа, анализирующая исходный код для выявления ошибок и уязвимостей без его выполнения."),
    "Тестирование безопасности": Term(description="Процесс проверки системы на наличие уязвимостей и слабых мест."),
    "Уязвимости безопасности": Term(description="Слабые места в системе, которые могут быть использованы для несанкционированного доступа или нанесения ущерба."),
    "OWASP": Term(description="Организация, занимающаяся разработкой стандартов и рекомендаций по безопасности веб-приложений."),
    "CWE": Term(description="Каталог уязвимостей программного обеспечения, разработанный MITRE."),
    "SQL-инъекция": Term(description="Вид атаки, при которой злоумышленник внедряет вредоносный SQL-код в веб-приложение."),
    "XSS (межсайтовый скриптинг)": Term(description="Вид атаки, при которой вредоносный код внедряется в веб-страницу и выполняется на стороне пользователя."),
    "Система контроля версий (VCS)": Term(description="Инструмент для управления изменениями в исходном коде."),
    "Backend": Term(description="Часть программного обеспечения, отвечающая за обработку данных и выполнение бизнес-логики."),
    "Матрица ошибок": Term(description="Таблица, отображающая результаты тестирования."),
    "True Positive": Term(description="Положительный результат, который был правильно идентифицирован."),
    "False Positive": Term(description="Положительный результат, который был ошибочно идентифицирован."),
    "True Negative": Term(description="Отрицательный результат, который был правильно идентифицирован."),
    "Flase Negative": Term(description="Отрицательный результат, который был ошибочно идентифицирован.")
}

@app.get("/terms", response_model=Dict[str, Term])
def get_all_terms():
    return glossary

@app.get("/terms/{term}")
def get_term(term: str):
    if term not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    return glossary[term]

@app.post("/terms/{term}", response_model=Dict[str, Term])
def add_term(term: str, term_data: Term):
    if term in glossary:
        raise HTTPException(status_code=400, detail="Term already exists")
    glossary[term] = term_data
    return {term: term_data}

@app.put("/terms/{term}", response_model=Dict[str, Term])
def update_term(term: str, term_data: Term):
    if term not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    glossary[term] = term_data
    return {term: term_data}

@app.delete("/terms/{term}")
def delete_term(term: str):
    if term not in glossary:
        raise HTTPException(status_code=404, detail="Term not found")
    del glossary[term]
    return {"detail": "Term deleted successfully"}
