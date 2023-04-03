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

def get_question_sample(path: str) -> list:

    list_quest_ans = []
    with open(path, "r", encoding="utf-8") as q_file:
        content = q_file.read()
        qst = 1
        last_index = 0
        while True: 
            last_index = content.find(f"Câu {qst}.", last_index)
            if last_index  == -1:
                break

            end_index = content.find('\n', last_index)
            question = content[last_index:end_index]

            four_ans = ""
            for i in "ABCD":
                last_index = content.find(f"{i}.", last_index)
                end_index = content.find('\n', last_index)
                four_ans = four_ans + content[last_index:end_index] + "\n"
            qst += 1
            list_quest_ans.append(question + "\n" + four_ans)

    return list_quest_ans 

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



file_similar = open(similar_quest_path, 'w')

list_quest_ans = get_question_sample("question.txt")

result = ""
request = "Create a list of 5 questions and 4 answers with each question, each with the same topic as the questions above."
for i in range(0, len(list_quest_ans)):
    result = result + generate_questions(list_quest_ans[i], request)

save_to_txt(result, similar_quest_path)

file_similar.close()