class Type(Node):

  self.name

  def __init__(self, name = null):
    self.name = name


  # def name=(name)
  #   if name.is_a?(Token)
  #     self.name = name.value
  #   else
  #     self.name = name

  def __setattr__(self, name, value):
      if isInstance(name, Token):
          self.name = name.value
      else:
          self.name = name

  def __str__(self):
    return '<TYPE: {}>'.format(self.name)


  def __eq__(self, other):
    return self.name == other.name
