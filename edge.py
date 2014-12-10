class Edge:
  def __init__(self,s,t,w,et):
    self.s = s
    self.t = s
    self.w = w
    self.type = et

  def is_null(self):
    return False

class NullEdge:
  def __init__(self):
    self.s = None
    self.t = None
    self.w = None
    self.type = None

  def is_null(self):
    return True