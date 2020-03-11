from pymtl3 import *
from FullAdderGL import FullAdderGL

class RippleCarryAdderGL( Component ):

  def construct( s, nbits ):
    # Interface
    s.in0  = InPort ( nbits )
    s.in1  = InPort ( nbits )
    s.out  = OutPort( nbits )
    s.cout = OutPort()

    # Implementatation
    s.fas = [ FullAdderGL() for _ in range(nbits) ]

    # Connect the input and output ports
    for i in range(nbits):
      s.fas[i].a   //= s.in0[i]
      s.fas[i].b   //= s.in1[i]
      s.fas[i].sum //= s.out[i]
    # Connect the carry chain
    s.fas[0].cin //= 0
    for i in range(nbits-1):
      s.fas[i].cout //= s.fas[i+1].cin
    s.fas[-1].cout //= s.cout

if __name__ == '__main__':
  dut = RippleCarryAdderGL(2)
  dut.apply( SimulationPass(waveform='text_ascii') )
  dut.sim_reset()

  tvecs = [
    # in0  in1  out cout
    [ 3,   2,   1,  1   ],
    [ 2,   1,   3,  0   ],
    [ 2,   1,   3,  0   ],
    [ 2,   1,   3,  0   ],
    [ 2,   3,   1,  1   ],
  ]
  for tvec in tvecs:
    dut.in0   @= tvec[0]
    dut.in1   @= tvec[1]

    dut.sim_tick()
    assert dut.out  == tvec[2]
    assert dut.cout == tvec[3]

  dut.print_textwave()
