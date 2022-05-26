import json

with open('tasks.json', encoding='utf-8') as f:
    task = json.load(f)

class AnswersMixin(object):
    __good_answers = 0
    __bad_answers = 0

    @property
    def good_answers(self):
        return self.__good_answers

    @property
    def bad_answers(self):
        return self.__bad_answers

    def append_good(self):
        self.__good_answers += 1

    def append_bad(self):
        self.__bad_answers += 1


class Poll(AnswersMixin, object):
    tasks = []

    def __init__(self, *task_list):
        if len(task_list):
            for task in task_list:
                self.tasks.append(Task(**task))

    def get_tasks_count(self):
        return len(self.tasks)

    def start(self):
        if len(self.tasks):
            for task in self.tasks:
                if task.wait_answer():
                    self.append_good()
                else:
                    self.append_bad()
        
        print('Задач ,больше нет!')


class Task(object):
    description = ''
    answer = ''

    def __init__(self, description, answer):
        self.description = description
        self.answer = answer
    
    def get_task(self):
        print('Task:', self.description)

    def wait_answer(self):
        self.get_task()
        answer = input('Your answer: ')
        if self.check_answer(answer):
            print('Ответ правильный!')
            return True
        else:
            print('Ответ неправильный!')
            return False

    
    def check_answer(self, answer):
        if answer.lower() == self.answer.lower():
            return True
        return False

    @staticmethod
    def do_something():
        print('Nothing')


poll = Poll(*task)
print('Tasks count:', poll.get_tasks_count())

poll.start()
print('good:', poll.good_answers)
print('bad:', poll.bad_answers)

