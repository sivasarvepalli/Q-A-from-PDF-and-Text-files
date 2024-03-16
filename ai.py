import os
from ai_bricks.api import openai

DEFAULT_USER = os.getenv('COMMUNITY_USER', '')

def initialize():
    openai.use_key(os.getenv('OPENAI_API_KEY', ''))
    set_user(DEFAULT_USER)

def set_user(user):
    openai.set_global('user', user)
    openai.add_callback('after', track_usage)

def track_usage(out, resp, self):
    model = self.config['model']
    usage = resp['usage']
    update_statistics(usage, model)

def update_statistics(usage, model):
    usage_stats.increment(f'usage:{model}', usage)
    usage_stats.increment(f'hourly:{model}', usage)

def complete(text, model='gpt-3.5-turbo'):
    llm = openai.model(model)
    llm.config['pre_prompt'] = 'output only in raw text'  # for chat models
    response = llm.complete(text)
    response['model'] = model
    return response

def embedding(text, model='text-embedding-ada-002'):
    llm = openai.model(model)
    response = llm.embed(text)
    response['model'] = model
    return response

def embeddings(texts, model='text-embedding-ada-002'):
    llm = openai.model(model)
    response = llm.embed_many(texts)
    response['model'] = model
    return response

def get_token_count(text):
    tokenizer_model = openai.model('text-davinci-003')
    return tokenizer_model.token_count(text)

def get_community_usage_cost():
    usage_data = usage_stats.get(f'usage:v4:{DEFAULT_USER}')
    costs = {
        'gpt-4': 0.04,
        'text-davinci-003': 0.02,
        'text-curie-001': 0.002,
        'gpt-3.5-turbo': 0.002,
        'text-embedding-ada-002': 0.0004
    }
    total_cost = sum(costs[model] * usage_data.get(f'total_tokens:{model}', 0) / 1000 for model in costs)
    return total_cost

initialize()
