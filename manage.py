"""
Python Script to manage the Solutions and Logic of the LC Questions.
"""

from pathlib import Path
import yaml
import os

root: Path = Path(__file__).parent
"""Make sure to run this script from the root of the repository."""

with open(root / "questions.yaml", "r", encoding="utf-8") as fd:
    questions = list(yaml.safe_load(fd).values())[0]


def generate_table():
    files = os.listdir("solutions")
    with open(root / "questions.yaml", "r", encoding="utf-8") as fd:
        questions = list(yaml.safe_load(fd).values())[0]
    
    t,flag = list(),False
    for i in questions:
        t.append(i['question_number'])
    
    for i in set(t):
        if t.count(i) > 1:
            print(f"Duplicate Question {i}")
            flag = True

    if flag:
        raise ValueError(f"Duplicate Questions in questions.yaml")
    
    for i in questions:
        if f"{i['question_number']}.py" not in files:
            print(f"Question {i['question_number']} not found.")
            raise FileNotFoundError(f"{i['question_number']}.py")

    headers = ['Question number', 'Name', 'Solution link']

    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---" for _ in headers]) + " |\n"

    for item in sorted(questions,key=lambda x: x['question_number']):
        row_values = list(item.values())
        row_values[0] = str(row_values[0])
        row_values[1] = f"[{row_values[1]}]({row_values[2]})"
        row_values[2] = f"[Python3 Solution](https://github.com/henilp105/leetcode-obsidian/blob/main/solutions/{row_values[0]}.py)"
        markdown_table += "| " + " | ".join(row_values) + " |\n"

    with open(root / "README.md", "r+", encoding="utf-8") as fd:
        data = ''.join(fd.readlines()[:8]) + markdown_table
        fd.seek(0)
        fd.write(data)



if __name__ == "__main__":

    print("Generating Table for LC Questions")
    generate_table()
    print("Table Generated.")
