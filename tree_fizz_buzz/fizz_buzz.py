class TNode:
    def __init__(self,value):
        self.value=value
        self.children=[]




class kTree:
    def __init__(self,root=None):
        self.root = root


    def _walk(self):
        output=[]
        def check_output(node):
            output.append(node.value)
            if node.children:
                for children in node.childern:
                    check_output(children)
        check_output(self.root)
        return  output



def fizz_buzz(kTree):
    def _walk(node):
        if node.children:
            for i in node.children:
                if i.value %3 ==0 and i.value% 5 ==0:
                    i.value="FizzBuzz"
                elif i.value %3==0:
                    i.value= "Fizz"

                elif i.value%5==0:
                    i.value="Buzz"

                else:
                    i.value= str(i.value)

    _walk(kTree.root)
    return (kTree)








