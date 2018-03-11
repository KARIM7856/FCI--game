#include<iostream>
#include<string>
#include<iomanip>
using namespace std;

string encrypt(int msgLength,char secretKey, string msg)
    {
    for (int  i = 0; i <= msgLength;  i++)
    	    	 {
    	    	     msg[i] = secretKey ^ msg[i];
    	    	 }
	return msg;
    }

int input(string userMsg)
    {
	int output;
	cout<<userMsg<<endl;
	while (!(cin >> output))
	    {
		cout<<"Input failed please re-enter:"<<endl;
	    	cin.clear();
	    	cin.ignore(1000, '\n');

	    }

	return output;

    }

void Hexa(string hexMsg, int length)
    {
    for (int j = 0; j <= length; j++)
	{
	  cout<<hex<<(int)hexMsg[j];
	}
    cout<<endl;
    }

string hex2stream(const std::string hexstr, std::string& str)
{
    str.resize((hexstr.size() + 1) / 2);

    for (size_t i = 0, j = 0; i < str.size(); i++, j++)
    {
        str[i] = (hexstr[j] & '@' ? hexstr[j] + 9 : hexstr[j]) << 4, j++;
        str[i] |= (hexstr[j] & '@' ? hexstr[j] + 9 : hexstr[j]) & 0xF;
    }
    return str;
}


int main()
 {
	int userDecision=0;
    	int msgLength = 0;
    	string msg =  "";
    	char secretKey;
    	bool isQuit = false;
    	bool isEncrypted = false;

    	while(!isQuit)
	{
    	cout<<"Hello user what do you want to do?"<<endl;
	userDecision = input("1- Encrypt a message.\n"
		                           "2- Decrypt a message.\n"
		                           "Any other number- Quit");

	if (userDecision == 1)
	    {

		string msgPrev = msg;
	        cout<<"Enter a message to be Encrypted : "<<endl;
	        cin.ignore();
	        getline(cin, msg);

	        if (msg == msgPrev)
	             {
	             cout<<"You know, you can use decrypt for decryption."<<endl;
	             continue;
	             }

	        cout<<"Please enter the secret key : ";
	        cin>>secretKey;

	        msgLength = msg.length();
	        msg = encrypt(msgLength, secretKey, msg);
	        isEncrypted = true;

	        cout<<"Encrypted message is \""<<msg<<"\""<<endl<<"Hexa : ";
	        Hexa(msg, msgLength);
	}
	else if (userDecision == 2)
	    {

		int decryptDecision=0;

		cout<<"Let's decrypt a secret message. "<<endl;

		decryptDecision = input("1- Decrypt latest encrypted message.\n"
			                                 "2- Decrypt another message.\n"
			                                 "Any other number- Quit\n");

		if (decryptDecision == 1)
		    {
		    if(isEncrypted == false)
		    		    {
		    			cout<<"There is no message to be decrypted.\n";
		    			continue;
		    		    }
			cout<<"What was the secret key? ";
			cin>>secretKey;

			msg = encrypt(msgLength, secretKey, msg);

			cout<<"The original message was \""<<msg<<"\""<<endl;
		    }

		else if (decryptDecision == 2)
		    {
					int hexDecision = 0;
				    cout<<"Enter a message to be decrypted : "<<endl;
				    hexDecision = input("1- Plain Text\n"
						    	    	    	    	    	   "2- Hexadecimal\n"
						    	    	    	    	    	   "3- Back to main menu");
		    	         if (hexDecision == 1)
		    	         {
					    cin.ignore();
					    getline(cin, msg);
		    	         }
		    	         else if (hexDecision == 2)
		    	         {
		    	     	    cin>>msg;
		    	     	    msg = hex2stream(msg, msg);
		    	         }
		    	         else
		    	     	    continue;
		    	         cout<<"What was the secret key ? ";
		    	         cin>>secretKey;

		    	        msgLength = msg.length();
		    	        msg = encrypt(msgLength, secretKey, msg);

		    	        cout<<"Message was \""<<msg<<"\""<<endl;
		    }
		else
		    isQuit = true;
	    }
	else
	    isQuit = true;
	}
}
