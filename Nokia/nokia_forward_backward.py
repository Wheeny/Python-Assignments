menu_functions = """
NOKIA MENU MAP
List of Menu Functions

Select Option

1. Phone book
2. Messages
3. Chat
4. Call Register
5. Tones
6. Settings
7. Call Divert
8. Games
9. Calculator
10. Reminders
11. Clock
12. Profiles
13. Sim Services
0.  Exit

 """


phone_book = """

Select Option

1. Search
2. Service Nos.
3. Add Name
4. Erase
5. Edit
6. Assign Tone
7. Send b'card
8. Options
9. Speed Dials
10. Voice Tags
0. Main menu

"""

options_menu = """

Select Option

1. Type of View
2. Memory Status
0. Back

"""


messages_menu = """

Select Option

1. Write Messages
2. Inbox
3. Outbox
4. Picture Messages
5. Templates
6. Smileys
7. Message Settings
8. Info Service
9. Voice Mailbox Number
10. Service Command Editor
0.  Back

"""


message_settings_menu = """

Select Option

1. Set 1
2. Common
0. Back

"""


set1_menu = """

Select Option

1. Message Centre Number
2. Message Sent as
3. Message Validity
0. Back

"""


common_menu = """

Select Option

1. Delivery Reports
2. Reply via same centre
3. Character Support
0. Back

"""


call_register_menu = """

Select Option

1. Missed Calls
2. Received Calls
3. Dialled Numbers
4. Erase recent call lists
5. Show call duration
6. Show call costs
7. Call cost settings
8. Prepaid Credit
0. Back

"""


show_call_duration_menu =  """

Select Option

1. Last call duration
2. All calls' duration
3. Received calls duration
4. Dialled calls' duration
5. Clear timers
0. Back

"""


show_call_costs_menu =  """

Select Option

1. Last call cost
2. All calls' costs
3. Clear counters
0. Back

"""


call_cost_settings_menu =  """

Select Option

1. Call cost limits
2. Show costs in
0. Back

"""


tones_menu = """

Select Option

1. Ringing Tone
2. Ringing Volume
3. Incoming call alert
4. Composer
5. Message alert tone
6. Keypad tones
7. Warning and game tones
8. Vibrating alert
9. Screen saver
0. Back

"""


settings_menu = """

Select Option

1. Call settings
2. Phone settings
3. Security settings
4. Restore factory settings
0. Back

"""


call_settings_menu = """

Select Option

1. Automatic redial
2. Speed dialling
3. Call waiting options
4. Own number sending
5. Phone line in use
6. Automatic Answer
0. Back

"""


phone_settings_menu = """

Select Option

1. Language
2. Cell info display
3. Welcome note
4. Network selection
5. Lights
6. Confirm sim service actions
0. Back

"""


security_settings_menu = """

Select Option

1. PIN code request
2. Call barring service
3. Fixed dialling
4. Closed user group
5. Phone security
6. Change access codes
0. Back

"""


clock_menu = """

Select Option

1. Alarm clock
2. Clock settings
3. Date setting
4. Stopwatch
5. Countdown timer
6. Auto update of date and time
0. Back

"""


running = True
phone_book_running = True
options_running = True
messages_running = True
message_settings_running = True
set1_running = True
common_running = True
call_register_running = True
show_call_duration_running = True
show_call_costs_running = True
call_cost_settings_running = True
tones_running = True
settings_running = True
call_settings_running = True
phone_settings_running = True
security_settings_running = True
clock_running = True


while running:
    print(menu_functions)
    menu_functions_list = int(input())

    match menu_functions_list:
        case 1: 
            print("Phone book")
            while phone_book_running:
                print(phone_book)
                phone_book_list = int(input())
             
                match phone_book_list:
                    case 1: 
                        print("Search")
                    case 2:
                        print("Service Nos.")
                    case 3: 
                        print("Add Name")
                    case 4: 
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6: 
                        print("Assign Tone")
                    case 7: 
                        print("Send b'card")
                    case 8:
                        print("Options")
                        while options_running:
                            print(options_menu)
                            options_menu_list = int(input())

                            match options_menu_list:
                                case 1: 
                                    print("Type of View")
                                case 2: 
                                    print("Memory Status")
                                case 0: 
                                    options_running = False
                                case _: 
                                    print("Invalid Input")

                      
                    case 9: 
                        print("Speed Dials")
                    case 10: 
                        print("Voice Tags")
                    case 0:
                        phone_book_running = False
                    case _: 
                        print("Invalid Input")
          
          
        case 2: 
            print("Messages")
            while messages_running:
                print(messages_menu)
                messages_menu_list = int(input())
                
                match messages_menu_list:
                    case 1: 
                        print("Write Messages")
                    case 2: 
                        print("Inbox")
                    case 3: 
                        print("Outbox")
                    case 4: 
                        print("Picture Messages")
                    case 5:
                        print("Templates")
                    case 6: 
                        print("Smileys")
                    case 7: 
                        print("Message Settings")
                        while message_settings_running:
                            print(message_settings_menu)
                            message_settings_menu_list = int(input())

                            match message_settings_menu_list:

                                case 1: 
                                    print("Set 1")
                                    while set1_running:
                                        print(set1_menu)
                                        set1_menu_list = int(input())
                               
                                        match set1_menu_list:
                                            case 1: 
                                                print("Message Centre Number")
                                            case 2: 
                                                print("Message Sent as")
                                            case 3: 
                                                print("Message Validity")
                                            case 0: 
                                                set1_running = False
                                            case _: 
                                                print("Invalid Input")
                        

                                case 2: 
                                    print("Common")
                                    while common_running:
                                        print(common_menu)
                                        common_menu_list = int(input())

                                        match common_menu_list:
                                            case 1: 
                                                print("Delivery Reports")
                                            case 2: 
                                                print("Reply via same centre")
                                            case 3: 
                                                print("Character Support")
                                            case 0: 
                                                common_running = False          
                                            case _: 
                                                print("Invalid Input")
                        

                                case 0: 
                                    message_settings_running = False
                                case _: 
                                    print("Invalid Input")
                    
                    
                    case 8:
                        print("Info Service")
                    case 9: 
                        print("Voice Mailbox Number")
                    case 10: 
                        print("Service Command Editor")
                    case 0: 
                        messages_running = False
                    case _: 
                        print("Invalid Input")
              
              
        case 3: 
            print("Chat")
        case 4: 
            print("Call Register")
            while call_register_running:
                print(call_register_menu)
                call_register_menu_list = int(input())
                    
                match call_register_menu_list:
                    case 1: 
                        print("Missed Calls")
                    case 2: 
                        print("Received Calls")
                    case 3: 
                        print("Dialled Numbers")
                    case 4: 
                        print("Erase recent call lists")
                    case 5:
                        print("Show call duration")
                        while show_call_duration_running:
                            print(show_call_duration_menu)
                            show_call_duration_menu_list = int(input())
                            
                            match show_call_duration_menu_list:
                                case 1: 
                                    print("Last call duration")
                                case 2: 
                                    print("All calls' duration")
                                case 3: 
                                    print("Received calls duration")
                                case 4: 
                                    print("Dialled calls' duration")
                                case 5:
                                    print("Clear timers")
                                case 0:
                                    show_call_duration_running = False
                                case _:
                                    print("Invalid Input")
                        
                        
                    case 6: 
                        print("Show call costs")
                        while show_call_costs_running:
                            print(show_call_costs_menu)
                            show_call_costs_menu_list = int(input())
                            
                            match show_call_costs_menu_list:
                                case 1: 
                                    print("Last call cost")
                                case 2: 
                                    print("All calls' costs")
                                case 3: 
                                    print("Clear counters")
                                case 0:
                                    show_call_costs_running = False
                                case _:
                                    print("Invalid Input")
                        

                    case 7: 
                        print("Call cost settings")
                        while call_cost_settings_running:
                            print(call_cost_settings_menu)
                            call_cost_settings_menu_list = int(input())
                            
                            match call_cost_settings_menu_list:
                                case 1: 
                                    print("Call cost limits")
                                case 2: 
                                    print("Show costs in")
                                case 0:
                                    call_cost_settings_running = False
                                case _:
                                    print("Invalid Input")
                        

                    case 8: 
                        print("Prepaid Credit")
                    case 0: 
                        call_register_running = False
                    case _: 
                        print("Invalid Input")
             
              
        case 5:
            print("Tones")
            while tones_running:
                print(tones_menu)
                tones_menu_list = int(input())
                            
                match tones_menu_list:
                    case 1: 
                        print("Ringing Tone")
                    case 2: 
                        print("Ringing Volume")
                    case 3: 
                        print("Incoming call alert")
                    case 4: 
                        print("Composer")
                    case 5:
                        print("Message alert tone")
                    case 6: 
                        print("Keypad tones")
                    case 7: 
                        print("Warning and game tones")
                    case 8:
                        print("Vibrating alert")
                    case 9:
                        print("Screen saver")
                    case 0:
                        tones_running = False
                    case _:
                        print("Invalid Input")
    
   
        case 6: 
            print("Settings")
            while settings_running:
                print(settings_menu)
                settings_menu_list = int(input())
                            
                match settings_menu_list:
                    case 1: 
                        print("Call settings")
                        while call_settings_running:
                            print(call_settings_menu)
                            call_settings_menu_list = int(input())
                            
                            match call_settings_menu_list:
                                case 1: 
                                    print("Automatic redial")
                                case 2: 
                                    print("Speed dialling")
                                case 3: 
                                    print("Call waiting options")
                                case 4: 
                                    print("Own number sending")
                                case 5:
                                    print("Phone line in use")
                                case 6:
                                    print("Automatic Answer")
                                case 0:
                                    call_settings_running = False
                                case _:
                                    print("Invalid Input")
                
                
                    case 2: 
                        print("Phone settings")
                        while phone_settings_running:
                            print(phone_settings_menu)
                            phone_settings_menu_list = int(input())
                            
                            match phone_settings_menu_list:
                                case 1: 
                                    print("Language")
                                case 2: 
                                    print("Cell info display")
                                case 3: 
                                    print("Welcome note")
                                case 4: 
                                    print("Network selection")
                                case 5:
                                    print("Lights")
                                case 6:
                                    print("Confirm sim service actions")
                                case 0:
                                    phone_settings_running = False
                                case _:
                                    print("Invalid Input")
                
                
                    case 3: 
                        print("Security settings")
                        while security_settings_running:
                            print(security_settings_menu)
                            security_settings_menu_list = int(input())
                            
                            match security_settings_menu_list:
                                case 1: 
                                    print("PIN code request")
                                case 2: 
                                    print("Call barring service")
                                case 3: 
                                    print("Fixed dialling")
                                case 4: 
                                    print("Closed user group")
                                case 5:
                                    print("Phone security")
                                case 6:
                                    print("Change access codes")
                                case 0:
                                    security_settings_running = False
                                case _:
                                    print("Invalid Input")
                
                
                    case 4: 
                        print("Restore factory settings")
                    case 0:
                        settings_running = False
                    case _:
                        print("Invalid Input")
      
      
        case 7: 
            print("Call Divert")
        case 8:
            print("Games")
        case 9: 
            print("Calculator")
        case 10: 
            print("Reminders")
        case 11: 
            print("Clock")
            while clock_running:
                print(clock_menu)
                clock_menu_list = int(input())
                            
                match clock_menu_list:
                    case 1: 
                        print("Alarm clock")
                    case 2: 
                        print("Clock settings")
                    case 3: 
                        print("Date setting")
                    case 4: 
                        print("Stopwatch")
                    case 5:
                        print("Countdown timer")
                    case 6:
                        print("Auto update of date and time")
                    case 0:
                        clock_running = False
                    case _:
                        print("Invalid Input")
          
          
        case 12: 
            print("Profiles")
        case 13: 
            print("Sim Services")
        case 0:
            print("**********Goodbye**********")
            running = False
        case _:
            print("Invalid Input")
