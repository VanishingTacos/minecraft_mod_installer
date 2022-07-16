# a script to install minecraft mods

# import the necessary modules
import os

# find the minecraft directory
def find_minecraft_dir():
    # find the minecraft directory
    minecraft_dir = os.path.expanduser("~") + "\AppData\Roaming\.minecraft"
    # if the directory exists
    if os.path.exists(minecraft_dir):
        # return the directory
        return minecraft_dir
    # if the directory does not exist
    else:
        # return false
        return False
    
# if the directory does not exist then ask for the minecraft directory
def ask_for_minecraft_dir():
    # ask for the minecraft directory
    minecraft_dir = input("Enter the path to your minecraft directory: ")
    # if the directory exists
    if os.path.exists(minecraft_dir):
        # return the directory
        return minecraft_dir
    # if the directory does not exist
    else:
        # return false
        return False

# find the mod directory in the minecraft directory
def find_mod_dir(minecraft_dir):
    # find the mod directory
    mod_dir = minecraft_dir + "\mods"
    # if the directory exists
    if os.path.exists(mod_dir):
        # return the directory
        return mod_dir
    # if the directory does not exist
    else:
        # return false
        return False

# if the directory does not exist the create it
def create_mod_dir(minecraft_dir):
    # create the mod directory
    mod_dir = minecraft_dir + "\mods"
    # if the directory does not exist
    if not os.path.exists(mod_dir):
        # create the directory
        os.makedirs(mod_dir)
        # return the directory
        return mod_dir
    # if the directory does exist
    else:
        # return the directory
        return mod_dir


# get the mods_for_install directory
def get_mods_for_install_dir():
    # get the directory
    mods_for_install_dir = os.path.dirname(os.path.abspath(__file__)) + "\mods_for_install"
    # if the directory exists
    if os.path.exists(mods_for_install_dir):
        # return the directory
        return mods_for_install_dir
    # if the directory does not exist
    else:
        # return false
        return False

# get the installables directory
def get_installables_dir():
    # get the directory
    installables_dir = os.path.dirname(os.path.abspath(__file__)) + "\installables"
    # if the directory exists
    if os.path.exists(installables_dir):
        # return the directory
        return installables_dir
    # if the directory does not exist
    else:
        # return false
        return False


# install optifine from the installables directory
def install_optifine(installables_dir):
    # run the install command
    os.system(installables_dir + "\OptiFine.jar --install")
    print("Optifine has been opened. Please install it and close it.")

# install fabric from the installables directory
def install_fabric(installables_dir):
    # run the install command
    os.system(installables_dir + "\Fabric.exe")
    print("Fabric has been opened. Please install it and close it.")


# main function
def main():
    # find the minecraft directory
    minecraft_dir = find_minecraft_dir()
    # if the directory does not exist
    if minecraft_dir == False:
        # ask for the minecraft directory
        minecraft_dir = ask_for_minecraft_dir()
        # if the directory does not exist
        if minecraft_dir == False:
            # print an error message
            print("Error: Minecraft directory not found.")
            # exit the program
            exit()
    # if the directory does exist
    else:
        # find the mod directory
        mod_dir = find_mod_dir(minecraft_dir)
        # if the directory does not exist
        if mod_dir == False:
            # create the mod directory
            mod_dir = create_mod_dir(minecraft_dir)
            # if the directory does not exist
            if mod_dir == False:
                # print an error message
                print("Error: Mod directory not found.")
                # exit the program
                exit()
        # if the directory does exist
        else:
            # get the mods_for_install directory
            mods_for_install_dir = get_mods_for_install_dir()
            # if the directory does not exist
            if mods_for_install_dir == False:
                # print an error message
                print("Error: Mods for install directory not found.")
                # exit the program
                exit()
            # if the directory does exist
            else:
                # get the installables directory
                installables_dir = get_installables_dir()
                # if the directory does not exist
                if installables_dir == False:
                    # print an error message
                    print("Error: Installables directory not found.")
                    # exit the program
                    exit()
                # if the directory does exist
                else:
                    # install optifine
                    install_optifine(installables_dir)
                    # install fabric
                    install_fabric(installables_dir)
                    # exit the program
    # copy the mods to the mod directory
    os.system("copy " + mods_for_install_dir + " " + mod_dir )
    print(mods_for_install_dir + " " + mod_dir)
    # print a message
    print("Installation complete.")

# run the main function
main()
# end of file
