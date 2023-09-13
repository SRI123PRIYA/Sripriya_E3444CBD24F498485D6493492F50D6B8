class Batsman:

  def _init_(self, name):
    self.name = name

  def play(self):
    print(f"{self.name} is batting.")


class Bowler:

  def _init_(self, name):
    self.name = name

  def play(self):
    print(f"{self.name} is bowling.")


# Create objects of the Batsman and Bowler classes
batsman1 = Batsman("Player 1")
bowler1 = Bowler("Player 2")

# Call the play() method for each object
batsman1.play()
bowler1.play()
