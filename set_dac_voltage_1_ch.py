from artiq.experiment import *

class SetDACVoltage(EnvExperiment):
    def build(self):
        # Specify the DAC device you want to control
       ## self.setattr_device("zotino0")
        self.dac_device = self.get_device("zotino0")
        self.core = self.get_device("core")

       # Set the desired voltage on a specific DAC channel
        self.channel = 3  # Replace with the channel number you want to set
        self.voltage = 2.5  # Replace with your desired voltage

    @kernel
    def run(self):
        self.core.reset()
        self.dac_device.init()
        
        # Convert the voltage to DAC register value
        dac_value = self.dac_device.voltage_to_mu(self.voltage)

        # Set the DAC register for the channel
        self.dac_device.write_dac_mu(self.channel, dac_value)

        # Pulse LDAC to update the DAC output
        self.dac_device.load()

        delay(3*s)

         # Set the DAC register for the channel
        self.dac_device.write_dac(self.channel, 0.)

        # Pulse LDAC to update the DAC output
        self.dac_device.load()







