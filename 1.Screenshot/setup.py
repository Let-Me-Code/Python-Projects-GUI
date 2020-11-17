from cx_Freeze import setup, Executable
setup(name = "SS",
      version = "0.1",
      author = "Abhinav Shukla",
      description = "Takes Screenshot",
      executables = [Executable("screenshot.py",
                     icon = "screen.ico",
                     shortcutName = "SS",
                     shortcutDir = "DesktopFolder")]

      )
