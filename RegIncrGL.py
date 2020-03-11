from pymtl3 import *
from RegGL import RegGL
from RippleCarryAdderGL import RippleCarryAdderGL

class RegIncrGL( Component ):
  def construct( s, nbits ):
    # Interface
    s.in_ = InPort ( nbits )
    s.out = OutPort( nbits )
    # Implementatation
    s.reg_ = RegGL( nbits )
    s.incr = RippleCarryAdderGL( nbits )
    # Connections
    s.reg_.in_ //= s.in_
    s.incr.in0 //= s.reg_.out
    s.incr.in1 //= 1
    s.out      //= s.incr.out

if __name__ == '__main__':
  dut = RegIncrGL(4)
  dut.apply( SimulationPass(waveform='text_ascii') )
  dut.sim_reset()

  tvecs = [
    # in_  out
    [ 3,   1,  ],
    [ 2,   4,  ],
    [ 1,   3,  ],
    [ 2,   2,  ],
    [ 2,   3,  ],
  ]
  for tvec in tvecs:
    dut.in_ @= tvec[0]

    dut.sim_tick()

  dut.print_textwave()
