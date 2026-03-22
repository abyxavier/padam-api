import ast

def parse_embedding(embedding_str: str):
    return ast.literal_eval(embedding_str)