# Bedsores Prevention System - Vibration Motor Fix
from machine import Pin, SoftI2C, PWM
import time
import bme280

# ========== HARDWARE CONFIGURATION ==========
# BME280 Sensor
I2C_SDA_PIN = 21
I2C_SCL_PIN = 22
i2c = SoftI2C(sda=Pin(I2C_SDA_PIN), scl=Pin(I2C_SCL_PIN))
bme = bme280.BME280(i2c=i2c)

# Vibration Motor (ERM) - Modified configuration
MOTOR_PIN = 13
motor = Pin(MOTOR_PIN, Pin.OUT)  # Simple digital control instead of PWM

# Servo Motor (SG90)
SERVO_PIN = 12
PWM_FREQ_SERVO = 50  # Standard 50Hz for servos
servo = PWM(Pin(SERVO_PIN), freq=PWM_FREQ_SERVO)

# ========== CALIBRATION ==========
# Servo Parameters
MIN_ANGLE = 0
MAX_ANGLE = 180
MIN_PULSE_US = 500
MAX_PULSE_US = 2500

# Threshold Values
TEMP_THRESHOLD = 32.0
PRESSURE_THRESHOLD = 1001.0
HUMIDITY_THRESHOLD = 80.0

# ========== ACTUATOR FUNCTIONS ==========
def vibrate(duration_ms=500):
    """Control vibration motor with digital output"""
    try:
        print("Activating vibration motor...")
        motor.value(1)  # Turn motor ON
        time.sleep_ms(duration_ms)
        motor.value(0)  # Turn motor OFF
        print("Vibration complete")
    except Exception as e:
        print("Vibration motor error:", e)
        motor.value(0)  # Ensure motor is off if error occurs

def test_vibration():
    """Test vibration motor function"""
    print("Testing vibration motor (3 pulses)...")
    for i in range(3):
        print(f"Pulse {i+1}...")
        vibrate(1000)  # 1 second on
        time.sleep(0.5)  # 0.5 second off

def set_servo_angle(angle):
    """Move servo to specified angle (0-180°) with protection"""
    try:
        angle = max(MIN_ANGLE, min(MAX_ANGLE, angle))
        pulse_us = MIN_PULSE_US + (angle * (MAX_PULSE_US - MIN_PULSE_US) / 180)
        duty = int(pulse_us * PWM_FREQ_SERVO * 65535 / 1_000_000)
        servo.duty_u16(duty)
        time.sleep_ms(300)  # Allow time to move
    except Exception as e:
        print("Servo error:", e)
        servo.duty_u16(0)

def lateral_movement():
    """Perform full lateral movement sequence"""
    print("Initiating lateral movement...")
    for angle in [45, 90, 135]:
        set_servo_angle(angle)
        vibrate(200)  # Small vibration during movement
        time.sleep(1)
    set_servo_angle(90)  # Return to center

# Run a simple test for the vibration motor
print("Bedsores Prevention System - Vibration Motor Test")
test_vibration()

# Now run the main system if you want
response = input("Continue with main program? (y/n): ")
if response.lower() == 'y':
    try:
        print("Starting main program...")
        while True:
            # Read and parse sensor data
            temp_str, press_str, hum_str = bme.values
            temp = float(temp_str[:-1])
            press = float(press_str[:-3])
            hum = float(hum_str[:-1])
            
            print(f"\nTemperature: {temp}°C | Pressure: {press}hPa | Humidity: {hum}%")
            
            # Check thresholds and trigger responses
            temp_high = temp > TEMP_THRESHOLD
            press_high = press > PRESSURE_THRESHOLD
            hum_high = hum > HUMIDITY_THRESHOLD
            
            if temp_high:
                print("High temperature detected")
                vibrate(1000)
                lateral_movement()
                
            if press_high:
                print("High pressure detected")
                vibrate(1000)
                lateral_movement()
                
            if hum_high:
                print("High humidity detected")
                vibrate(1000)
                lateral_movement()
            
            if temp_high and press_high and hum_high:
                print("Critical condition detected")
                vibrate(1500)
                lateral_movement()
            
            time.sleep(2)
    except KeyboardInterrupt:
        motor.value(0)
        servo.duty_u16(0)
        print("\nSystem safely stopped")
else:
    print("Test complete. System not started.")
