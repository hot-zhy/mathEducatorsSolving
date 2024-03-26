import copy
import json
import argparse
import os
import re
from tqdm import tqdm
from sympy import symbols
from cot.core import interface
from cot.prompt import choose_COT_or_PAL_prompt

# Command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument(
    '--dataset', default='../results/cluster_answers/cluster_5_PAL/cluster_5_COT_PAL_combine_answers.jsonl', type=str)
parser.add_argument('--model', default='gpt-4-1106-preview', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=2096, type=int)
args = parser.parse_args()

# File paths
DATA_PATH = args.dataset
OUTPUT_PATH = f'../../results/cluster_answers/cluster_5_PAL/cluster_5_COT_PAL_combine_choose.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# ProgramChatInterface initialization
itf = interface.ProgramChatInterface(
    stop=None,
    model=args.model,
    verbose=args.verbose,
    system_message=choose_COT_or_PAL_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE,
)

# Set of processed queIds
processed_queIds = set()
if os.path.exists(OUTPUT_PATH) and os.path.getsize(OUTPUT_PATH) > 0:
    with open(OUTPUT_PATH, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                processed_queIds.add(json.loads(line).get('queId'))
            except json.JSONDecodeError:
                continue
# Processing and resuming
with open(DATA_PATH, 'r', encoding='utf-8') as file, open(OUTPUT_PATH, 'a', encoding='utf-8') as f:
    for line in tqdm(file, desc="Processing"):
        try:
            x = json.loads(line)
            if x.get('queId') in processed_queIds:
                continue  # Skip already processed entries

            result = copy.copy(x)
            problem_description = x['problem']
            pal_solution = x['pal_generation']
            pal_answer = x['pal_answer']
            cot_solution = x['cot_generation']
            cot_number_answer = x['cot_answer']
            number_match = re.findall(
                r"[-+]?\d*\.\d+|[-+]?\d+", cot_number_answer)
            cot_answer = float(number_match[-1]) if number_match else None

            ans = itf.generate(
                choose_COT_or_PAL_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE +
                choose_COT_or_PAL_prompt.MATH_CHAT_BETA_PROMPT.format(
                    problem_description=problem_description,
                    pal_solution=pal_solution, pal_answer=pal_answer, cot_solution=cot_solution, cot_answer=cot_answer),
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens
            )

            result['choose-answer'] = ans
            f.write(json.dumps(result, ensure_ascii=False) + '\n')
            processed_queIds.add(x.get('queId'))  # Mark as processed
        except json.JSONDecodeError as e:
            print(f'Parsing error: {e}')
