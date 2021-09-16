import math
import io

class StableMarriable(object):
    n = 0  # Variable to store men and women
    m_id = []  # An array to maintain id to name mapping for men
    wm_id = []  # An array to maintain id to name mapping for women
    wife = []
    husband = []
    men_preference = [[]]
    women_preference = [[]]
    women_preference_inverse = [[]]  # Avoid increasing time complexity we define inverse
    count = []
    file = None
    no_of_iterations = 0

    def main(args):
        # getting the input from file or from cmd prompt
        PrefList_names = getPrefList()
        # Converting the name to ids
        PrefList_ids = convert_to_id(PrefList_names)
        wife = [0 for _ in range(n + 1)]
        husband = [0 for _ in range(n + 1)]
        count = [0 for _ in range(n + 1)]
        # setting the preference order for men
        set_men_preference_order(PrefList_ids)
        # setting the inverse of preference order for women
        set_women_inverse_preference(PrefList_ids)
        # Execute Propose-and-reject algorithm
        execute_Gale_Shapely()
        output = ""
        i = 1
        while i <= n:
            # converting the output ( stable matchs )ids to names
            output += m_id[i] + ", " + wm_id[wife[i]] + "\n"
            i += 1
        output = output[0:len(output) - 1]
        print("Stable matchs are \n" + output + "\n")
        output_file_name = "Output"
        try:
            output_file_name += "_for_" + file.getName()
        except Exception as e:
            pass
        writer = BufferedWriter(FileWriter(output_file_name))
        # writing the output to file
        writer.write(output)
        print("The displayed result is witen to '" + output_file_name + "'")
        writer.close()

def execute_Gale_Shapely():
    # data structure to maintain free men
    stack = Stack()
    
    # Algorithm kicks-off here
    # 1. Initialize each person to be free
    i = 1
    while i <= n:
        stack.push(n - i + 1)
        wife[i] = 0
        husband[i] = 0
        count[i] = 0
        i += 1
        
    # Start loop with terminating condition
    while not stack.empty():
        # Choose a man m
        m = stack.pop()
        
        # Choose a women from mens pref list to whom m has not yet proposed
        w = men_preference[m][count[m] + 1]
        count[m] += 1
        
        # If the women is free => assign m and w to be engaged
        if husband[w] == 0:
            wife[m] = w
            husband[w] = m
        # 5.2. if w prefers m over m_prime(current assignment) m and w will be engaged and m_prime will be set as free(by pushing to stack)
        elif women_preference_inverse[w][m] < women_preference_inverse[w][husband[w]]:
            m_prime = husband[w]
            husband[w] = m
            wife[m] = w
            wife[m_prime] = 0
            stack.push(m_prime)
            
        # 5.3. w rejects m => m is set to free(by pushing to stack)
        else:
            stack.push(m)
        no_of_iterations += 1

        def getPrefList():
            sc = Scanner(System.__in__)
            print("Please choose a method to select PrefList")
            print("1. From text file")
            print("2. Enter the Preference list here")
            print("Choose your option (1 or 2):", end='')
            opt = None
            opt = sc.nextInt()
            PrefList = ""
            if opt == 1:
                print("Enter file path(Eg:'input1.txt' or 'C:\\Users\\acadi\\prob_1\\input1.txt'):", end='')
                sc.nextLine()
                fileName = sc.nextLine()
                file = File(fileName)
                PrefList = str(Files.readAllBytes(Paths.get(fileName)))
                n = math.trunc((PrefList.split("\n").length - 1) / float(2))
            elif opt == 2:
                print("Enter the number of Men / Women (value of n):", end='')
                n = sc.nextInt()
                sc.nextLine()
                print(
                    "Enter the preference lists � n lines for men and n lines for women with one empty line to separate the two lists")
                i = 1
                while i <= (2 * n + 1):
                    PrefList += sc.nextLine() + "\n"
                    i += 1
                PrefList = PrefList[0:len(PrefList) - 1]
            else:
                print("Invalid choice: Please run the program again and choose one from above options!!")
            return PrefList

        def getId_name(name):
            i = None
            i = 1
            while i <= n:
                if m_id[i] is name or wm_id[i] is name:
                    break
                i += 1
            return i

        def convert_to_id(PrefList_n):
            m_id = [None for _ in range(n + 1)]
            wm_id = [None for _ in range(n + 1)]
            new_list = ""
            i = 1
            while i <= n:
                temp = PrefList_n.split("\n")[i - 1].split(",")[0].trim()
                m_id[i] = temp
                temp = PrefList_n.split("\n")[n + i].split(",")[0].trim()
                wm_id[i] = temp
                i += 1
            i = 1
            while i <= (2 * n + 1):
                if i != n + 1:
                    Curr_line = PrefList_n.split("\n")[i - 1].split(",")
                    j = 0
                    while j < len(Curr_line):
                        new_list += getId_name(Curr_line[j].trim()) + ","
                        j += 1
                    new_list = new_list[0:len(new_list) - 1]
                new_list += "\n"
                i += 1
            if str(n + 1) in new_list:
                print("Error: can not convert names to ids properly, check the input data")
            return new_list

        def set_men_preference_order(Pref):

            men_preference = new
            int[n + 1][n + 1]
            i = 1
            while i <= n:
                c_line = Pref.split("\n")[i - 1]
                j = 1
                while j < c_line.split(",").length:
                    men_preference[i][j] = int(c_line.split(",")[j])
                    j += 1
                i += 1

        def set_women_inverse_preference(Pref):
            women_preference = new
            int[n + 1][n + 1]
            i = 1
            while i <= n:
                c_line = Pref.split("\n")[n + i]
                j = 1
                while j < c_line.split(",").length:
                    women_preference[i][j] = int(c_line.split(",")[j])
                    j += 1
                i += 1
            women_preference_inverse: object = new
            int[n + 1][n + 1]
            i = 1
            while i <= n:
                j = 1
                while j <= n:
                    women_preference_inverse[i][women_preference[i][j]] = j
                    j += 1
                i += 1