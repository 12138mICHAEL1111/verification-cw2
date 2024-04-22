import re
from openai import OpenAI
import subprocess
import argparse

def parse_arg():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--key', type=str, help='openai API key')
    args = parser.parse_args()
    apikey = args.key
    return apikey

def extract_code(completion):
    pattern = r'```([a-zA-Z]+)\n(.*?)```'
    match = re.search(pattern, completion, re.DOTALL) 
    if match:
        code = match.group(2)
    return code

def pylint(file_path,disable_error_list):
    command = ['pylint', file_path , *disable_error_list]
    result = subprocess.run(command, capture_output=True, text=True).stdout
    result_lines = result.split("\n")
    result_lines = ["# "+line for line in result_lines if line != ""]
    result_format = "\n".join(result_lines)
    with open(file_path, 'a') as file:
        file.write(result_format)
    return result

def evaluate_score(result):
    start = result.find("rated at ") + 9
    end = result.find("/", start) 
    score = float(result[start:end].strip())
    return score

key = parse_arg()

client = OpenAI(
  api_key=key
)

s_prompt = []
with open("prompt/s.txt", 'r') as file:
    for line in file:
        s_prompt.append(line)

prompt_opt = ", directly return code to me with no text description and use print to print the results if needed"
s_prompt = [prompt + prompt_opt for prompt in s_prompt]

c_prompt = []
with open("prompt/c.txt", 'r') as file:
    for line in file:
        c_prompt.append(line)

c_prompt = [prompt + prompt_opt for prompt in c_prompt]

disable_error_list = []
with open("disable_error.txt", 'r') as file:
    for line in file:
        disable_error_list.append(line.strip())
   
disable_error_list = ["--disable="+error for error in disable_error_list]

def evaluate(prompt_list,type):
    raw_score_list =[]
    optimized_score_list= []
    for index,p in enumerate(prompt_list):
        history = []
        completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
                {"role": "user", "content": p}
            ]
        )
        first_completion_result = completion.choices[0].message.content
        code = extract_code(first_completion_result)
        history.append({"role":"assistant","content":code})

        raw_file_path = f"results/raw/{type}_{index}.py"
        with open(raw_file_path, 'w') as file:
            file.write(code)
            file.write("\n")
            
        result = pylint(raw_file_path,disable_error_list)
        score = evaluate_score(result)
        raw_score_list.append(score)
        history.append({"role": "user", "content": f"I use pylint to check the above code, and found the following issues:{result}, re-generate code by fixing above issues and directly return the code to me"})
        completion = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=history
        )
        second_completion_result = completion.choices[0].message.content
        code = extract_code(second_completion_result)
        optimized_file_path = f"results/optimized/{type}_{index}.py"
        with open(optimized_file_path, 'w') as file:
            file.write(code)
            file.write("\n")
        
        if score < 10.0:
            result = pylint(optimized_file_path,disable_error_list)
            score = evaluate_score(result)
            
        optimized_score_list.append(score)
    raw_average_score = sum(raw_score_list) / len(raw_score_list)
    optimized_average_score = sum(optimized_score_list) / len(optimized_score_list)
    return raw_average_score,optimized_average_score

raw_avg_score, opt_avg_score = evaluate(s_prompt,"s")
print("raw completion scroe:")
print(raw_avg_score)
print(opt_avg_score)
raw_avg_score, opt_avg_score = evaluate(c_prompt,"c")
print("optimized completion score")
print(raw_avg_score)
print(opt_avg_score)