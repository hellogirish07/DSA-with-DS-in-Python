# Given an expression string exp,
# WAP in python to examin wheather the pair and the orders of "{", "}", "(", ")", "[", "]" 
# are correct expression.

# Example 

# input : exp = "[()]{}{[()()]}{}"
# output : balanced

# input : exp = "[(])"
# output : not balanced 

def isBalanced(exp):
    stack = []
    for char in exp:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            currunt_char = stack.pop()
            if currunt_char == "(":
                if char != ")":
                    return False
            if currunt_char == "[":
                if char != "]":
                    return False
            if currunt_char == "{":
                if char != "}":
                    return False
    if stack:
        return False
    return True

exp = "{()}[]"
if(isBalanced(exp)):
    print("Balanced")
else:
    print("Not Balanced")
