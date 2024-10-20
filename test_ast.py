def test_simple_rule():
    root = Node("operator", "AND")
    assert root.node_type == "operator"
    assert root.value == "AND"


from ast_node import Node  # Import your Node class

def test_simple_rule():
    # Creating a simple AST node structure for a rule: (age > 30 AND department = 'Sales')
    root = Node("operator", "AND")
    root.left = Node("operand", {"attribute": "age", "operator": ">", "value": 30})
    root.right = Node("operand", {"attribute": "department", "operator": "=", "value": "Sales"})
    
    # Print the node structure to verify
    print(root)

if __name__ == "__main__":
    test_simple_rule()

