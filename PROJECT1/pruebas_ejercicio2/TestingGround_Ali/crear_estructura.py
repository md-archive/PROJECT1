import os
def project2_MAIN_structure():
    #
    # main_directory = "Project 2 Counting Calories"
    # def project2_MAIN_FOLDER():  
    #     project2_exists = os.path.exists(main_path)
    #     #
    #     if project2_exists == True:
    #         print(f"{main_directory} folder already exists")
    #     else:
    #         # crear fichero si no existe
    #         print(f"{main_directory} does not exist. Proceeding to create it.")
    #         os.mkdir(main_directory)
    # #
    friend1 = "robert"
    friend2 = "mary"
    def create_files():
        #
        calories_file = "calories.txt"
        #
        carrots = ['Carrots',160]
        peas = ['Peas',110]
        #
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, calories_file)
        file_exists = os.path.exists(filename)
        #
        if file_exists == True:
            print(f"File {calories_file} already exists")
        else:
            # crear fichero si no existe
            print(f"File {calories_file} does not exist. Proceeding to create it.")
            # Crear fichero vacio " open(filename, 'a').close() "
            open(filename, 'x')
        with open(filename, 'w', encoding='UTF8', newline='') as f:
            for line in carrots:
                if type(line) is int:
                    f.write(" " + str(line) + "\n")
                else:
                    f.write(line)
            for line in peas:
                if type(line) is int:
                    f.write(" " + str(line) + "\n")
                else:
                    f.write(line)
    #
    def robert_structure():
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname,friend1)
        robert_exists = os.path.exists(filename)
        if robert_exists == True:
            print(f"{robert_exists}'s folder already exists")
        else:
            # crear fichero si no existe
            print(f"{robert_exists}'s does not exist. Proceeding to create it.")
            os.mkdir(filename)
    #
        def robert_files():
                robert_weight = 'weight.txt'
                robert_1st_register = '01-01-2020.txt'
                robert_2nd_register = '03-01-2020.txt'
                #
                dirname = os.path.dirname(__file__)
                filename = os.path.join(dirname,friend1,robert_weight)
                file_exists = os.path.exists(filename)
                #
                robert_1st_evaluation = os.path.exists(dirname + friend1 + robert_1st_register)
                robert_2nd_evaluation = os.path.exists(dirname + friend1 + robert_2nd_register)
                #
                # CREAR WEIGHT.TXT PARA ROBERT
                #
                if file_exists == True:
                    print(f"File {robert_weight} on {friend1} already exists")
                else:
                    # crear fichero si no existe
                    print(f"File {robert_weight} on {friend1} does not exist. Proceeding to create it.")
                    # Crear fichero vacio " open(filename, 'a').close() "
                    open(filename, 'a').close()
                #
                # CREAR 01-01-2020.TXT PARA ROBERT
                #
                if robert_1st_evaluation == True:
                    print(f"File {robert_1st_register} on {friend1} already exists")
                else:
                    # crear fichero si no existe
                    print(f"File {robert_1st_register} on {friend1} does not exist. Proceeding to create it.")
                    # Crear fichero vacio " open(filename, 'a').close() "
                    first_txt = os.path.join(dirname,friend1,robert_1st_register)
                    open(first_txt, 'a').close()
                #
                # CREAR 03-01-2020.TXT PARA ROBERT
                #
                if robert_2nd_evaluation == True:
                    print(f"File {robert_2nd_register} on {friend1} already exists")
                else:
                    # crear fichero si no existe
                    print(f"File {robert_2nd_register} on {friend1} does not exist. Proceeding to create it.")
                    # Crear fichero vacio " open(filename, 'a').close() "
                    second_txt = os.path.join(dirname,friend1,robert_2nd_register)
                    open(second_txt, 'a').close()
        robert_files()
    robert_structure()
    #
    def mary_structure():
        dirname = os.path.dirname(__file__)
        filename = (os.path.join(dirname,friend2))
        mary_exists = os.path.exists(filename)
        if mary_exists == True:
            print(f"{mary_exists}'s already exists")
        else:
            print(f"{mary_exists}'s does not exist. Proceeding to create it.")
            os.mkdir(filename)
        def mary_files():
            mary_weight = 'weight.txt'
            mary_1st_register = '01-01-2020.txt'
            mary_2nd_register = '02-01-2020.txt'
            mary_3rd_register = '03-01-2020.txt'
            #
            dirname = os.path.dirname(__file__)
            filename = os.path.join(dirname,friend2,mary_weight)
            file_exists = os.path.exists(filename)
            #
            mary_1st_evaluation = os.path.exists(dirname + friend2 + mary_1st_register)
            mary_2nd_evaluation = os.path.exists(dirname + friend2 + mary_2nd_register)
            mary_3rd_evaluation = os.path.exists(dirname + friend2 + mary_3rd_register)
            #
            # CREAR WEIGHT.TXT PARA MARY
            #
            if file_exists == True:
                print(f"File {mary_weight} on {friend2} already exists")
            else:
                # crear fichero si no existe
                print(f"File {mary_weight} on {friend2} does not exist. Proceeding to create it.")
                # Crear fichero vacio " open(filename, 'a').close() "
                open(filename, 'a').close()
            #
            # CREAR 01-01-2020.TXT PARA MARY
            #
            if mary_1st_evaluation == True:
                print(f"File {mary_1st_register} from {friend2} already exists")
            else:
                print(f"File {mary_1st_register} from {friend2} does not exist. Proceeding to create it.")
                first_txt = os.path.join(dirname,friend2,mary_1st_register)
                open(first_txt, 'a').close()
            #
            # CREAR 02-01-2020.TXT PARA MARY
            #
            if mary_2nd_evaluation == True:
                print(f"File {mary_2nd_register} from {friend2} already exists")
            else:
                print(f"File {mary_2nd_register} from {friend2} does not exist. Proceeding to create it.")
                second_txt = os.path.join(dirname,friend2,mary_2nd_register)
                open(second_txt, 'a').close()
            #
            # CREAR 03-01-2020.TXT PARA MARY
            #
            if mary_3rd_evaluation == True:
                print(f"File {mary_3rd_register} from {friend2} already exists")
            else:
                print(f"File {mary_3rd_register} from {friend2} does not exist. Proceeding to create it.")
                third_txt = os.path.join(dirname,friend2,mary_3rd_register)
                open(third_txt, 'a').close()
            #  
        mary_files() 
    mary_structure()
    create_files()
    #project2_MAIN_FOLDER()
project2_MAIN_structure()