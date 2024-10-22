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
    long_click(4)

def cut_meat():
    """
    Simulate cutting meat by moving the mouse up and down over the meat area.
    """
    print("Cutting meat")
    # Check if the meat inventory is less than 3
    if inventory[3] < 3:
        # Move to the knife location to pick it up
        pyautogui.moveTo(386, 749, duration=0.1)
        # Simulate picking up the knife
        pyautogui.mouseDown()
        time.sleep(0.2)
        # Simulate the cutting motion by moving up and down repeatedly
        for _ in range(120):
            pyautogui.moveTo(450, 370, duration=0.1)  # Move to the top position
            pyautogui.moveTo(450, 600, duration=0.1)  # Move to the bottom position
            pyautogui.moveTo(450, 370, duration=0.1)  # Return to the top position
        # Release the mouse button to put down the knife
        pyautogui.mouseUp()
        # Update the meat inventory
        inventory[3] += 8

def gather_ingredients():
    """
    Simulate gathering various ingredients by clicking on their respective locations.
    """
    # Click on the character to open the ingredient menu
    pyautogui.moveTo(248, 614, duration=0.2)
    long_click(0)

    time.sleep(0.2)
    # Additional wait time if juice or sweet potato inventory is low
    if inventory[7] < 2 or inventory[8] < 2:
        time.sleep(0.6)
    # Collect cucumber if inventory is low
    if inventory[4] < 3:
        print("Collecting cucumber")
        pyautogui.moveTo(412, 539)  # Move to cucumber location
        for _ in range(10):
            long_click(0)  # Simulate clicking to collect
        inventory[4] += 8
    # Collect salt if inventory is low
    if inventory[5] < 3:
        print("Collecting salt")
        pyautogui.moveTo(412, 631)  # Move to salt location
        for _ in range(10):
            long_click(0)
        inventory[5] += 8
    # Collect juice if inventory is low
    if inventory[7] < 2:
        print("Collecting juice")
        pyautogui.moveTo(423, 718)  # Move to juice location
        for _ in range(10):
            long_click(0)
        inventory[7] = 4
    # Collect sweet potato if inventory is low
    if inventory[8] < 2:
        print("Collecting sweet potato")
        pyautogui.moveTo(424, 807)  # Move to sweet potato location
        for _ in range(10):
            long_click(0)
        inventory[8] = 8
    # Click on the character again to close the ingredient menu
    pyautogui.moveTo(248, 614, duration=0.2)
    long_click(0)

def prepare():
    """
    Perform all preparation steps: gathering ingredients, cutting potatoes, and cutting meat.
    """
    gather_ingredients()
    cut_potato()
    cut_meat()

def make_shawarma():
    """
    Simulate the process of making a shawarma.
    """
    print("Making shawarma")
    # Step 1: Click on the bread
    pyautogui.moveTo(605, 879, duration=0.1)
    long_click(0)
    # Step 2: Click on meat, cucumber, salt, and potato strips in sequence (each twice)
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
    # Step 3: Roll the shawarma
    pyautogui.moveTo(948, 915, duration=0.01)  # Start rolling
    pyautogui.mouseDown()
    pyautogui.moveTo(1148, 728, duration=0.5)  # Finish rolling (adjusted x position for better rolling)
    pyautogui.mouseUp()
    # Wait before bagging
    time.sleep(0.5)
    # Step 4: Bag the shawarma
    pyautogui.moveTo(761, 866, duration=0.1)
    long_click(0)

def add_meat():
    """
    Simulate adding meat by moving the mouse up and down over the meat area for a shorter duration.
    """
    print("Adding meat")
    # Move to the knife location to pick it up
    pyautogui.moveTo(386, 749, duration=0.1)
    # Simulate picking up the knife
    pyautogui.mouseDown()
    time.sleep(0.2)
    # Simulate the cutting motion by moving up and down repeatedly
    for _ in range(50):
        pyautogui.moveTo(450, 370, duration=0.1)  # Move to the top position
        pyautogui.moveTo(450, 600, duration=0.1)  # Move to the bottom position
        pyautogui.moveTo(450, 370, duration=0.1)  # Return to the top position
    # Release the mouse button to put down the knife
    pyautogui.mouseUp()

def add_ingredients():
    """
    Simulate adding cucumber, salt, juice, and sweet potato.
    """
    print("Adding cucumber, salt, juice, and sweet potato")
    # Click on the character to open the ingredient menu
    pyautogui.moveTo(248, 614, duration=0.2)
    long_click(0)

    time.sleep(0.2)
    # Add cucumber
    pyautogui.moveTo(412, 539, duration=0.1)  # Move to cucumber location
    for _ in range(10):
        long_click(0)  # Simulate clicking to collect
    inventory[4] += 8
    # Add salt
    pyautogui.moveTo(412, 631, duration=0.1)  # Move to salt location
    for _ in range(10):
        long_click(0)
    inventory[5] += 8
    # Add juice
    pyautogui.moveTo(423, 718, duration=0.1)  # Move to juice location
    for _ in range(10):
        long_click(0)
    inventory[7] = 4
    # Add sweet potato
    pyautogui.moveTo(424, 807, duration=0.1)  # Move to sweet potato location
    for _ in range(10):
        long_click(0)
    inventory[8] = 8
    # Click on the character again to close the ingredient menu
    pyautogui.moveTo(248, 614, duration=0.2)
    long_click(0)

print("Press the '1' key to start the preparation process...")
print("Press the '2' key to start making a shawarma...")
print("Press the '3' key to add meat...")
print("Press the '4' key to add cucumber, salt, juice, and sweet potato...")

# Main loop waiting for the '1', '2', '3', or '4' key to start the respective processes
while True:
    if keyboard.is_pressed('1'):
        print("Starting the preparation process...")
        prepare()
        print("Preparation completed!")
        time.sleep(1)  # Prevent repeated triggers
    elif keyboard.is_pressed('2'):
        print("Starting to make shawarma...")
        make_shawarma()
        print("Shawarma completed!")
        time.sleep(1)  # Prevent repeated triggers
    elif keyboard.is_pressed('3'):
        print("Adding meat...")
        add_meat()
        print("Meat added!")
        time.sleep(1)  # Prevent repeated triggers
    elif keyboard.is_pressed('4'):
        print("Adding cucumber, salt, juice, and sweet potato...")
        add_ingredients()
        print("Ingredients added!")
        time.sleep(1)  # Prevent repeated triggers
