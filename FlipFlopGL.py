from pymtl3 import *

class FlipFlopGL( Component ):

  def construct( s ):
    # Interface
    s.d = InPort ()
    s.q = OutPort()
    # Implementatation
    @update_ff
    def up_seq_logic():
      s.q <<= s.d

if __name__ == '__main__':
  dut = FlipFlopGL()
  dut.apply( SimulationPass(waveform='text_ascii') )
  dut.sim_reset()

  tvecs = [
    # d
    [ 1 ],
    [ 0 ],
    [ 0 ],
    [ 1 ],
    [ 1 ],
    [ 0 ],
    [ 0 ],
    [ 0 ],
  ]
  for tvec in tvecs:
    dut.d   @= tvec[0]
    dut.sim_tick()

  dut.print_textwave()
