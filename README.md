# GPT-4 automatically solves math problems

This repo provides the code, prompts, and our answers solved for the [AAAI2024 Global Competition on Math Problem Solving and Reasoning](https://ai4ed.cc/competitions/aaai2024competition)

**We have participated in both Track 1 and Track 2, this document is mainly about the steps and methods used in solving the English questions of Track 2, the description of the Chinese part of Track 1 is at the bottom of this document.**

Our final submission of the answer file is in:

```
/final-submission/TAL_SAQ6K_EN_prediction.json
```

You can submit this result directly to codebench as our result on the leaderboard

This README is organized in the following order.

1. Methods: The main methods used in the competition and the procedures used to obtain the final results.
2. Final Submission: Location for submitting answer results
3. Setup: Preparation before running the code
4. Usage Demo: Steps to run the code quickly

## Methods

We have mainly used to solve the problem by using `few-shot+chain of thought(COT)`, `Program-Aided Language(PAL)`, `choose-COT-or-PAL` ,`Plan and execute`, `ResPrompt`,`Vote`, COT related code and result intermediate files are at: `/code/COT`, the PAL related code and result intermediate files are in:`/code/PAL`.

The specific methods and steps are as follows:

### Dataset  classification

In order to better use the `Few-Shot` Learning and `Chain of Thought` methods in the following section with respect to solving math problems, this study first uses the `KMeans` clustering algorithm to classify the text of the topic 

The classified code is in`/code/classification`

The main categories after classification are as follows:

![image-20240111232136172](https://github.com/hot-zhy/mathEducatorsSolving/assets/100272100/744cee19-8075-4259-9389-f14da8acf242)


### Few-shot+Chain of thought（COT）

After the above categorization, there are 14 categories, each category has its specific knowledge point topic, we wrote 3-5 sample problems for each category as example problems for the `few-shot`, and incorporated the sample problems into the `Prompt`, and categorized the constructed Prompts to input to the` GPT-4` for solving the problems.

The template location for this section of the prompt is at:

```
/code/COT/cot/prompt/clusters_few_shot_prompt
```

### Program-Aided Language(PAL)

Use PAL (Program-aid Language) for topics that are suitable for solving in code (denoted as PAL)

The template location for this section of the prompt is at:

```
/code/PAL/pal/prompt/clusters_prompt
```

PAL's related papers:

```
[7]Gao L, Madaan A, Zhou S, et al. Pal: Program-aided language models[C]//International Conference on Machine Learning. PMLR, 2023: 10764-10799.
```

In addition to this we use the following templates:

### Choose PAL or COT

In order to choose whether to use PAL or COT, we wrote the relevant templates to allow it to automatically choose which scheme to use, and save the result

The template location for the associated prompt is at:

```
/code/COT/cot/prompt/choose_COT_or_PAL_prompt.py
```

### Plan and Execute

Use first plan and then execute.

The template location for the associated prompt is at:

```
/code/COT/cot/prompt/plan_and_execute_prompt.py
```

### ResPrompt

Template prompts for using residual connections

The template location for the associated prompt is at:

```
/code/COT/cot/prompt/resprompt.py
```

### Getting the final result

Following Methods step by step, we end up with the result:

```
{"TAL_SAQ6K_EN_Public_Acc": 85.21, "TAL_SAQ6K_EN_Private_Acc": 86.0}
```

## Final Submission

The following document is the final outcome document:

```
/final-submission/TAL_SAQ6K_EN_prediction.json
```

You can submit this result directly to codebench as our result on the leaderboard

### 我们获得这个答案的步骤为：

In addition, we also use a certain`voting` mechanism, that is, the answers of the above methods are summarized, and the answer with the `highest` number of times is used as the final result

So, in `final-submission`, we first got the following result file as described above:

```
/final-submission/TAL_SAQ6L_EN_prediction.jsonl
```

Then we voted on the first category of the classification and got the results:

```
cluster_1_vote.jsonl
```

We merged these two jsonl file and extracted the final numerical answer as:

```
/final-submission/TAL_SAQ6K_EN_prediction.json
```

## Setup 

1. Pull the code repository

2. Go to /code/COT and execute:

   ```
   pip install ./
   ```

   Go to /code/PAL and execute.

   ```
   pip install ./
   ```

3. Prepare an OpenAI key, go to the following location for api-key and api-url settings

   ```
   /code/COT/cot/core/backend.py
   /code/PAL/pal/core/backend.py
   ```

## Usage Demo

### Executing the following file is to solve the first category of topics using `few-shot`+`chain of thought`:

```
/code/COT/scripts/cot_chatgpt.py
```

If you need to use another prompt, just change the corresponding imported prompt in the files under `/code/COT/scripts/` (or `/code/PAL/scripts `if it's PAL):.

```python
from cot.prompt import cluster_0_prompt
#Then you can change the places in this file where you need to use the prompt.
```

## Chinese Problems Track 1

For the Chinese track 1, we only used the form of few-shot+Chain of thought, and the related result files are in:

```
/code/COT/chinese-answers/submission/TAL_SAQ7K_CN_prediction.json
```







