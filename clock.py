import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
import random
import os

def generate_analog_clock(time, filename):
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal')

    # Draw the clock face
    clock_face = plt.Circle((0, 0), 1, edgecolor='black', facecolor='white')
    ax.add_patch(clock_face)

    # Draw the hour marks
    for hour in range(1, 13):
        angle = np.deg2rad((hour / 12) * 360)
        x = 0.9 * np.sin(angle)
        y = 0.9 * np.cos(angle)
        ax.text(x, y, str(hour), horizontalalignment='center', verticalalignment='center', fontsize=15)

    # Extract hour, minute, and second from the time
    hour = time.hour % 12
    minute = time.minute
    second = time.second

    # Calculate the angles for the hour, minute, and second hands
    hour_angle = np.deg2rad((hour + minute / 60) / 12 * 360)
    minute_angle = np.deg2rad((minute + second / 60) / 60 * 360)
    second_angle = np.deg2rad(second / 60 * 360)

    # Draw the hour hand
    hour_hand_x = [0, 0.5 * np.sin(hour_angle)]
    hour_hand_y = [0, 0.5 * np.cos(hour_angle)]
    ax.plot(hour_hand_x, hour_hand_y, linewidth=6, color='black')

    # Draw the minute hand
    minute_hand_x = [0, 0.8 * np.sin(minute_angle)]
    minute_hand_y = [0, 0.8 * np.cos(minute_angle)]
    ax.plot(minute_hand_x, minute_hand_y, linewidth=4, color='blue')

    # Draw the second hand
    second_hand_x = [0, 0.9 * np.sin(second_angle)]
    second_hand_y = [0, 0.9 * np.cos(second_angle)]
    ax.plot(second_hand_x, second_hand_y, linewidth=2, color='red')

    # Remove the axes
    ax.set_axis_off()

    # Set the limit for x and y axis
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)

    # Save the figure to a file
    plt.savefig(filename, format='jpg', bbox_inches='tight')
    plt.close(fig)

def generate_markdown_file(image_filenames, markdown_filename):
    with open(markdown_filename, 'w') as f:
        f.write("# Analog Clock Faces\n\n")
        for image_filename in image_filenames:
            f.write(f"![{image_filename}]({image_filename})\n\n")

# Example usage to generate 6 clock faces with random times
current_time = datetime.now()
image_filenames = []
for i in range(6):
    # Generate a random number of hours, minutes, and seconds
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    random_seconds = random.randint(0, 59)

    # Create a random time based on the current time
    random_time = current_time.replace(hour=random_hours, minute=random_minutes, second=random_seconds)

    # Generate the filename
    filename = f'clock_{i + 1}.jpg'
    
    # Print the random time
    print(f"{random_hours}:{random_minutes}:{random_seconds}")
    
    # Generate and save the clock face
    generate_analog_clock(random_time, filename)
    
    # Add the filename to the list
    image_filenames.append(filename)

# Generate the markdown file with all the images
generate_markdown_file(image_filenames, 'clocks.md')
