from pymtl3 import *

class FullAdderGL( Component ):

  def construct( s ):
    # Interface
    s.a    = InPort ()
    s.b    = InPort ()
    s.cin  = InPort ()
    s.sum  = OutPort()
    s.cout = OutPort()
    # Implementatation
    @update
    def up_comb_logic():
      s.sum  @= s.a ^ s.b ^ s.cin
      s.cout @= (s.a & s.b) | (s.a & s.cin) | (s.b & s.cin)

if __name__ == '__main__':
  dut = FullAdderGL()
  dut.apply( SimulationPass(waveform='text_ascii') )

  tvecs = [
    # a  b  cin
    [ 0, 0, 0 ],
    [ 0, 0, 1 ],
    [ 0, 1, 0 ],
    [ 0, 1, 1 ],
    [ 1, 0, 0 ],
    [ 1, 0, 1 ],
    [ 1, 1, 0 ],
    [ 1, 1, 1 ],
  ]
  for tvec in tvecs:
    dut.a   @= tvec[0]
    dut.b   @= tvec[1]
    dut.cin @= tvec[2]
    dut.sim_tick()

  dut.print_textwave()
