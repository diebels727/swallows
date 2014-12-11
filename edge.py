class Edge:
  def __init__(self,s,t,w,et):
    self.s = s
    self.t = t
    self.w = w
    self.type = et

  def is_null(self):
    return False

  def __repr__(self):
    return "[s: %d,t: %d,w: %d,type: %s]" % (self.s,self.t,self.w,self.type)

  def __str__(self):
    return "Edge [s: %d,t: %d,w: %d,type: %s]" % (self.s,self.t,self.w,self.type)

class NullEdge:
  def __init__(self):
    self.s = None
    self.t = None
    self.w = None
    self.type = None

  def is_null(self):
    return True