from collections import namedtuple
from statistics import median

Syntax = namedtuple("Syntax", "match,score")


def parse_input_file(input_file_name) -> list[str]:
    print(f"Reading input: {input_file_name}")
    with open(input_file_name, "r") as f:
        return [line.strip() for line in f.readlines()]


def is_opening(char):
    return char in list("([{<")


def is_closing(char):
    return char in list(")]}>")


def main():
    input_file_name = "input.txt"
    lines = parse_input_file(input_file_name)

    # Key: character to close a chunk
    syntax = {
        ")": Syntax(match="(", score=3),
        "]": Syntax(match="[", score=57),
        "}": Syntax(match="{", score=1197),
        ">": Syntax(match="<", score=25137),

        "(": Syntax(match=")", score=0),
        "[": Syntax(match="]", score=0),
        "{": Syntax(match="}", score=0),
        "<": Syntax(match=">", score=0),
    }

    syntax_errors = []
    incomplete_lines = []
    for line in lines:
        print(line)
        stack = []
        syntax_error = None
        for index, char in enumerate(line):
            if is_opening(char):
                stack.append(char)
            elif is_closing(char):
                top_element = stack[-1]
                if top_element != syntax[char].match:
                    syntax_error = syntax[char].score
                    #print(f"char={char} at index {index}, top_element={top_element}, stack={stack}")
                    #print(f"{top_element} != {syntax[char].match}")
                    #print(f"Syntax error to add: {syntax_error}")
                    break
                else:
                    stack.pop()
            else:
                print(f"Illegal character! {char}")
                assert False

        if syntax_error:
            syntax_errors.append(syntax_error)
        else:
            incomplete_lines.append(line)

    print(f"{len(syntax_errors)}/{len(lines)} lines with syntax errors: {syntax_errors}")
    print(f"Total score: {sum(syntax_errors)}")
    if input_file_name == "example_input.txt":
        assert sum(syntax_errors) == 26397

    print("~ * ~ * ~ Part II ~ * ~ * ~")

    points = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    scores = []
    for line in incomplete_lines:
        print(line)
        stack = []
        for char in line:
            if is_opening(char):
                stack.append(char)
            elif is_closing(char):
                top_element = stack[-1]
                if top_element == syntax[char].match:
                    stack.pop()
            else:
                print(f"Illegal character! {char}")
                assert False

        print(f"Stack: {stack}")
        stack.reverse()
        to_add = ""
        for char in stack:
            if is_closing(char):
                print(f"{char} = closing ...")
                assert False
            to_add += syntax[char].match

        print(f"to_add: {to_add}")
        total_score = 0
        for char in to_add:
            total_score *= 5
            total_score += points[char]
        scores.append(total_score)

    print(f"Scores: {scores}")
    print(f"Median score: {median(scores)}")


main()
