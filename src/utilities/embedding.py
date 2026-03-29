import ast

def parse_embedding(embedding_str: str):
    if not embedding_str:
        return []
    return ast.literal_eval(embedding_str)