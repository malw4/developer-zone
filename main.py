
def define_env(env):
  "Hook function"

  @env.macro
  def prerequisites():

      return "## Prerequisites

        * A Raspberry Pi Pico W board with a USB cable
        * Installed **minicom** (for Linux), **RealTerm**, **PuTTy** (for Windows), or another serial communication program.
        * An active [Coiote IoT DM](https://eu.iot.avsystem.cloud/) user account."