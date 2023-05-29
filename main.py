from dotenv import load_dotenv
import os, time
import openai

load_dotenv()
api_key = os.getenv('API_KEY')
max_tokens = os.getenv('MAX_TOKEN')
quest_path = 'question.txt'
similar_quest_path = 'similar_question.txt'

def convert_list_to_str(list_question: list) -> str:
    str_formated = ""
    for j in range(0, len(list_question)):
        str_formated += list_question[j] + ""
    return str_formated

def save_to_txt(text: str, path_file: str) -> None:
    with open(path_file, 'w', encoding='utf-8', errors='ignore') as txt_file:
        txt_file.write(text)

def read_file_lines(file_path):
    lines = []
    with open(file_path, 'r', encoding= 'utf-8') as file:
        lines = file.readlines()
    return lines

def generate_questions(question_sample: str, request: str, api_key=api_key, max_tokens=max_tokens):
    openai.api_key = (api_key)
    prompt = question_sample + '\n' + request

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )    
    return response.choices[0].text

def checked_with_api(question: str, request: str, api_key=api_key, max_tokens=max_tokens):

    openai.api_key = (api_key)
    prompt = question + '\n' + request

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=3000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text


def check():
    file_similar = open(quest_path, 'w')

    list_quest_ans = read_file_lines(quest_path)
    result = ""
    request = "Answer the question."
    for i in range(0, len(list_quest_ans)):
        result = result + generate_questions(list_quest_ans[i], request)

    save_to_txt(result, 'check.txt')

    file_similar.close()

def main():
    file_similar = open(similar_quest_path, 'w')

    list_quest_ans = read_file_lines('question.txt')
    result = ""
    # request = "Create a list of 5 questions and 4 answers with each question, each with the same topic as the questions above."
    request = """Create a list of 5 questions and 4 answers with each question, each on the same topic as the questions above, of the form:
    Question: |Answer A| Answer B|Answer C|Answer D"""
    for i in range(0, len(list_quest_ans)):
        result = result + generate_questions(list_quest_ans[i], request)

    save_to_txt(result, similar_quest_path)

    file_similar.close()

if __name__ == '__main__':
    main()
    check()



