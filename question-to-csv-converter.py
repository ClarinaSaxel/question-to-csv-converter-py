from string import ascii_uppercase
import os

def glue_question_back_together(list):
    a=list[:]
    string=''
    for element in list:
        if any(element.startswith(s) for s in '123456789'):
            string+=f'\t{element}'
            a.remove(element)
    a[1]+=string
    return a

def insert_empty_explanation_for_wrong_answers(list, count_wrong_answers):
    a=list[-count_wrong_answers:]
    for count in range(count_wrong_answers):
        #print(f'count: {count}, 2*count-1 = {2*count-1}')
        a.insert(2*count+1, '')
    #print(f'a: {a}\nlist[count_wrong_answers:]: {list[:-count_wrong_answers]}')
    return list[:-count_wrong_answers]+a

def change_weird_answer_format(list):
    a=list[1:]
    for index,element in enumerate(a):
        tab = element.find('\t')
        if tab>-1:
            a[index]=element[tab+1:]
    return [list[0]]+a

def count_possible_answers(list):
    count=0
    for element in list:
        if any(element.startswith(s) for s in [f'{s})' for s in ascii_uppercase]):
            count+=1
    return count

def remove_unnecessary_lines(list):
    a=list[:]
    for element in list:
        if element[:-2].isupper():
            a.remove(element)
    return a

def sort_answer_to_right_place(list):
    solindex = list.index('LÖSUNG')+1
    list.remove(list[solindex])
    answer = list.pop(solindex-1)
    list.insert(2, answer)
    return list

def sort_explanation_to_right_place(list):
    expindex = list.index('ERKLÄRUNG')+1
    explanation = list.pop(expindex)
    list.insert(3, explanation)
    return list

def convert_to_csv(textfile):
    with open(textfile, 'r', encoding='utf-8') as filobjekt:
        content_string = filobjekt.read()

    content_string = content_string.strip()
    questions = content_string.split('\n\n')

    for q in range(len(questions)):
        questions[q] = questions[q].split('\n')

    csv_formatted_questions=[]

    for question in questions:
        question=glue_question_back_together(question)
        sort_answer_to_right_place(question)
        sort_explanation_to_right_place(question)
        question=remove_unnecessary_lines(question)
        wrong_answers=count_possible_answers(question)-1
        question=change_weird_answer_format(question)
        question.insert(1,'')
        question.insert(2, '1')
        question.insert(3, f'{wrong_answers}')
        question=insert_empty_explanation_for_wrong_answers(question, wrong_answers)
        question=';'.join(question)
        csv_formatted_questions.append(question)

    title = textfile.split('.')[0]

    with open(f'{title}.csv', 'w', encoding='utf-8') as filobjekt:
        filobjekt.write('\n'.join(csv_formatted_questions))
    return '\n'.join(csv_formatted_questions)

if __name__ == '__main__':

    path = input('Give the path to the folder with your textfiles or press enter for current folder:\n')
    if path == '':
        path=os.getcwd()
    textfiles = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)) and file.endswith('.txt'):
            textfiles.append(file)
    print(textfiles)

    for textfile in textfiles:
        try:
            convert_to_csv(textfile)
        except:
            print('Oops, something went wrong, maybe there is a wrong textfile?')
