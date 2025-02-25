import tkinter as tk
import math
import ast
import operator

class CalculadoraGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Básica")

        self.entry = tk.Entry(root, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: self.click(b)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def calcular_expressao(self, expressao):
        try:
            node = ast.parse(expressao, mode='eval').body
            return self.avaliar_node(node)
        except Exception as e:
            return f"Erro: {e}"

    def avaliar_node(self, node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = self.avaliar_node(node.left)
            right = self.avaliar_node(node.right)
            return self.aplicar_operacao(node.op, left, right)

    def aplicar_operacao(self, operacao, *args):
        operadores = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv
        }
        try:
            func = operadores[type(operacao)]
            return func(*args)
        except KeyError:
            raise ValueError(f"Operador não suportado: {type(operacao)}")

    def click(self, key):
        if key == '=':
            try:
                result = self.calcular_expressao(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, f"Erro: {e}")
        else:
            self.entry.insert(tk.END, key)

root = tk.Tk()
calculadora = CalculadoraGUI(root)
root.mainloop() 