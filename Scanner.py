#!/usr/bin/python

class Scanner:

   position = 0

   def __init__(self, codeFile, commandsFile):
      self.commands = self.getCommands(commandsFile)
      self.text = self.getTextFromFile(codeFile)
      
   def valueOf(self, string):
      if string in self.commands:
         return self.commands.index(string)
      start = string[0]
      if start == "$":
         return len(self.commands)
      if start.isdigit():
         return len(self.commands) + 1
      if start.isalpha():
         return len(self.commands) + 2
      if start == "\"":
         return len(self.commands) + 3
      if start == "\0":
         return len(self.commands) + 5
      return len(self.commands) + 4

   def getCommands(self, commandsFile):
      text = self.getTextFromFile(commandsFile)
      commands = text.split()
      return commands

   def getTextFromFile(self, filepath):
      with open(filepath, 'rb') as f:
         return f.read()

   def nextChar(self):
      if (self.hasNext()):
         c = self.text[self.position]
         self.position += 1
         return c
      print "FINISHED"
      return "\0"

   def hasNext(self):
     while (self.position < len(self.text) and self.text[self.position].isspace()):
         self.position += 1
     return self.position < len(self.text)



   def next(self):
       c = self.nextChar()
       while (c.isspace() and self.hasNext()):
          c = self.nextChar()
       if c.isalpha():
          return self.generateName(c)
       elif c.isdigit():
          return self.generateInt(c)
       elif (c == "/"):
          return self.checkSlash(c)
       elif (c == "$"):
          secondChar = self.text[self.position]
          if secondChar.isalpha():
             return self.generateName(c)
          else:
             return "?"
       elif (c == "\""):
          return self.generateString(c)
       elif (c in "+-*{}();,"):
          return c
       elif (c in "<>!="):
          return self.generateEql(c)
       return c

   def generateEql(self, c):
       string = ""
       string += c
       if (self.text[self.position] == "="):
           string += self.nextChar()
       return string

   def generateString(self, c):
       string = ""
       string += c
       while (self.position < len(self.text) and ((self.text[self.position] == '"' and self.text[self.position - 1] == "\\") or self.text[self.position] <> '"')):
            string += self.nextChar()
       if (self.position == len(self.text)):
           return "?"
       string += self.nextChar()
       return string

   def checkSlash(self, c):
       nextChar = self.text[self.position]
       if (nextChar == "/"):
           while ((self.nextChar()) <> "\n"):
              pass
           return self.next()
       if (nextChar == "*"):
           while True:
               if(self.nextChar() == "*"):
                   if (self.text[self.position] == "/"):
                       self.position += 1
                       break
               if(len(self.text) == self.position):
                   return "?"
           return self.next()
       return c

   def generateName(self, c):
       string = ""
       string += c
       while (self.text[self.position].isalnum() or self.text[self.position] == "_"):
          string += self.next()
       return string

   def generateInt(self, c):
       string = ""
       string += c
       while (self.text[self.position].isdigit()):
          string += self.next()
       return string

