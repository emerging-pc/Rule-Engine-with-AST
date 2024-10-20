import re

class Node:
    def __init__(self, node_type, value, left=None, right=None):
        self.node_type = node_type
        self.value = value
        self.left = left
        self.right = right

def tokenize(rule_string):
    pattern = r"\s+|([()])|([A-Za-z_][A-Za-z0-9_]*)|(!=|<=|>=|<|>|=|AND|OR)"
    tokens = []

    for match in re.finditer(pattern, rule_string):
        if match.group(1):  # Parentheses
            tokens.append(match.group(1))
        elif match.group(2):  # Identifiers (attributes, values)
            tokens.append(match.group(2))
        elif match.group(3):  # Operators
            tokens.append(match.group(3))

    return tokens

def create_rule(rule_string):
    tokens = tokenize(rule_string)
    print(f"Tokens: {tokens}")  # Debugging: Print tokens

    stack = []
    current_expression = []
    expecting_operator = False  # Track if we are expecting an operator after an attribute
    expecting_value = False     # Track if we are expecting a value after an operator

    for token in tokens:
        if token == '(':
            stack.append(current_expression)
            current_expression = []
            expecting_operator = False
            expecting_value = False
        elif token == ')':
            if not stack:
                raise ValueError("Mismatched parentheses")
            last_expression = stack.pop()
            last_expression.append(current_expression)
            current_expression = last_expression
            expecting_operator = True  # After closing parentheses, expect AND/OR
        elif token in {'AND', 'OR'}:
            if not expecting_operator:
                raise ValueError(f"Invalid token format '{token}'. Expected a condition before this operator.")
            current_expression.append(token)
            expecting_operator = False
        else:
            if not expecting_operator and not expecting_value:  # Start of a condition
                if len(current_expression) == 0 or current_expression[-1] in {'AND', 'OR', '('}:
                    current_expression.append(token)  # First token of a condition: attribute
                    expecting_operator = True
                else:
                    raise ValueError(f"Unexpected token '{token}'. Expected an operator.")
            elif expecting_operator:  # We are expecting an operator now
                if token in {'>', '<', '>=', '<=', '=', '!='}:
                    current_expression.append(token)
                    expecting_operator = False
                    expecting_value = True  # After operator, we expect a value next
                else:
                    raise ValueError(f"Invalid token format '{token}'. Expected an operator.")
            elif expecting_value:  # Now we expect a value
                current_expression.append(token)
                expecting_operator = True  # After value, expect AND/OR or closing parenthesis
                expecting_value = False

    if len(current_expression) < 3:
        raise ValueError("Incomplete expression; expected at least one condition.")

    return current_expression
