import pyautogui
import time
import keyboard

# Inventory to store the count of different ingredients
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
    Simulate cutting potato strips by holding down the mouse button over the potato area for a few seconds.
    """
    print("Cutting potato strips for 3 seconds")
    pyautogui.moveTo(1742, 711, duration=0.1)  # Move to the potato cutting area
    long_click(3)  # Hold down the mouse button to simulate cutting

def click_coke_machine():
    """
    Simulate clicking the Coke machine multiple times.
    """
    print("Clicking Coke machine")
    positions = [(1341, 623), (1410, 619), (1562, 668)]
    for pos in positions:
        pyautogui.moveTo(*pos, duration=0.01)
        long_click(0)

def add_fries():
    """
    Simulate adding fries.
    """
    print("Adding fries")
    pyautogui.moveTo(1549, 892, duration=0.01)  # Add fries
    for _ in range(3):
        long_click(0)
    time.sleep(1)  # Wait for the fries to be ready
    positions = [(1544, 797), (1630, 809), (1704, 795)]  # Positions to add fries to different slots
    for pos in positions:
        pyautogui.moveTo(*pos, duration=0.01)
        long_click(0)

def prepare():
    """
    Perform all preparation steps: gathering ingredients, cutting potatoes, and using the Coke machine.
    """
    print("Starting preparation process")
    pyautogui.moveTo(260, 557, duration=0.01)  # Gather ingredients
    long_click(0)
    cut_potato()
    click_coke_machine()
    add_fries()

def make_shawarma():
    """
    Simulate the process of making a shawarma.
    """
    print("Making shawarma")
    ingredients_positions = [
        (513, 739),  # Meat
        (670, 739),  # Cucumber
        (829, 739),  # Salt
        (965, 739)   # Potato strips
    ]
    # Add ingredients to shawarma
    for pos in ingredients_positions:
        pyautogui.moveTo(*pos, duration=0.1)
        long_click(0)
        long_click(0)
    # Roll the shawarma
    pyautogui.moveTo(948, 915, duration=0.01)  # Start rolling
    pyautogui.mouseDown()
    pyautogui.moveTo(1148, 728, duration=0.3)  # Finish rolling
    pyautogui.mouseUp()

def collect_money():
    """
    Simulate collecting money from the table.
    """
    print("Collecting money from the table")
    POS_TABLE_LEFT = (586, 627)
    POS_TABLE_RIGHT = (1557, 624)
    pyautogui.moveTo(*POS_TABLE_LEFT, duration=0.2)
    pyautogui.mouseDown()
    pyautogui.moveTo(*POS_TABLE_RIGHT, duration=1.0)
    pyautogui.mouseUp()

def main():
    """
    Main function to run the automation script based on key presses.
    """
    print("Press '1' to start the preparation process...")
    print("Press '2' to start making a shawarma...")
    print("Press '3' to add fries...")
    print("Press '4' to click the Coke machine...")
    print("Press '5' to collect money from the table...")

    while True:
        if keyboard.is_pressed('1'):
            print("Starting the preparation process...")
            prepare()
            print("Preparation completed!")
            time.sleep(0.7)  # Prevent repeated triggers
        elif keyboard.is_pressed('2'):
            print("Starting to make shawarma...")
            make_shawarma()
            time.sleep(0.2)
            make_shawarma()
            time.sleep(0.2)
            pyautogui.moveTo(761, 866, duration=0.1)
            long_click(0)
            print("Shawarma completed!")
            time.sleep(0.7)  # Prevent repeated triggers
        elif keyboard.is_pressed('3'):
            print("Adding fries...")
            add_fries()
            print("Fries added!")
            time.sleep(0.7)  # Prevent repeated triggers
        elif keyboard.is_pressed('4'):
            print("Clicking Coke machine...")
            click_coke_machine()
            print("Coke machine clicked!")
            time.sleep(0.7)  # Prevent repeated triggers
        elif keyboard.is_pressed('5'):
            print("Collecting money from the table...")
            collect_money()
            print("Money collected!")
            time.sleep(0.7)  # Prevent repeated triggers

if __name__ == "__main__":
    main()
