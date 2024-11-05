import pyautogui
import time
import keyboard

# Initialize inventory with zeros for different ingredients
inventory = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Set a brief pause between PyAutoGUI actions to prevent errors
pyautogui.PAUSE = 0.02

def long_click(duration):
    """
    Simulate holding down the mouse button for a specified duration.
    """
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def cut_potato():
    """
    Simulate cutting potato strips by holding down the mouse button over the potato area for 4 seconds.
    """
    print("Cutting potato strips for 4 seconds")
    # Move to the potato cutting area
    pyautogui.moveTo(1742, 711, duration=0.1)
    # Hold down the mouse button to simulate cutting
    long_click(3)

def click_coke_machine():
    pyautogui.moveTo(1341, 623, duration=0.01)
    long_click(0)
    pyautogui.moveTo(1410, 619, duration=0.01)
    long_click(0)
    pyautogui.moveTo(1562, 668, duration=0.01)
    long_click(0)

def add_fries():
    pyautogui.moveTo(1549, 892, duration=0.01)
    long_click(0)
    long_click(0)
    long_click(0)
    time.sleep(1)
    pyautogui.moveTo(1544, 797, duration=0.01)
    long_click(0)
    pyautogui.moveTo(1630, 809, duration=0.01)
    long_click(0)
    pyautogui.moveTo(1704, 795, duration=0.01)
    long_click(0)

def prepare():
    """
    Perform all preparation steps: gathering ingredients, cutting potatoes, and cutting meat.
    """
    pyautogui.moveTo(260, 557, duration=0.01)
    long_click(0)
    cut_potato()
    click_coke_machine()
    add_fries()
    
def make_shawarma():
    """
    Simulate the process of making a shawarma.
    """
    print("Making shawarma")
    # Step 1: Click on meat, cucumber, salt, and potato strips in sequence (each twice)
    pyautogui.moveTo(513, 739, duration=0.1)
    long_click(0)
    long_click(0)
    pyautogui.moveTo(670, 739, duration=0.01)
    long_click(0)
    long_click(0)
    pyautogui.moveTo(829, 739, duration=0.01)
    long_click(0)
    long_click(0)
    pyautogui.moveTo(965, 739, duration=0.01)
    long_click(0)
    long_click(0)
    # Step 2: Roll the shawarma
    pyautogui.moveTo(948, 915, duration=0.01)  # Start rolling
    pyautogui.mouseDown()
    pyautogui.moveTo(1148, 728, duration=0.5)  # Finish rolling (adjusted x position for better rolling)
    pyautogui.mouseUp()
    # Step 3: Bag the shawarma
    time.sleep(0.2)
    pyautogui.moveTo(761, 866, duration=0.1)
    long_click(0)

def collect_money():
    """
    Simulate collecting money by moving the mouse from the left side of the table to the right side.
    """
    print("Collecting money from the table")
    POS_TABLE_LEFT = (586, 627)
    POS_TABLE_RIGHT = (1557, 624)
    # Move to the left side of the table
    pyautogui.moveTo(POS_TABLE_LEFT[0], POS_TABLE_LEFT[1], duration=0.2)
    # Hold down the mouse button and drag to the right side of the table
    pyautogui.mouseDown()
    pyautogui.moveTo(POS_TABLE_RIGHT[0], POS_TABLE_RIGHT[1], duration=1.0)
    pyautogui.mouseUp()

print("Press the '1' key to start the preparation process...")
print("Press the '2' key to start making a shawarma...")
print("Press the '3' key to add fries...")
print("Press the '4' key to click coke machine...")
print("Press the '5' key to collect money from the table...")

# Main loop waiting for the '1', '2', '3', '4', or '5' key to start the respective processes
while True:
    if keyboard.is_pressed('1'):
        print("Starting the preparation process...")
        prepare()
        print("Preparation completed!")
        time.sleep(0.7)  # Prevent repeated triggers
    elif keyboard.is_pressed('2'):
        print("Starting to make shawarma...")
        make_shawarma()
        time.sleep(0.3)
        make_shawarma()
        time.sleep(0.2)
        long_click(0)
        print("Shawarma completed!")
        time.sleep(0.7)  # Prevent repeated triggers
    elif keyboard.is_pressed('3'):
        print("Adding fries...")
        add_fries()
        print("Meat added!")
        time.sleep(0.7)  # Prevent repeated triggers
    elif keyboard.is_pressed('4'):
        print("Click coke machine")
        click_coke_machine()
        print("Machine clicked!")
        time.sleep(0.7)  # Prevent repeated triggers
    elif keyboard.is_pressed('5'):
        print("Collecting money from the table...")
        collect_money()
        print("Money collected!")
        time.sleep(0.7)  # Prevent repeated triggers
