import copy
import json
import argparse
import tqdm
import os

from sympy import symbols
from pal.core import interface
from pal.prompt import cluster_5_PAL_prompt, cluster_1_PAL_prompt


parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument(
    '--dataset', default='../../COT/results/cluster_answers/possible_no_answer/possible_no_answer.jsonl', type=str)
parser.add_argument('--model', default='gpt-4-1106-preview', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=512, type=int)
args = parser.parse_args()

DATA_PATH = f'../../COT/results/cluster_answers/possible_no_answer/possible_no_answer.jsonl'
OUTPUT_PATH = f'../../COT/results/cluster_answers/possible_no_answer/possible_no_answer_answers.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

examples = []
with open(DATA_PATH, encoding='utf-8') as file:
    for line in file:
        try:
            example = json.loads(line)
            examples.append(example)
        except json.JSONDecodeError:
            print("Skipping a malformed line in the JSON file.")

itf = interface.ProgramChatInterface(
    stop=None,
    get_answer_expr='solution()',
    model=args.model,
    verbose=args.verbose,
    system_message=cluster_5_PAL_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE,
)

args.append = True
if args.append:
    # print("是否是这样")
    lines = open(OUTPUT_PATH, encoding="utf-8").readlines()
    num_skip_exps = len(lines)
else:
    num_skip_exps = 0
# num_skip_exps=76
print(num_skip_exps)
# if args.append else 'w'
with open(OUTPUT_PATH, 'a', encoding='utf-8') as f:
    pbar = tqdm.tqdm(examples[num_skip_exps:],
                     initial=num_skip_exps, total=len(examples))
    print(len(pbar))
    for x in pbar:
        question = x['problem']
        # print(x)
        result = copy.copy(x)

        try:
            ans = itf.run(
                cluster_5_PAL_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE +
                cluster_5_PAL_prompt.MATH_CHAT_BETA_PROMPT+question,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens
            )
            ans = float(ans)
            print(ans)
        except Exception as e:
            print(e)
            ans = ''

        result['answer'] = ans
        result['generation'] = itf.history
        f.write(json.dumps(result, ensure_ascii=False) + '\n')

        itf.clear_history()
        f.flush()
