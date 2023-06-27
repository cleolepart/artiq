from artiq.experiment import *

class SetDACVoltage(EnvExperiment):
    def build(self):
        # Specify the DAC device you want to control
        self.setattr_device("dac_device")

    @kernel
    def run(self):
        # Set the desired voltage on a specific DAC channel
        channel = 0  # Replace with the channel number you want to set
        voltage = 2.5  # Replace with your desired voltage

        # Convert the voltage to DAC register value
        dac_value = voltage_to_mu(voltage)

        # Set the DAC register for the channel
        self.dac_device.write_dac_mu(channel, dac_value)

        # Pulse LDAC to update the DAC output
        self.dac_device.load()
