import glob
import os


def renpy_music_check(directory_dir):
    dir_search = glob.glob(str(directory_dir))
    if len(dir_search) < 1:
        f.write(str('# these files  contain no images'))
    else:
        for i in range(0, len(dir_search)):
            ogg_list = glob.glob(dir_search[i] + "*ogg")
            mp3_list = glob.glob(dir_search[i] + "*mp3")
            wav_list = glob.glob(dir_search[i] + "*wav")
            folder_name = str(os.path.split(os.path.dirname(dir_search[i]))[-1])
            if int(len(ogg_list) + len(mp3_list)+ len(wav_list)) >= 1:
                ogg_folder = (folder_name if folder_name != "images" else " ")
                f.write(str("# these are images in " + dir_search[i]) + "\n")
                for x in range(0, len(ogg_list)):
                    f.write(str(
                        "define " + "audio." + ogg_folder + "_" + os.path.splitext(os.path.basename(ogg_list[x]))[
                            0] + " = " + '"' + ogg_list[
                            x] + '"') + "\n")

                for y in range(0, len(mp3_list)):
                    mp3_folder = (folder_name if folder_name != "images" else " ")
                    f.write(str(
                        "define " + "audio." + mp3_folder + " = " + '"' + mp3_list[
                            y] + '"') + "\n")
                    # print(str(
                    #     "image " + mp3_folder[0] + " = " + '"' + mp3_list[
                    #         y] + '"') + "\n")
                for a in range(0, len(wav_list)):
                    f.write(str(
                        "define " + "audio." + wav_folder + "_" + os.path.splitext(os.path.basename(wav_list[a]))[
                            0] + " = " + '"' + wav_list[
                            a] + '"') + "\n")


f = open("audio_directory.rpy", "w")

f.write(str("#Thanks for using my script! find more at https://github.com/tiny-witch" + "\n"))
f.write(str("# This file will include mp3 , ogg, wav files only" + "\n"))
f.write(str("# Here are the directories this file searched for audio:" + "\n"))
dir_list = ["*", "*/", "*/*/"]
for lst in range(0, len(dir_list)):
    temp_list = glob.glob(str(dir_list[lst]))
    # print("temp list is: ", temp_list)
    # print(temp_list[0])
    # print(len(temp_list))

    k = int(len(temp_list))
    # print(k)

    for r in range(0, k):
        # print(r)
        # f.write(str((" "*8)+"# " + str(temp_list[r]) + "\n"))
        if os.path.isdir(temp_list[r]):
            f.write(str("# " + (" " * 8) + ("-" * 8 * lst) + str(temp_list[r]) + "\n"))
            # f.write(str((" " * 8) + "# " + "is directory" + "\n"))
# print('\n'.join([str(glob.glob(str(dir_list[lst]))) for lst in range(0, len(dir_list))]))
for q in range(0, len(dir_list)):
    renpy_music_check(dir_list[q])

f.close()

if __name__ == "__main__":
    import os
    import glob

    f = open("audio_directory.rpy", "w")

    f.write(str("# Thanks for using my script! find more at https://github.com/tiny-witch" + "\n"))
    f.write(str("# This file will include mp3 , ogg, wav files only" + "\n"))
    f.write(str("# Here are the directories this file searched for audio:" + "\n"))
    dir_list = ["*", "*/", "*/*/"]
    for lst in range(0, len(dir_list)):
        temp_list = glob.glob(str(dir_list[lst]))
        # print("temp list is: ", temp_list)
        # print(temp_list[0])
        # print(len(temp_list))

        k = int(len(temp_list))
        # print(k)

        for r in range(0, k):
            # print(r)
            # f.write(str((" "*8)+"# " + str(temp_list[r]) + "\n"))
            if os.path.isdir(temp_list[r]):
                f.write(str("# " + (" " * 8) + ("-" * 8 * lst) + str(temp_list[r]) + "\n"))
                # f.write(str((" " * 8) + "# " + "is directory" + "\n"))
    # print('\n'.join([str(glob.glob(str(dir_list[lst]))) for lst in range(0, len(dir_list))]))
    for q in range(0, len(dir_list)):
        renpy_music_check(dir_list[q])

    f.close()

