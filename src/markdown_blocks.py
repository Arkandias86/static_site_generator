def markdown_to_blocks(markdown):
    lines = list(map(lambda line: line.strip(), markdown.strip().splitlines(True)))
    blocks = []
    block = ""
    for line in lines:
        if line:
            block =  block + "\n" + line if block else block + line
        else:
            if block:
                blocks.append(block)
                block = ""
    if block:
        blocks.append(block)
    return blocks