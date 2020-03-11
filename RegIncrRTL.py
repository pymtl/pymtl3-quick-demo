from pymtl3 import *

class RegIncrRTL( Component ):
  def construct( s, nbits ):
    # Interface
    s.in_ = InPort ( nbits )
    s.out = OutPort( nbits )
    # Implementatation
    s.tmp = Wire( nbits )
    @update_ff
    def up_reg():
      s.tmp <<= s.in_
    @update
    def up_incr():
      s.out @= s.tmp + 1

if __name__ == '__main__':
  dut = RegIncrRTL(4)
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
