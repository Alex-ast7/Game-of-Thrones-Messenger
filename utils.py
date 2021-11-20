# import torch
# from transformers import AutoModelForCausalLM, AutoTokenizer
#
# checkpoint = "Grossmend/rudialogpt3_medium_based_on_gpt2"
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
#
# model = AutoModelForCausalLM.from_pretrained(
#     pretrained_model_name_or_path='checkpoints/gpt/', )
# model = model.to('cpu')
# model.eval()
#
#
# def get_length_param(text: str) -> str:
#     tokens_count = len(tokenizer.encode(text))
#     if tokens_count <= 15:
#         len_param = '1'
#     elif tokens_count <= 50:
#         len_param = '2'
#     elif tokens_count <= 256:
#         len_param = '3'
#     else:
#         len_param = '-'
#     return len_param
#
#
# chat_history_ids = torch.zeros((1, 0), dtype=torch.int)
#
# input_user = 'Приветствую тебя!'
# new_user_input_ids = tokenizer.encode(f"|0|{get_length_param(input_user)}|" \
#                                       + input_user + tokenizer.eos_token,
#                                       return_tensors="pt")
# chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
# next_len = 2
# new_user_input_ids = tokenizer.encode(f"|1|{next_len}|", return_tensors="pt")
# chat_history_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
# # append the new user input tokens to the chat history
# input_len = chat_history_ids.shape[-1]
# chat_history_ids = model.generate(
#     chat_history_ids,
#     num_return_sequences=1,
#     max_length=512,
#     no_repeat_ngram_size=3,
#     do_sample=True,
#     top_k=50,
#     top_p=0.9,
#     temperature=0.6,  # 0 for greedy
#     mask_token_id=tokenizer.mask_token_id,
#     eos_token_id=tokenizer.eos_token_id,
#     unk_token_id=tokenizer.unk_token_id,
#     pad_token_id=tokenizer.pad_token_id,
#     device='cpu'
# )
#
# # pretty print last ouput tokens from bot
# print(
#     f"===> GPT-3:  {tokenizer.decode(chat_history_ids[:, input_len:][0], skip_special_tokens=True)}")
from transformers import AutoTokenizer
mode = 'ru-en'
AutoTokenizer.from_pretrained(f"Helsinki-NLP/opus-mt-ru-en")