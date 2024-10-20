from ast_node import create_rule


def evaluate_rule(ast, data):
    if ast is None:
        return False

    if ast.node_type == "operand":
        attribute = ast.value["attribute"]
        operator = ast.value["operator"]
        value = ast.value["value"]
        
        data_value = data.get(attribute)
        print(f"Evaluating: {attribute} {operator} {value} (data_value: {data_value})")  # Debug output
        
        if data_value is None:
            print(f"Warning: {attribute} not found in data.")
            return False
        
        if operator == '=':
            return data_value == value
        elif operator == '>':
            return data_value > value
        elif operator == '<':
            return data_value < value
        elif operator == '>=':
            return data_value >= value
        elif operator == '<=':
            return data_value <= value
        elif operator == '!=':
            return data_value != value

    elif ast.node_type == "operator":
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        
        print(f"Evaluating: {left_eval} {ast.value} {right_eval}")  # Debug output
        
        if ast.value == "AND":
            return left_eval and right_eval
        elif ast.value == "OR":
            return left_eval or right_eval
    
    return False
