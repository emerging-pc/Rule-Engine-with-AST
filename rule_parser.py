from ast_node import Node


def create_rule(rule_string):
    # For simplicity, handle basic AND/OR rules for now.
    if "AND" in rule_string:
        parts = rule_string.split("AND")
        return Node("operator", "AND", create_rule(parts[0].strip()), create_rule(parts[1].strip()))
    # For operand nodes like "age > 30"
    elif ">" in rule_string:
        attr, val = rule_string.split(">")
        return Node("operand", {"attribute": attr.strip(), "operator": ">", "value": int(val.strip())})
    # Handle more cases (OR, <, =, etc.) similarly


rule_string = "age > 30 AND department = 'Sales'"
ast = create_rule(rule_string)
print(ast)  # Check if it builds the correct AST
