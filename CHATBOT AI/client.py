from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="<Your-API-Key>",
)
command = '''
[1:32 pm, 28/8/2025] Manojkourav Pw Skills: Thankyou Tanuj bhai ❤️
[10:02 pm, 28/8/2025] Manojkourav Pw Skills: Submit kab karna hoa
[10:02 pm, 28/8/2025] Manojkourav Pw Skills: Hai bhai
[10:27 am, 29/8/2025] Tanuj Singh: kl last day tha
[10:28 am, 29/8/2025] Manojkourav Pw Skills: Module konsa tha Bhai
[10:29 am, 29/8/2025] Manojkourav Pw Skills: Btao naa bhai
[10:29 am, 29/8/2025] Tanuj Singh: Ebsemble learning
[10:30 am, 29/8/2025] Manojkourav Pw Skills: Hnn
'''
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a person named <Your Name> who speaks hindi as well as english. You are from India and you are a coder. You anaylze chat history and respond like <Your name>. Output should be the next chat response as (text message only)"},
    {"role": "user", "content": command}
  ]
)

print(completion.choices[0].message.content)