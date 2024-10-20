from ast_node import Node
from ast_node import create_rule  # Import the create_rule function

def test_create_rule():
    # Test parsing of a rule: "age > 30 AND department = 'Sales'"
    rule_string = "age > 30 AND department = 'Sales'"
    ast = create_rule(rule_string)

    # Print the AST to check the structure
    print(ast)

    # You can also add assertions to verify the structure programmatically
    assert ast.type == "operator"
    assert ast.value == "AND"
    assert ast.left.value == {"attribute": "age", "operator": ">", "value": 30}
    assert ast.right.value == {"attribute": "department", "operator": "=", "value": "Sales"}

if __name__ == "__main__":
    test_create_rule()
