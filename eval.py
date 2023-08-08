"""
eval()
  文字列をPythonのコードとして実行するための関数

使い方
% poetry run python eval.py
Enter an arithmetic expression: 5*7
Result: 35
"""
expression = input("Enter an arithmetic expression: ")

result = eval(expression)
print(f"Result: {result}")
