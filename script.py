import random
import easygui

# List of bodyweight exercises to pick from
exerciseList = [
    "Bodyweight Bridge",
    "Bodyweight Single Leg Deadlift",
    "Bodyweight Y Squats",
    "Bodyweight Forward Lunge",
    "Bodyweight Lateral Squat",
    "Bodyweight Shoulder Taps",
    "Bodyweight Static Lunge",
    "Bodyweight Bird Dog",
    "Bodyweight Back Extensions",
    "Bodyweight Yoga Squat",
    "Bodyweight Bob & Weave",
    "Bodyweight Elbow to Knee",
    "Bodyweight Hip Openers",
    "Bodyweight Fast Mountain Climbers",
    "Bodyweight Side Plank with Rotation",
    "Bodyweight Push Ups", 
    "Bodyweight Side Lunge with a Reach", 
    "Bodyweight Scissors",
    "Bodyweight High Knees",
    "Bodyweight Cross Overs",
    "Bodyweight Side Shuffles",
    "Bodyweight Dead Bug",
    "Bodyweight Bird Dog with Rotation",
    "Bodyweight Side Plank",
    "Bodyweight Double Lunge with Reach",
    "Bodyweight Cross Body Mountain Climbers",
    "Bodyweight Squat Thrusts",
    "Bodyweight Dirty Dogs",
    "Bodyweight Burpees",
    "Bodyweight Dive Bomber Push Ups",
    "Bodyweight Side Plank with Extension",
    "Bodyweight Jump Squats",
    "Bodyweight Plank to Push Up",
    "Bodyweight Single Leg Up and Down Dogs",
    "Bodyweight Figure 4 Mountain Climbers",
    "Bodyweight T Push Ups",
    "Bodyweight Reverse Lunge with Lateral Reach",
    "Bodyweight Breakdancer Push Ups",
    "Bodyweight Reverse Lunge and Hop",
    "Bodyweight Skaters",
    "Bodyweight Reverse Diagonal Lunge with Reach",
    "Bodyweight Cross Body Extension",
    "Bodyweight Jumping Lunges",
    "Bodyweight Kangaroos",
    "Bodyweight Mountain Climber Push Ups"
]

# List of bodyweight warm up exercises to pick from
warmUpList = [
    "Jumping",
    "Run in place",
    "Jumping jacks"
]


warmUP = (f"Warm up: {random.choice(warmUpList)} x {random.randint(50, 100)} repetitions\n")
execOne = (f"Execise #1: {random.choice(exerciseList)} x {random.randint(5, 10)} repetitions\n")
execTwo = (f"Execise #2: {random.choice(exerciseList)} x {random.randint(5, 10)} repetitions\n")
execThree = (f"Execise #3: {random.choice(exerciseList)} x {random.randint(5, 10)} repetitions\n")

#Use easygui to display window on the screen
easygui.msgbox(
    warmUP + execOne + execTwo + execThree, 
    title="TIME TO MOVE")
