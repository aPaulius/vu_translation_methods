class Parameter(Node):

  self.name
  self.type
  self.localSlot

  def __init__(self):
    self.name   = null
    self.type   = null

  def allocateSlots(self):
    global localSlot

    self.localSlot  = localSlot
    localSlot       += 1

  def isConst(self):
    return False
