import Parser
import Scanner
# read tokens


tokens = []
globalSlot = 0
localSlot  = 0

scanner = Scanner.Scanner('pavyzdys-programos.txt', 'commands.txt')
while scanner.hasNext():
    string = scanner.next()
    tokens.append(scanner.valueOf(string))

parser = Parser.Parser()

# parse tokens
parser.parse(tokens)
