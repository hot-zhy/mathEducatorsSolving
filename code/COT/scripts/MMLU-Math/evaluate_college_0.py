import copy
import json
import argparse
import tqdm
import os

from sympy import symbols

from cot.core import interface
from cot.prompt import MMLU_math_prompt,high_1_prompt,college_0_prompt


parser = argparse.ArgumentParser()
parser.add_argument('--append', action='store_true')
parser.add_argument('--verbose', action='store_true')
parser.add_argument(
    '--dataset', default='../../../../code/classification/MMLU-Math/college/college_0.jsonl', type=str)
parser.add_argument('--model', default='gpt-4-1106-preview', type=str)
parser.add_argument('--temperature', default=0.0, type=float)
parser.add_argument('--top_p', default=1.0, type=float)
parser.add_argument('--max_tokens', default=2096, type=int)
args = parser.parse_args()

DATA_PATH = args.dataset
OUTPUT_PATH = f'./results/few-shot/college/college_0_answers.jsonl'
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

examples = list(map(json.loads, open(DATA_PATH, encoding='utf-8')))

itf = interface.ProgramChatInterface(
    stop=None,
    model=args.model,
    verbose=args.verbose,
    system_message=college_0_prompt.META_PROMPT,
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
        question = x['problem']+'The options are: '+str(x['options'])
        # print(x)
        result = copy.copy(x)
        try:
            ans = itf.generate(
                college_0_prompt.SPECIFIC_METHOD +
                college_0_prompt.EXEMPLARS+college_0_prompt.FORMAT_REQUIREMENT+question,
                temperature=args.temperature,
                top_p=args.top_p,
                max_tokens=args.max_tokens
            )
        except Exception as e:
            print(e)
            ans = ''

        result['answer'] = ans
        # result['generation'] = itf.history
        result['standard-answer']=x['answer']
        f.write(json.dumps(result, ensure_ascii=False) + '\n')

        itf.clear_history()
        f.flush()
