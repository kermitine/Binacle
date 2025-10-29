"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the DHOC project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

version = '0.0.5'

motor_settings = { # defaults
    'rpm': 3000,
    'gear_ratio': 100,
    'stepper_motor_steps': 200
}

arduino_settings = { # defaults
    'port': 'COM3',
    'baud_rate': 9600,
    'port_number': 3
}

azimuth_settings = { # defaults for latitude and longitude are for the observatory at CSUDH
    'latitude': 33.863907, 
    'longitude': -118.255190,
    'planet': 'Mars'
}

# commonly used prompts
prompt_input_not_recognized = 'Input not recognized. Please try again.'
prompt_invalid_values = 'ERROR: One or multiple invalid values detected. Please try again.'