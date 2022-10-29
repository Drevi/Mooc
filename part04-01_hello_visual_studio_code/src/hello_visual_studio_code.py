# Write your solution here
while True:
    editor = input("Editor:")

    if "visual studio code" == editor.lower():
        print("an excellent choice!")
        break
    if "notepad" == editor.lower() or "word" == editor.lower():
        print("awful")
    else:
        print("not good")