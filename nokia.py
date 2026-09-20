    currentMenu = 0;

    appIsStillRunning = True;
    
    while appIsStillRunning:
      print();
      
      match currentMenu:
        case 0:
            
          print("=======================")
          print("     Nokia 5510 Menu   ")
          print("=======================")
          print("1. Phone Book")
          print("2. Messages")
          print("3. Chat")
          print("4. Call Register");
          print("5.Tone")
          print("6.Settings");
          print("-1. Exit");

          
        case 1:
            
          print("Phone Book");
          print("1.Search");
          print("2.Service");
          print("3.Add Name");
          print("4.Erase");
          print("5.Edit");
          print("6.Copy");
          print("7.Assign Tone");
          print("8.Send B'Card");
          print("9.Options");
          print("0. Back");
          print("99 Main Menu");
          print("-1. Exit");

          
        case 2:
  
          print("Messages");
          print("1.Write Message");
          print("2.Inbox");
          print("3.Outbox");
          print("4.Picture Message");
          print("5.Templates");
          print("6.Smileys");
          print("7.Message Settings");
          print("0.Back");
          print("99 Main Menu");
          print("-1. Exit");

          
        case 3:
            
          print("Chat");
          print("0.Back");
          print("99 Main Menu");
          print("-1. Exit");

          
        case 4:
            
          print("Call Register");
          print("1.Missed Calls");
          print("2.Received Calls");
          print("3.Dialed number");
          print("4.Erase Recent Call List");
          print("0.Back");
          print("99 Main Menu");
          print("-1. Exit");

        
        case 5:
            
          print("Tone");
          print("1.Ringing Tone");
          print("2.Ringing Volume");
          print("3.Incoming Call Alert");
          print("4.Message Alert Tone");
          print("5.Keypad Tones");
          print("6.Warning Tone");
          print("7.Vibrating Alert");
          print("8.Screen Saver");
          print("0.Back");
          print("99 Main Menu");
          print("-1. Exit");

          
        case 6:
            
          print("Settings");
          print("1.Call Settings");
          print("2.Automatic Redial");
          print("3.Speed dialing");
          print("4.Call Waiting Options");
          print("5.Own Number Sending");
          print("6.Phone Line in Use");
          print("7.Automatic Answer");
          print(" 0.Back");
          print("99 Main Menu");
          print("-1. Exit");
          
          
        default:
          print("Options Not Found");
          currentMenu = 0;

      

        currentMenu = int(input("\n Choose an Option: "));

        
        if currentMenu == 99 :
          currentMenu = 0;
          continue;


        if currentMenu == -1 :
          appIsStillRunning = false;
          continue;

