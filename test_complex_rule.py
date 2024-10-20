# test_complex_rule.py

from ast_node import create_rule
from rule_evaluator import evaluate_rule

def test_complex_rule():
    rule_string = "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
    ast = create_rule(rule_string)
    print("Generated AST:", ast)  # Add this line to check the AST structure

    data_1 = {"age": 35, "department": "Sales", "salary": 60000, "experience": 6}
    data_2 = {"age": 22, "department": "Marketing", "salary": 40000, "experience": 2}
    data_3 = {"age": 40, "department": "HR", "salary": 30000, "experience": 3}

    print("Case 1: ", evaluate_rule(ast, data_1))  # Expected output: True
    print("Case 2: ", evaluate_rule(ast, data_2))  # Expected output: False
    print("Case 3: ", evaluate_rule(ast, data_3))  # Expected output: False


if __name__ == "__main__":
    test_complex_rule()
