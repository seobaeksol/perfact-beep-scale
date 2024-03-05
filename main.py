import winsound
import random

# the frequency of each note by octave
sound_hz_table = [
    [
        32.7032,  # C(Do)
        34.6478,  # C#
        36.7081,  # D(Re)
        38.8909,  # D#
        41.2034,  # E(Mi)
        43.6535,  # F(Fa)
        46.2493,  # F#
        48.9994,  # G(Sol)
        51.9131,  # G#
        55.0,  # A(La)
        58.2705,  # A#
        61.7354,  # B(Si)
    ],
    [
        65.4064,
        69.2957,
        73.4162,
        77.7817,
        82.4069,
        87.3071,
        92.4986,
        97.9989,
        103.8262,
        110.0,
        116.5409,
        123.4708,
    ],
    [
        130.8128,
        138.5913,
        146.8324,
        155.5635,
        164.8138,
        174.6141,
        184.9972,
        195.9977,
        207.6523,
        220.0,
        233.0819,
        246.9417,
    ],
    [
        261.6256,
        277.1826,
        293.6648,
        311.127,
        329.6276,
        349.2282,
        369.9944,
        391.9954,
        415.3047,
        440.0,
        466.1638,
        493.8833,
    ],
    [
        523.2511,
        554.3653,
        587.3295,
        622.254,
        659.2551,
        698.4565,
        739.9888,
        783.9909,
        830.6094,
        880.0,
        932.3275,
        987.7666,
    ],
    [
        1046.5023,
        1108.7305,
        1174.6591,
        1244.5079,
        1318.5102,
        1396.9129,
        1479.9777,
        1567.9817,
        1661.2188,
        1760.0,
        1864.655,
        1975.5332,
    ],
    [
        2093.0045,
        2217.461,
        2349.3181,
        2489.0158,
        2637.0205,
        2793.8259,
        2959.9554,
        3135.9635,
        3322.4376,
        3520.0,
        3729.31,
        3951.0664,
    ],
    [
        4186.009,
        4434.9221,
        4698.6363,
        4978.0317,
        5274.0409,
        5587.6517,
        5919.9108,
        6271.927,
        6644.8752,
        7040.0,
        7458.62,
        7902.1329,
    ],
]

note_name_dict = {
    1: "Do",
    2: "Do#",
    3: "Re",
    4: "Re#",
    5: "Mi",
    6: "Fa",
    7: "Fa#",
    8: "Sol",
    9: "Sol#",
    10: "La",
    11: "La#",
    12: "Si",
}

heptatonic_scale = [0, 2, 4, 5, 7, 9, 11]

def geuss_the_note(target_octave = -1, use_heptatonic_scale = False):
    # play a random note for 1000 ms (1 second)
    # and get a user input which user guess the note
    # if the user guess the note correctly, count the score
    # do this until the socre is 10
    score = 0
    len_octave = len(sound_hz_table)
    len_note = len(sound_hz_table[0])
    try_count = 0
    while score < 10:
        # play a random note
        octave = random.randint(0, len_octave - 1) if target_octave == -1 else target_octave - 1
        note = heptatonic_scale[random.randint(0, 6)] if use_heptatonic_scale else random.randint(0, len_note - 1)
        random_note = int(sound_hz_table[octave][note])
        print("Sound Playing...")
        winsound.Beep(random_note, 1000)  # winsound.Beep(frequency, duration)
        # get a user input
        user_guess_octave = str(target_octave)
        if octave == -1:
            user_guess_octave = input("Guess the octave: ")
        user_guess_note = input(
            "Guess the note (1: Do, 2: Do#, 3: Re, 4: Re#, 5: Mi, 6: Fa, 7: Fa#, 8: Sol, 9: Sol#, 10: La, 11: La#, 12: Si): "
        )
        # print user choice and color the text in gray and the correct answer
        try_count += 1
        print("\033[90mYou guessed", note_name_dict[int(user_guess_note)], "in octave", user_guess_octave, "\033[0m")
        if user_guess_octave == str(octave + 1) and user_guess_note == str(note + 1):
            score += 1
            # print the score and color the text in green
            print(f"\033[92mCorrect! Your score is {score} of {try_count}\033[0m")
        else:
            # print the score and color the text in red
            print(f"\033[91mWrong! Your score is {score} of {try_count}\033[0m")
        print("The note is", note_name_dict[note + 1], "in octave", octave + 1)
    # print win message and correct percentage and color the text in blue
    print(f"\033[94mYou win! Your accuracy rate is {score/try_count*100:2.2f}%\033[0m")
def practice_octave(octave = 4, use_heptatonic_scale = False):
    scale = heptatonic_scale if use_heptatonic_scale else range(12)
    for note in scale:
        print("The note is", note_name_dict[note + 1], "in octave", octave)
        winsound.Beep(int(sound_hz_table[octave-1][note]), 1000)


if __name__ == "__main__":
    # user can choose to guess the note or practice the octave
    while True:
        print("1. Guess the note")
        print("2. Practice the octave")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            # user can choose the scale and the octave to practice
            print("Choose the scale to practice")
            print("1. Heptatonic scale")
            print("2. Chromatic scale")
            scale_choice = input("Enter your choice: ")
            if scale_choice != "1" and scale_choice != "2":
                print("Invalid choice")
                continue
            print("Choose the octave to practice (1-8, all: -1)")
            octave = int(input("Enter the octave: "))
            if octave < -1 or octave > 8 or octave == 0:
                print("Invalid octave")
                continue
            else:
                geuss_the_note(octave, scale_choice == "1")
        elif choice == "2":
            # user can choose the scale and the octave to practice
            print("Choose the scale to practice")
            print("1. Heptatonic scale")
            print("2. Chromatic scale")
            scale_choice = input("Enter your choice: ")
            if scale_choice != "1" and scale_choice != "2":
                print("Invalid choice")
                continue
            print("Choose the octave to practice (1-8)")
            octave = int(input("Enter the octave: "))
            if octave < 1 or octave > 8:
                print("Invalid octave")
                continue
            else:
                practice_octave(octave, scale_choice == "1")
        elif choice == "3":
            break
        else:
            print("Invalid choice")