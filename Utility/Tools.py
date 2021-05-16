import os
import re


class Tools:
    def __init__(self):
        self.home_dir = os.path.abspath(os.path.dirname(os.getcwd()))
        self.recent_created_dir = ''
        self.question_name = ''
        self.default_filename_regex = r'^\d{4}_(.+)$'

    def build_folder_name(self, name):
        question_regex = re.compile(r'^(\d+)\.\s(.+)$')
        question_number = question_regex.match(name).group(1)
        question_name = question_regex.match(name).group(2)
        self.question_name = question_name
        print(f"question_number: {question_number}")
        print(f"question_name: {question_name}")
        final_question_number = (4 - len(question_number)) * '0' + question_number
        final_queston_name = re.sub(r'\.\s|[\.\s]', '_', question_name)
        folder_name = final_question_number + '_' + final_queston_name
        print(f"folder_name: {folder_name}")
        return folder_name

    def make_dir(self, name, selection=1):
        python_algorithms_dir = os.path.join(self.home_dir, "Algorithms")
        java_algorithms_dir = os.path.join(self.home_dir, "Algorithms")

        if selection == 1:
            name = self.build_folder_name(name)
            new_dir = os.path.join(python_algorithms_dir, name, 'Python')
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            self.recent_created_dir = new_dir

        if selection == 2:
            name = self.build_folder_name(name)
            new_dir = os.path.join(java_algorithms_dir, name, 'Java')
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            self.recent_created_dir = new_dir

        return new_dir

    def make_file(self, name='', selection=1, solution_number=1):
        dir = self.make_dir(name, selection)
        # file_name = os.path.basename(dir)

        if selection == 1:
            file_name = self.question_name.replace(' ', '_') + '_Solution_' + str(solution_number) + '.py'
        if selection == 2:
            file_name = self.question_name.replace(' ', '') + 'Solution' + str(solution_number) + '.java'

        file_destination = os.path.join(dir, file_name)

        if os.path.exists(file_destination):
            print("file already exists. " + file_destination)
        else:
            # print(file_destination)
            with open(file_destination, 'w')as f:
                pass


tools = Tools()
tools.make_file('65. Valid Number',1,1)
# tools.make_file('9999. Find First and Last Position of Element in Sorted Array',2,1)

