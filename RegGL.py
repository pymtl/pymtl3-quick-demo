from pymtl3 import *
from FlipFlopGL import FlipFlopGL

class RegGL( Component ):
  def construct( s, nbits ):
    # Interface
    s.in_ = InPort ( nbits )
    s.out = OutPort( nbits )
    # Implementatation
    s.ffs = [ FlipFlopGL() for _ in range(nbits) ]
    # Connect the input and output ports
    for i in range(nbits):
      s.ffs[i].d //= s.in_[i]
      s.ffs[i].q //= s.out[i]

if __name__ == '__main__':
  dut = RegGL( nbits = 5 )
  dut.apply( SimulationPass(waveform='text_ascii') )
  dut.sim_reset()

  tvecs = [
    # d
    [ 0b00010 ],
    [ 0b00100 ],
    [ 0b11010 ],
    [ 0b00010 ],
  ]
  for tvec in tvecs:
    dut.in_ @= tvec[0]
    dut.sim_tick()

  dut.print_textwave()
