import copy
import json
import argparse
import tqdm
import os

from sympy import symbols

from cot.core import interface
from cot.prompt import cluster_0_prompt, cluster_13_prompt, cluster_11_prompt, cluster_9_prompt, cluster_11_3_prompt, cluster_11_2_prompt, cluster_12_prompt, plan_and_execute_prompt


parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument(
    '--dataset', default='../results/cluster_answers/cluster_12_COT_PAL/cluster_12_COT_PAL.jsonl', type=str)
parser.add_argument('--model', default='gpt-4-1106-preview', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=2096, type=int)
args = parser.parse_args()

DATA_PATH = f'../results/cluster_answers/cluster_12_COT_PAL/cluster_12_COT_PAL.jsonl'
OUTPUT_PATH = f'../results/cluster_answers/cluster_12_COT_PAL/cluster_12_COT_PAL_plan.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

examples = list(map(json.loads, open(DATA_PATH, encoding='utf-8')))

itf = interface.ProgramChatInterface(
    stop=None,
    model=args.model,
    verbose=args.verbose,
    system_message=plan_and_execute_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE,
)


args.append = True
if args.append:
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
    for x in pbar:
        question = x['problem']
        # print(x)
        result = copy.copy(x)
        try:
            ans = itf.generate(
                plan_and_execute_prompt.MATH_CHAT_BETA_SYSTEM_MESSAGE +
                plan_and_execute_prompt.MATH_CHAT_BETA_PROMPT+question,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens
            )
        except Exception as e:
            print(e)
            ans = ''

        result['answer'] = ans
        result['generation'] = itf.history
        f.write(json.dumps(result, ensure_ascii=False) + '\n')

        itf.clear_history()
        f.flush()
