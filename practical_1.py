user_answer = ""

special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

questions_admission = ['admission']
questions_fees = ['fees']
questions_course_offered = ['course']
questions_contact = ['contact']
questions_brochure = ['brochure']
questions_placement = ['placement']
questions_scholarship = ['scholarship']
questions_campus = ['campus']
questions_about = ['about']
questions_FAQ = ['faq'] 


print("😎Bot: Hi there! Welcome to Mihir's PC!. You're now face to face with Bot, your college assistant.")

user_name = input("Please enter your name: ")
#user_email = input("Bot: Please enter your email: ")

print(f"😎Bot: Welcome {user_name} to Admission Cell 😄.")
print(f"😎Bot: Tell me, How can I help you today ?")

flag = True  # used for control the loop

while flag:
    user_answer = input("User: ").lower()

    for char in user_answer:  # for remove the special char in user input
        if char in special_chars:
            user_answer = user_answer.replace(char, '')
    # print(user_answer)

    words = user_answer.split()  # split the string of user input
    #print(words)

    for word in words:
        if word in questions_fees:
            print("😎Bot: Fees of It will be around 57,000 (57k) according to 2020-21")
            flag = True
            break

        elif word in questions_admission:
            print("😎Bot: Admissions at Ganpat University are open for the academic year 2021 -22 for Engineering,\n "
                  "Management, Computer Applications, Pharmacy, Sciences, Commerce & Social Science, Architecture,\n "
                  "Design & Planning, Maritime Studies & Other Programs")
            flag = True
            break

        elif word in questions_course_offered:
            print(
                '😎Bot: Ganpat University is widely known for Strong Industry-Academia-Linked Higher Education Model '
                'and \n'
                'Centres of Excellence, only university in Gujarat offering heterogeneous & specialised programs. \n'
                'We offered specialised (sector/industry/technology focused) programs in Engineering, Management, \n'
                'Computer Applications, Pharmacy, Sciences, Commerce & Social Science, Architecture, \n'
                'Design & Planning, Maritime Studies & Others.')
            flag = True
            break

        elif word in questions_contact:
            print("😎Bot: GANPAT UNIVESITY \nAddress:  Ganpat University, Ganpat Vidyanagar,Mehsana-Gozaria Highway,\n"
                  "PO - 384012, North Gujarat,\nINDIA Working Time: 09.00 am to 04.00 pm\nEmail: "
                  "info@ganpatuniversity.ac.in\nToll Free No.: 1800 233 12345\nAdmissions Cell Ganpat University Toll "
                  "Free No. 1800 233 12345 | +91-2762-226000\nEmail: admissions@ganpatuniversity.ac.in,"
                  "int.admission@ganpatuniversity.ac")
            flag = True
            break

        elif word in questions_brochure:
            print("😎Bot: This is College Brochure!\n http://online.fliphtml5.com/lpcv/rtuf/#p=10")
            flag = True
            break

        elif word in questions_placement:
            print("😎Bot: Thinking about placements? Worry not, you are at the right place!\nGanpat University "
                  "Placement"
                  "Highlights 2022\nHighest Package	Rs. 12 lakhs p.a. (Engineering)\nAverage Package	Rs. 3.1 lakhs "
                  "p.a.\nNumber of Students Placed	1380\n% of students placed	95+ %\nMedian Package	Rs. 1.9 lakhs "
                  "p.a.")
            flag = True
            break

        elif word in questions_scholarship:
            print("😎Bot: Many types of scholarship are offered to students of Ganpat University such as merit-based, \n"
                  "need-based, student-specific, career-specific and college-specific.Ganpat University offers \n"
                  "Scholarship worth Rs. 3.00 Crore every year to more than 2000 students.We strongly believe that \n"
                  "financial constraints should not be an obstacle for a student to have access to quality education. "
                  "\n"
                  "So, the University offers scholarships to students on various parameters")
            flag = True
            break

        elif word in questions_campus:
            print("😎Bot: Apart from state-of-the-art classrooms, Ganpat University campus is equipped with the "
                  "latest \n"
                  "facilities including high-end workshops, laboratories, simulators, rich library, sports grounds, \n"
                  "recreational facilities, amphitheater, and seminar halls.Here is the list of facilities we provide "
                  "\n"
                  "to our students.")
            flag = True
            break

        elif word in questions_about:
            print("😎Bot: Ganpat University is a well Reputed State Self Finance Private University established in "
                  "2005 \n"
                  "through the State Legislative Act no 19 of 2005, Government of Gujarat and recognized by the UGC \n"
                  "under the section 2(f) of the UGC Act, 1956. Ganpat University has been ranked amongs top 5 self \n"
                  "finance state Universites under Gujarat State Institutional Ranking Framework (GSIRF 2021) by \n"
                  "Government of Gujarat.")
            flag = True
            break

        elif word in questions_FAQ:
            print("😎Bot: I know you wanna inquire more. Hence, here are your options below.\n"
                  "https://www.ganpatuniversity.ac.in/campus-lifes/transportation")
            flag = True
            break

        elif user_answer == "exit":
            print(f"😘Bot: {user_name} See you!")
            flag = False
            break

    else:
        print(f"😒Bot: Sorry I don't understand what are you trying to say!\n Please Reenter Your Query:")
