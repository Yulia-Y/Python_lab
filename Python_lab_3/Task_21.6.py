global wb_tree

def tree():
    #black = tree() бесконечную рекурсия? не будет работать
    black = [] #не поняла что значит 'имитировать' бесконечное дерево
    white = []
    white.extend([black, black])
    black.extend([white, white, white])
    return black

wb_tree = tree()